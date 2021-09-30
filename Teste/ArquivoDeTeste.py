import pyautogui
import os
import time

import sys
sys.path.append("..")
from utils.Functions import *


def teste():
    time.sleep(2)
    p_Teclas = ObterPosicoesTeclas()
    if p_Teclas == TECLA_NAO_ENCONTRADA:
        print ("Erro Login")
        return TECLA_NAO_ENCONTRADA
   
    #Posicoes de cada tecla
    p_Left = p_Teclas[1]          # Recebem (x,y) 
    p_Up = p_Teclas[2]
    p_Right = p_Teclas[3]
    p_Down = p_Teclas[4]
    p_Z = p_Teclas[5]
    p_B = p_Teclas[7]
    p_F2 = p_Teclas[9]
    p_F7 = p_Teclas[9]
    p_ESC = p_Teclas[10]
   
    # Verificando a região atual 
    regiao = RegiaoAtual(p_F2)
    
    # Indo para Kanto, se o personagem não estiver.
    if regiao != "Kanto":
        print ("Mudando para Kanto...")
        erro = TrocarRegiao(p_Left, p_Up, p_Right, p_Down, p_Z, p_F2, regiaoOrigem=regiao, regiaoDestino="Kanto")
        if erro != OK:
            return erro
     
teste()