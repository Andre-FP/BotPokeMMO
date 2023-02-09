from functions.utils.parametros import *
from functions.utils.erros import *
from functions.tela import CheckPixel, PosicaoEDimensaoDaImagem, CentroDaImagem
from functions.teclado import Teclado
from functions.verificacao import EncontrarAbaPokebola


def LancarPokebola(qntdPokebolas):
    '''
    Lança pokebola, ou lança a bola que tiver (sem ser master ball) se as pokebolas
    acabaram durante a batalha.

    Args: 
        qntdPokebolas(int):
            qntd atual de pokebolas

    Returns:   
        OK
        ERRO_LUTAR_LANCAR_POKEBOLA
        SO_TEM_MASTER_BALL
        LANCOU_BOLA_ENCONTRADA    
    '''
    # Verifica se já apareceu o botao "Lutar", indicando que pode lançar a pokebola
    if not CheckPixel("Lutar"):
        return ERRO_LUTAR_LANCAR_POKEBOLA   
    
    # Selecionando a aba "Mochila"
    Teclado(t_Right)                
    Teclado(t_Z)
    
    # SELECIONANDO A ABA DE "POKEBOLAS" DA MOCHILA, PARA ENTÃO USAR A POKEBOLA
    if qntdPokebolas > 0:
        erro = EncontrarAbaPokebola(bola="Pokebola")
        if erro != OK:
            return erro
    ########
    # Caso já tenha acabado as pokebolas.
    else: 
        # Pokebola é verificada para ver se tem pokebolas residuais (< 99)
        outras_bolas = ["Pokebola", "GreatBall", "UltraBall"]
        for bola in outras_bolas:
            encontrou = EncontrarAbaPokebola(bola=bola)
            if encontrou == OK: break

    ################## SE ACABOU AS POKEBOLAS ENQUANTO LUTAVA ###############

    """if qntdPokebolas <= 0:
        print("As pokebolas dos packs acabaram")          
        print("Verificando se tem alguma qntd residual...")
         
        if not CheckPixel("Pokebola"):
            print("Nao tem pokebola residual, usar Great ball nessa captura.")
            
            # Pegando a cor da bola inicial:
            im = pyautogui.screenshot()
            corBolaAnterior = im.getpixel((627, 714)) # posicao das bolas 

            chegouFim = False
            qntdPack = 0
            while not CheckPixel("GreatBall", tentativas=5) and not chegouFim:  
                Teclado(t_Down)
                time.sleep(0.1)
                im = pyautogui.screenshot()
                corBolaAtual = im.getpixel((627, 714))
                
                if corBolaAtual == corBolaAnterior: # qr dizer que encontrou um outro pack da mesma bola
                    qntdPack += 1                   # ou chegou ao fim
                
                if qntdPack == 4:       #Assumindo que se encontrar 4 vezes a mesma bola, n é pq é outro pack
                    chegouFim = True    # e sim pq chegou ao fim 
                
                corBolaAnterior = corBolaAtual

            if chegouFim: # Nao tem great ball
                chegouFim = False
                qntdPack = 0
                
                # Verificando se tem ultra ball
                while not CheckPixel("UltraBall", tentativas=5) and not chegouFim:  
                    Teclado(t_Up)
                    time.sleep(0.1)
                    im = pyautogui.screenshot()
                    corBolaAtual = im.getpixel((627, 714))
                    
                    if corBolaAtual == corBolaAnterior: # qr dizer que encontrou um outro pack da mesma bola
                        qntdPack += 1                   # ou chegou ao fim ao fim
                    
                    if qntdPack == 4:       #Assumindo que se encontrar 4 vezes a mesma bola, n é pq é outro pack
                        chegouFim = True    # e sim pq chegou ao fim 
                    
                    corBolaAnterior = corBolaAtual

                # Se nao encontrou nem ultra ball
                if chegouFim:
                    # Lança a bola atual se n for uma master ball
                    if CheckPixel("MasterBall"):
                        Teclado(t_Down)
                        if CheckPixel("MasterBall"):
                            # Só tem master ball, dar Run.
                            return SO_TEM_MASTER_BALL"""

    # Lanca a bola encontrada (pokebola, great ball, ultra ball, ou outra)
    Teclado(t_Z)
    return OK

def VerificarPokemonCapturado(manter_pokemon=False, tentativas=50):
    '''
    Verifica se o pokemon capturado tem IV31 ou não

    Argumentos: tentativas -> inteiro positivo -> qntd de tentativas pra achar a janela do pokemon 
    
    Retornos:   POKEMON_NAO_CAPTURADO
                CAPTURA_CONFIRMADA
                ERRO_VERIFICAR_POKE
                COM_IV31
                SEM_IV31
    '''
    # Verificando se a janela do pokemon já apareceu
    # Imagem do botao de IV
    posicaoSimboloIV = CentroDaImagem(PosicaoEDimensaoDaImagem("PokemonCapturado1.png",\
    "PokemonCapturado2.png", "PokemonCapturado3.png", tentativas=tentativas))
    if posicaoSimboloIV == IMG_NAO_ENCONTRADA: # Pokemon nao foi capturado
        print ("Pokemon nao foi capturado ou o personagem esta numa acao diferente")
        return POKEMON_NAO_CAPTURADO
    if manter_pokemon:
        return CAPTURA_CONFIRMADA

    #Clica no botao de IV
    pyautogui.moveTo(posicaoSimboloIV)
    pyautogui.click()

    # Verifica se abriu a aba e espera um determinado tempo ate abrir
    pixelHelp = (posicaoSimboloIV[x] + 47, posicaoSimboloIV[y] + 257)
    if not CheckPixel("AbaDoIV", pixel=pixelHelp, espera=0.05):
        print("Nao carregou depois de ter apertado o botao do IV, ou a cor n está cadastrada ainda")
        return ERRO_VERIFICAR_POKE
    
    ###### Verificando se tem algum IV 31 ######

    # Matriz de posicao absoluta dos IVs do pokemon. Consegue-se suas posicoes
    # a partir da posicao do botao de IV. Cada posicao corresponde a uma tupla
    posicaoIVs = []
    
    # Posicao absoluta do primeiro IV.
    # (54, 41) eh a posicao relativa do IV1 ao botao     
    posicaoIV1 = (posicaoSimboloIV[x] + 54, posicaoSimboloIV[y] + 41)

    posicaoIVs.append(posicaoIV1)
    
    # Checa se o pixel analisado eh o pixel q identifica o IV 31. Verifica 6 pixels pq sao 6 IVs
    proximoIV = 0
    while not CheckPixel("IV31", pixel=posicaoIVs[proximoIV]) and proximoIV <= 5:
        proximoIV += 1
        posicaoIVs.append((posicaoIV1[x], posicaoIV1[y] + 32*proximoIV)) 
    
    # Nenhum eh igual a 31
    if proximoIV == 6:
        print ("Nao achou IV 31")
        return SEM_IV31
    
    # Achou um IV 31
    print ("IV", proximoIV + 1,"= 31")    
    print ("Fim")
    return COM_IV31

def GuardarOuRelease(status, isShiny=False):
    '''
    Se tiver algum IV 31, guarda o pokemon capturado.
    Se não tiver, joga ele fora.

    Args: 
        status(COM_IV31 ou SEM_IV31):
            informação se tem IV 31 ou não. 
                
    Returns:
        POKEMON_GUARDADO
        POKEMON_RELEASED
        STATUS_INVALIDO 
    '''

    if status == COM_IV31 or isShiny:
        Teclado(t_ESC)# Fecha a aba de status
        
        if isShiny:
            shinyFile = open("shinyFile.txt", "a")
            shinyFile.write("1")
            shinyFile.close()

        return POKEMON_GUARDADO

    elif status == SEM_IV31:
        print ("IV ruim")
        print ("Jogando pokemon fora...")
        # Movendo para o menu do release
        pyautogui.moveRel(123, -2)
        pyautogui.click()
        
        # Movendo para o botao release
        pyautogui.moveRel(-90, 153)
        pyautogui.click()
        
        # Clicando em confirmar
        pyautogui.moveTo((961, 522))
        pyautogui.click()
        #Então, volta pro while ateh o PP do false swipe acabar
        return POKEMON_RELEASED

    else:
        return STATUS_INVALIDO