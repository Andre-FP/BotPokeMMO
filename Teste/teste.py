
import sys

import keyboard
sys.path.append("..")
from utils.configuracoesIniciais import Teclado, TECLAS
import time

encontros = 1
with open("teste.txt", "w") as f: 
    f.write(str(encontros))