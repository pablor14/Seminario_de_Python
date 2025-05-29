#-*-coding: utf-8-*-
import socket
import signal
import threading
import random
import time
import math

continua = True
i=0;
href=0.5;
mutex = threading.Semaphore(1)
mutexr = threading.Semaphore(1)

def sigint_handler(signum, frame):
	mutexr.release()
	
def UI():
	global href, client, continua
	while continua:
		try:
			mutexr.acquire()
			mutex.acquire()
			print("")
			print("----------------------------------------------------")
			user_input=input("Digite o novo valor de href:  ")
			print("----------------------------------------------------")		
			print("")
			href=float(user_input)
			a=str(href)
			client.send(a.encode())
			mutex.release()
		except EOFError:
			print ("Saindo do programa")
			continua = False
			a = "-.1"

			client.send(a.encode())
			mutex.release()
	print("Saindo da UI")

ip = '127.0.0.1' # Endereço IP do Servidor;
port = 1267 # Porta que o Servidor se encontra
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Comunicação TCP
address = (ip, port) # Endereço
server.bind(address)
server.listen(2) # Quantidade de threads a serem conectadas

print("[*] Esperando Conexões:\n IP: "+str(ip)+"\nPorta:"+str(port))

(client, addr) = server.accept() 
print("[*] Cliente :\n IP: "+str(addr[0])+"\nPorta:"+str(addr[1])+" conectado!")

w = open("historiador.txt", "w")
w.write("HREF HCALCULADA QOUT QIN;\n")
signal.signal(signal.SIGINT, sigint_handler)

KB = threading.Thread(target=UI)
KB.start()
		
while continua:
	mutex.acquire()
	data = client.recv(1024)
	data = data.decode()
	w.write(data)
	valores = data.split()
	print("----------------------------------------------------")
	print("Altura Referencia: "+valores[0]+"\n"+"Altura Atual: "+valores[1]+"\n"+"Vazao de Saada: "+valores[2]+"\n"+"Vazao de Entrada: "+valores[3]+"\n")
	print("----------------------------------------------------")
	mutex.release()
	try:
		time.sleep(.1)
	except IOError:
		pass
print("Saindo do logger")
KB.join()
w.close()
server.close()



	
	










