import pyautogui
import os
import time
from configuracoesIniciais import *
from Functions import *

#Conclusoes: pixel absoluto (627, 714) esta correto
# Cor1: (248, 144, 56)
# Cor2: (246, 143, 56)
# Cor3: (244, 142, 55)

def testeCorPosicao():

    p_Teclas = ObterPosicoesTeclas()
    p_Up = p_Teclas[2]
    p_Down = p_Teclas[4]
    p_Left = p_Teclas[1]          # Recebem (x,y) 
    p_Right = p_Teclas[3]
    p_Z = p_Teclas[5]
    p_ESC = p_Teclas[11]
    

    direita = False
    while 1:
        if direita:
            ClickTecladoVirtual(p_Right, clicks=19, modo="Surf")
            direita = False
        else:
            ClickTecladoVirtual(p_Left, clicks=19, modo="Surf")
            direita = True
        time.sleep(5)

    '''
    while 1:
        pyautogui.moveTo(p_Down)
        pyautogui.click(p_Down)
        time.sleep(0.1)
        pyautogui.click(p_Down)
        pyautogui.moveTo(p_Left)
        pyautogui.click(p_Left)
        time.sleep(0.1)
    '''
    
    
    
testeCorPosicao()






