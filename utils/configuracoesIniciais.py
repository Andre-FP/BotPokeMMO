 # Autor: Andre de Farias Pereira
 # Idade: 20 anos/ 21 anos
 # Descricao: Testando algumas funcionalidades
 
import pyautogui
import os
import time
import keyboard

POKEMMOFILE = "C:\\\"Arquivos de Programas\"\\PokeMMO\\PokeMMO.exe"
ROOT = "."
IMAGESDIR = os.path.join(ROOT, "imagens") 
FILESDIR = os.path.join(ROOT, "arquivos")
TECLAS = {
    "Fly": "f1",
    "Bolsa": "b",
    "Up": "w",
    "Left": "a",
    "Down": "s",
    "Right": "d",
    "Z": "z",
    "X": "x",
    "Bike": "3",
    "Regar": "4",
    "SuperRepel": "5",
    "Repel": "6",
    "Pescar": "7",
    "SweetScent": "8",
    "Teleport": "9",
    "Enter": "enter",
    "ESC": "esc",
}

# GLOBAL VARIABLES
default_position_image = 0

## Coordenadas para serem usado em listas (coordx[x], coordy[y])
x=0
y=1

#ERROS:
OK = "0 - OK"
FALTANDO_ARGUMENTOS = "1 - FALTANDO_ARGUMENTOS"
IMG_NAO_ENCONTRADA = False
IMG_ENCONTRADA = True
TECLA_NAO_ENCONTRADA = "2 - TECLA_NAO_ENCONTRADA"
FUNCIONALIDADE_NAO_CADASTRADA = "6 - FUNCIONALIDADE_NAO_CADASTRADA"

'''
 Verifica se a proxima pagina ja carregou e retorna a posicao da imagem. 
 Se nao carregou ainda, espera um determinado tempo e da erro se ultrapassa-lo.
'''
def PosicaoEDimensaoDaImagem(imagem1=None, imagem2=None, imagem3=None, imagem4=None, espera = 0.0, tentativas=11):
    '''
    O tempo de execucao dessa funcao com o tempo de espera = 0.0 eh de mais ou menos 2.2 segundos.
    Nao sei se depende da imagem.
    '''
    imagens = [imagem1, imagem2, imagem3, imagem4]
    if imagens[3] == None:
        del(imagens[3])
        if imagens[2] == None: 
            del(imagens[2])
            if imagens[1] == None:
                del(imagens[1])
                if imagens[0] == None:
                    return FALTANDO_ARGUMENTOS
    
    coordenadaImagem = None 

    loop = 0
    while coordenadaImagem == None:
        for imagem in imagens:
            image_path = os.path.join(IMAGESDIR, imagem)
            coordenadaImagem = pyautogui.locateOnScreen(image_path)    
            if coordenadaImagem != None:
                print("Imagem \"" + imagem + "\" encontrada")
                print("Corrdenada:", coordenadaImagem)
                return coordenadaImagem

            print ("Imagem \"" + imagem + "\" NÃO encontrada. tentativa =", loop + 1)
        time.sleep(espera)
        loop += 1
        if loop == tentativas:
            return IMG_NAO_ENCONTRADA
    
def ImagemEncontrada(imagem1=None, imagem2=None, imagem3=None, imagem4=None, espera = 0.0, tentativas=11):
    '''
    Verifica se a imagem especificada já apareceu na tela.

    Args: 
        imagem(str):
            Nome da imagem.png
        espera(float):
            tempo de espera para novas tentativas
        tentativas(int):
            numero de tentativas

    Returns:   
        OK
        IMG_NAO_ENCONTRADA
        FALTANDO_ARGUMENTOS
        IMG_ENCONTRADA
    '''
    imagemEncontrada = PosicaoEDimensaoDaImagem(imagem1, imagem2, imagem3, imagem4, espera, tentativas)

    if imagemEncontrada == IMG_NAO_ENCONTRADA:
        return IMG_NAO_ENCONTRADA    
    elif imagemEncontrada == FALTANDO_ARGUMENTOS:
        return FALTANDO_ARGUMENTOS

    return IMG_ENCONTRADA

def CentroDaImagem(dimensoes=None):
    
    if dimensoes == None or dimensoes == FALTANDO_ARGUMENTOS:
        return FALTANDO_ARGUMENTOS
    elif dimensoes == IMG_NAO_ENCONTRADA:
        return dimensoes
    centro = pyautogui.center(dimensoes)
    return centro
    
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

def Login(bot):
    '''
    Abre os programas necessários e realiza o login no PokeMMO.

    Args: 
        bot(str):
            bot que vai ser executado.
    
    Returns: 
        list: Lista contendo as posições de cada tecla do teclado
        str: TECLA_NAO_ENCONTRADA
        str: IMG_NAO_ENCONTRADA
    '''
    pyautogui.FAILSAFE = True
    
    # -- Abrindo Pokemmo -- #
    print ("Abrindo PokeMMO...")
    execPoke = f"start {POKEMMOFILE}"
    os.system(execPoke)
    
    # -- Pegando a coordenada do botao Conectar da pagina de login -- #
    print ("Logando...")
    coordenadaConectar = CentroDaImagem(PosicaoEDimensaoDaImagem("BotaoConectar.png", "BotaoConectar2.png", "BotaoConectar3.png"))
    if coordenadaConectar == IMG_NAO_ENCONTRADA:
        print ("Erro Login: Conectar")
        return IMG_NAO_ENCONTRADA

    # -- Clicando no botao conectar -- #
    pyautogui.click(coordenadaConectar[0], coordenadaConectar[1])
    #-------------------------------------------------------#
    # -- Apertando enter para as proximas etapas de login -- #
    
    #### 1 - Selecionar Servidor

    #Verifica se a pagina Selecionar Servidor ja foi aberta
    encontrouImagemServidor = ImagemEncontrada("SelecionarServidor.png", "SelecionarServidor2.png", "SelecionarServidor3.png")
    if not encontrouImagemServidor:
        print ("Erro Login: Selecionar Servidor")
        return IMG_NAO_ENCONTRADA
            
    #Clica no enter
    Teclado(TECLAS["Enter"])
    ##---------------------------------------------    
    
    #### 2 - Selecionar Personagem
    encontrouImagemServidor = ImagemEncontrada("SelecaoPersonagem.png", "SelecaoPersonagem2.png", 
    "SelecaoPersonagem3.png", "SelecaoPersonagem4.png")
    if not encontrouImagemServidor:
        print ("Erro Login: Selecao Personagem")
        return IMG_NAO_ENCONTRADA

    Teclado(TECLAS["Enter"])
    time.sleep(3.0)
    return OK
