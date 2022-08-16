import sys
sys.path.append("..")
from utils.Functions import *
import time

time.sleep(2)

# Apertando Run.
Teclado(t_Z)
Teclado(t_Right)
Teclado(t_Z)
Teclado(t_Z)
time.sleep(3)

print("Indo para o Centro Pokemon...")
print("Usando teleport...")
Teclado(t_Teleport)

######### VERIFICA SE USOU TELEPORT ########
if not CheckPixel("balaoChat"):

    # Verifica se não conseguiu escapar da batalha anterior.
    # Se não conseguiu, usa "Run" até conseguir.
    erro = RunUntilRunHorde()
    print("RunUntilRunHorde:", erro)

    # Usando teleport
    Teclado(t_Teleport)
    if not CheckPixel("balaoChat"):
        print("Erro", ERRO_TELEPORT)
# --------------------------------------------------------------------#
time.sleep(2)

if not CheckPixel("cabeloJoyHoenn", pixel=(986, 349)):
    print ("Personagem não conseguiu utilizar o teleport.")
    print("Erro", ERRO_TELEPORT)

erro = UsarCPESair(regiao="Hoenn")
if erro != OK:
    print ("Erro em UsarCPESair")
    print("Erro", erro)
