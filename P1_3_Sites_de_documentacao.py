'''
    Arquivo com exemplos e sites de documentação de bibliotecas Python.

'''
############# OpenCV #############
# OpenCV: https://docs.opencv.org/4.x/
import cv2

img = cv2.imread('Dados_para_exemplo\exemplo.png')                      # Lê imagem
cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)        # Converte para escala de cinza
cv2.imshow('Cinza', cinza)                           # Exibe imagem
cv2.waitKey(0)                                       # Espera tecla


############# KEYBOARD #############
# # keyboard: https://pypi.org/project/keyboard/
import keyboard
keyboard.press_and_release('ctrl+t')        # Pressiona teclas
keyboard.write('oiiii')                     # Escreve texto
keyboard.read_hotkey()                      # Recebe algo do teclado 

############# MATPLOTLIB PYPLOT #############
# # matplotlib: https://matplotlib.org/stable/index.html
# https://matplotlib.org/stable/tutorials/pyplot.html#sphx-glr-tutorials-pyplot-py
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()

############# NUMPY #############
# Numpy https://docs.scipy.org/doc/numpy-1.3.x/reference/
import numpy as np
list = np.random.randint(0, 100, 20)

############# Datas Horas e fuso horarios #############
# Time: https://docs.python.org/3/library/time.html
# Datetime: https://docs.python.org/3/library/datetime.html
# ZoneInfo: https://docs.python.org/3/library/zoneinfo.html
# Locale: https://docs.python.org/3/library/locale.html
import locale
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

############# Pprint #############
# Printa objetos de forma mais legivel
import pprint
pprint.pprint(list)

############# STRING #############
# https://docs.python.org/3/library/string.html
import string
string.ascii_letters

############# RANDOM #############
# https://docs.python.org/pt-br/3.13/library/random.html
import random
print(random.choices([1,2,3,4,5,6,7,8,9,0], k = 3))   # 3 valores aleatorios da lista
print(random.shuffle([1,2,3,4,5,6,7,8,9,0]))          # Embaralha caracteres da lista

############# QR CODE #############
#Documentação: https://github.com/lincolnloop/python-qrcode
import qrcode
imagem = qrcode.make("https://github.com/Lariterrinha/Seminario_de_Python")
imagem.save("qrcode.png")

############# PANDAS #############
# Pandas: https://pandas.pydata.org/docs/ (Manipulação de dados, tabelas e séries)
import pandas as pd
url = 'https://drive.google.com/uc?authuser=0&id=1Ru7s-x3YJuStZK1mqr_qNqiHVvdHUN66&export=download'
cotacao_df = pd.read_csv(url)

############# TQDM #############
# TQDM:  
from tqdm import tqdm
pbar = tqdm(total=100, position = 0 , leave = True)                         # Barra de progresso 0 a 100 na mesma linha

############# Openpyxl #############
# Openpyxl: https://openpyxl.readthedocs.io/en/stable/ (Manipulação de planilhas Excel)
from openpyxl import Workbook, load_workbook
planilha = load_workbook(r'D:\Eng_computacao\Linguagens de Programacao\Seminario_de_Python\Dados_para_exemplo\Produtos.xlsx')      # Abre a planilha
planilha.active['A1'] = 'NOME'                                                                                                      # Escreve na célula A1 da aba padrão
planilha.save(r'D:\Eng_computacao\Linguagens de Programacao\Seminario_de_Python\Dados_para_exemplo\ProdutosNOVO.xlsx')             # Salva a planilha

############# TQDM #############
# TQDM:  
from tqdm import tqdm
pbar = tqdm(total=100, position = 0 , leave = True)                         # Barra de progresso 0 a 100 na mesma linha
for i in range(100):
    pbar.update(1)

############# REQUESTS e IO #############
# Requests: https://docs.python-requests.org/en/latest/
# Importando arquivos da internet (com requests)
import requests
import io
url = 'https://portalweb.cooxupe.com.br:9080/portal/precohistoricocafe_2.jsp?d-3496238-e=2&6578706f7274=1'
conteudo_url = requests.get(url).content
arquivo = io.StringIO(conteudo_url.decode('latin1'))    # decode = (tipos de enconding)
cafe_df = pd.read_csv(arquivo, sep=r'\t', engine='python')