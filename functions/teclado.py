from functions.utils.parametros import *
from functions.utils.erros import *

def Teclado(tecla, clicks=1, modo="andar", virar=False, interval=1):
    '''
    Tecla de um modo especifico (com intervalo entre tecladas 
    definido pelo modo). As setas não sao reconhecidas pelo "keyboard".

    Argumentos: 
        tecla(str):
            tecla a ser pressionada
        clicks(int):
            numero de cliques 
        modo(str):
            deve ser uma das adicionadas ("andar", "correr", "bike" 
            ou "custom")

    Returns:   
        str: OK
        str: FUNCIONALIDADE_NAO_CADASTRADA
    '''
    if modo == "andar":
        interval = 0.2
    elif modo == "correr":
        interval = 0.15
    elif modo == "bike":
        interval = 0.03
    elif modo == "custom":
        pass
    else:
        return FUNCIONALIDADE_NAO_CADASTRADA
    
    if virar:
        if modo == "andar":
            interval = 0.05
        elif modo == "bike":
            interval = 0.05
        elif modo != "custom":
            interval = 0.001     
    
    for count in range(clicks):
        keyboard.press(tecla)
        time.sleep(0.05)
        keyboard.release(tecla)
        time.sleep(interval)

    return OK