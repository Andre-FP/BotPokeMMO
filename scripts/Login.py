 # Autor: Andre de Farias Pereira
 # Idade: 20 anos/ 21 anos
 # Descricao: Testando algumas funcionalidades

import sys
sys.path.append('..')
from functions.utils.parametros import *
from functions.utils.erros import *
from functions.teclado import *
from functions.tela import *

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