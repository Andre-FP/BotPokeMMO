import pyautogui
import os
import time

import sys
sys.path.append('..')
from utils.Functions import *


def PosicaoAtual():
    #print ("Posicao Atual: ", pyautogui.position())
    # centro = (1029, 453)
    # L = (921, 484)
    # Relacao : (95, -2)
    
    # cor 1: (248, 160, 176)
    # cor 2: (83, 90, 96)
    # cor 3: (83, 90, 95)
    
    time.sleep(3)
    posicao = pyautogui.position()
    print ("Posicao alvo:", posicao)
    
    while 1:
        pyautogui.moveTo(900, 50, duration=0.5)
        time.sleep(2)
        pyautogui.moveTo(posicao, duration=0.5)


    '''
    while 1:
        t_BolsaotaoPlantar = CentroDaImagem(PosicaoEDimensaoDaImagem("SementePicSelecionada1.png", "SementePicSelecionada2.png", 
                                "SementePicSelecionada3.png"))
        if t_BolsaotaoPlantar == IMG_NAO_ENCONTRADA:
            print ("Não encontrada.")
            return -1
        else:
            pyautogui.moveTo(t_BolsaotaoPlantar)
            time.sleep(2)
            print ("Encontrada.")
        pyautogui.moveTo(500, 500)
       
    '''
    '''
    while 1:
        time.sleep(2)
        
        posicao = CentroDaImagem(PosicaoEDimensaoDaImagem("RegiaoUnova1.png", "RegiaoUnova2.png", "RegiaoUnova3.png"))   
        
        pyautogui.moveTo(posicao)
        print ("Posicao referencia:", posicao)
        posicaoRelativaCidade = (posicaoCidade[0] - posicao[0], posicaoCidade[1] - posicao[1])
        print ("Posição relativa:", posicaoRelativaCidade)
        time.sleep(0.5)
        pyautogui.moveRel(posicaoRelativaCidade)
    '''
    return 0
    # (x=631, y=172)

PosicaoAtual()