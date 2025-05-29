# -*- coding: utf-8 -*-

import threading
import random
import time
import math
import socket
import string

href = 0.5        # Altura de Referência
qinAtual = 0      # Condição Inical Para Vazão de Entrada
qinPassado = 0    # Ação de Controle Passada
hAtual = 0.5      # Condição Inicial Para Altura do Tanque
hPassado = 0.5
erroPassado = 0   # Erro Passado
erroAtual = 0     # Erro Atual
Cv = 0.05         # Coeficiente de Carga da Planta
qout = 0          # Vazao de Saída
continua = True

# ===== Saturação da vazão de controle =====
QIN_MIN = 0.0         # mínimo (normalmente zero)
QIN_MAX = 0.0333     # exemplo: 200 L/min = 0,00333 m³/s

def saturate(value, vmin, vmax):
    return max(min(value, vmax), vmin)
# ==========================================

mutex = threading.Semaphore(1)
qin = [0]
alturaCalculada = [0.5]
erro = [0] 
clientSoftPLC = socket.socket()

def receive_thread():
    global clientSoftPLC, href, mutex, continua
    while continua:
        href_new = clientSoftPLC.recv(3).decode()
        if href_new == "-.1":
            continua = False
        else:
            mutex.acquire()
            print("Mudanca de Href {}".format(href_new))
            href = float(href_new)
            mutex.release()

def softPLC_thread():
    global href, qinAtual, qinPassado, hAtual, hPassado, erroPassado, erroAtual, Cv, qout, mutex, continua
    while continua:
        mutex.acquire()
        erroAtual = href - hAtual
        # --- aqui aplicamos a saturação ---
        qin_raw = qinPassado + 10.95 * erroAtual - 7.86 * erroPassado
        qinAtual = saturate(qin_raw, QIN_MIN, QIN_MAX)
        # ====================================
        erroPassado = erroAtual
        qinPassado = qinAtual
        mutex.release()
        time.sleep(0.025)

def process_thread():
    global clientSoftPLC, continua, href, qinAtual, qinPassado, hAtual, hPassado, erroPassado, erroAtual, Cv, qout, mutex
    ip = '127.0.0.1'
    port = 1267
    address = (ip, port)
    clientSoftPLC.connect(address)

    while continua:
        time.sleep(0.050)
        mutex.acquire()
        print("----------------------------------------------------")
        print("Altura Referência: "+str(href))
        print("Altura Calculada: "+str(hAtual)+"m")
        print("Qout: "+str(qout))
        print("Qin(t)="+str(qinAtual))
        print("----------------------------------------------------")        
        message = f"{href} {hAtual} {qout} {qinAtual} ;\n"
        clientSoftPLC.send(message.encode())

        hAtual = max(0.997*hPassado + 0.0590*qinAtual + 0.0590*qinPassado, 0.0)
        qout = Cv*math.sqrt(hAtual)
        hPassado = hAtual
        mutex.release()

tPLC = threading.Thread(target=softPLC_thread)
tProcess = threading.Thread(target=process_thread)
receive_thread = threading.Thread(target=receive_thread)

tPLC.start()
tProcess.start()
receive_thread.start()

tPLC.join()
tProcess.join()
receive_thread.join()
clientSoftPLC.close()
