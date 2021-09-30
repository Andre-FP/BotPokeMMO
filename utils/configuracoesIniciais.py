 # Autor: Andre de Farias Pereira
 # Idade: 20 anos
 # Descricao: Testando algumas funcionalidades
 
import pyautogui
import os
import time

POKEMMOFILE = "C:\\\"Arquivos de Programas\"\\PokeMMO\\PokeMMO.exe"
IMAGESDIR = "C:\\Users\\andre\\OneDrive\\Área de Trabalho\\BotPokeMMO\\imagens\\"
FILESDIR = "C:\\Users\\andre\\OneDrive\\Área de Trabalho\\BotPokeMMO\\arquivos\\"

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
    
    global default_position_image
    print ("default_position_image =", default_position_image)
    
    print("\n", imagens, "\n")
    
    if default_position_image == 'first_to_second':
        # Colocando a primeira posição como segunda.
        imagens.insert(2, imagens[0])
        print("\n", imagens, "\n")        
        del(imagens[0])
    else:
        # Colocando a imagem padrao como primeiro
        imagens.insert(0, imagens[default_position_image])
        print("\n", imagens, "\n")
        del(imagens[default_position_image + 1])
    
    print("\n", imagens, "\n")
    
    coordenadaImagem = None 

    loop = 0
    while coordenadaImagem == None:
        for imagem in imagens:
            coordenadaImagem = pyautogui.locateOnScreen(IMAGESDIR + imagem)    
            if coordenadaImagem != None:
                print ("Imagem \"" + imagem + "\" encontrada")
                
                # Se não passou de primeira, então default tem q trocar para o atual.
                # Se passou de primeira, mas no segundo loop, quer dizer que esse default está bom.
                index_image = imagens.index(imagem)
                if index_image != 0:
                    default_position_image = index_image
                elif loop == 1:
                    default_position_image = "first_to_second"
                print ("\ndefault_position_image =", default_position_image, "\n")
                return coordenadaImagem

            print ("Imagem \"" + imagem + "\" NÃO encontrada. tentativa =", loop + 1)
        time.sleep(espera)
        loop += 1
        if loop == tentativas:
            return IMG_NAO_ENCONTRADA
    
def ImagemEncontrada(imagem1=None, imagem2=None, imagem3=None, imagem4=None, espera = 0.0, tentativas=11):
    '''
    Verifica se a imagem especificada já apareceu na tela.

    Argumentos: imagem -> string -> Nome da imagem.png
                espera -> float -> tempo de espera para novas tentativas
                tentativas -> inteiro -> numero de tentativas

    Retornos:   OK
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
    
def ObterPosicoesTeclas():
    posicoesTeclas = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), 
                (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), 
                (0, 0), (0, 0),(0, 0), (0, 0)]

    imagemTeclas = ("KeyEnter.png", "KeyLeft.png", "KeyUp.png", "KeyRight.png", 
    "KeyDown.png", "KeyZ.png", "KeyX.png", "KeyB.png","KeyF1.png", "KeyF2.png", 
    "KeyF5.png", "KeyF6.png", "KeyF7.png", "KeyF8.png", "KeyF9.png", "KeyESC.png", "KeyA.png")
    
    tamanho = len(posicoesTeclas)
    for termo in range (tamanho):
        posicoesTeclas[termo] = CentroDaImagem(PosicaoEDimensaoDaImagem(imagemTeclas[termo]))
        if posicoesTeclas[termo] == IMG_NAO_ENCONTRADA:
            return TECLA_NAO_ENCONTRADA
    
    return tuple(posicoesTeclas)

def Login(bot):
    '''
    Abre os programas necessários e realiza o login no PokeMMO.

    Argumentos: bot -> string -> bot que vai ser executado.
    
    Retornos: 
                Lista contendo as posições de cada tecla do teclado
                TECLA_NAO_ENCONTRADA
                IMG_NAO_ENCONTRADA
    '''
    pyautogui.FAILSAFE = True
    position = pyautogui.position()
    print (position)
    
    # -- Abrindo Pokemmo -- #
    print ("Abrindo PokeMMO...")
    execPoke = f"start {POKEMMOFILE}"
    os.system(execPoke)
    
    # -- Abrindo o teclado virtual -- #
    print ("Abrindo Free Virtual Keyboard...")
    encontrou = False
    while encontrou == False:
        pyautogui.click(245, 1056) #Clica na aba de pesquisa do windows
        time.sleep(0.3)
        pyautogui.typewrite("FreeV")
        posicaoIcone = CentroDaImagem(PosicaoEDimensaoDaImagem("TecladoVirtual.png"))
        if posicaoIcone == IMG_NAO_ENCONTRADA:
            pyautogui.click(29, 1054)#Clica no botao menu iniciar
            time.sleep(1.0)
        else:
            encontrou = True
    pyautogui.moveTo(posicaoIcone[0], posicaoIcone[1], duration=0.3) # Posicao do app na janela de pesquisa
    pyautogui.click() 
    # -- 
    if bot == "CapturarMagikarp" or bot == "MagikarpShiny":
        # Movendo o teclado virtual um pouco mais pra baixo.
        posicaoTeclado = CentroDaImagem(PosicaoEDimensaoDaImagem("TecladoAberto.png"))
        posicaoArrastar = (posicaoTeclado[x] + 50, posicaoTeclado[y])
        pyautogui.moveTo(posicaoArrastar, duration=0.5)
        pyautogui.drag(0, 50, duration=1.0)

    # -- Mapeando as teclas do teclado virtual --#
    print("Mapeando as posicoes das teclas do teclado virtual...")
    posicoesTeclas = ObterPosicoesTeclas()
    print (posicoesTeclas)
    if posicoesTeclas == TECLA_NAO_ENCONTRADA:
        print ("Erro mapeando alguma tecla")
        return TECLA_NAO_ENCONTRADA
    
    #Pegando a posição da tecla Enter
    p_Enter = posicoesTeclas[0]
    # --
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
    pyautogui.click(p_Enter[x], p_Enter[y])
    ##---------------------------------------------    
    
    #### 2 - Selecionar Personagem
    encontrouImagemServidor = ImagemEncontrada("SelecaoPersonagem.png", "SelecaoPersonagem2.png", 
    "SelecaoPersonagem3.png", "SelecaoPersonagem4.png")
    if not encontrouImagemServidor:
        print ("Erro Login: Selecao Personagem")
        return IMG_NAO_ENCONTRADA

    pyautogui.click(p_Enter[x], p_Enter[y])
    time.sleep(3.0)
    return posicoesTeclas 
