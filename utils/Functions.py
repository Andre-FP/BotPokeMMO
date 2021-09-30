import datetime
import sys
sys.path.append('..')
from .configuracoesIniciais import *


POSITIONS_HORDE_MOUSE = [(672, 158), (672, 118), (930, 118), (1192, 118), (1192, 155)]


#ERROS:
CIDADE_NAO_CADASTRADA = "3 - CIDADE_NAO_CADASTRADA"
CIDADE_NAO_ENCONTRADA = "4 - CIDADE_NAO_ENCONTRADA"
REGIAO_NAO_CADASTRADA = "5 - REGIAO_NAO_CADASTRADA"
FUNCIONALIDADE_NAO_CADASTRADA = "6 - FUNCIONALIDADE_NAO_CADASTRADA"
PIXEL_NAO_CADASTRADO = "7 - PIXEL_NAO_CADASTRADO"
PIXEL_ENCONTRADO = True
PIXEL_NAO_ENCONTRADO = False
FALTANDO_ARGUMENTO_POSICAO_PIXEL = "8 - FALTANDO_ARGUMENTO_POSICAO_PIXEL"
BOLSA_NAO_ABRIU = "9 - BOLSA_NAO_ABRIU"
ABA_NAO_ABRIU = "10 - ABA_NAO_ABRIU"
NAO_ENTROU_NO_CP = "11 - NAO_ENTROU_NO_CP"
ERRO_CP = "12 - ERRO_CP" 
ERRO_PESCAR = "13 - ERRO_PESCAR"
NOME_NAO_APARECEU = "14 - NOME_NAO_APARECEU"
MAGIKARP_NAO_ENCONTRADO = "15 - MAGIKARP_NAO_ENCONTRADO"
MAGIKARP_ENCONTRADO = "16 - MAGIKARP_ENCONTRADO"
ERRO_RECONHECER_POKE = "17 - ERRO_RECONHECER_POKE"
MAGIKARP_SHINY = "18 - MAGIKARP_SHINY"
TENTACOOL_NAO_ENCONTRADO = "19 - TENTACOOL_NAO_ENCONTRADO"
TENTACOOL_ENCONTRADO = "20 - TENTACOOL_ENCONTRADO"
TENTACOOL_SHINY = "21 - TENTACOOL_SHINY"
POKEMON_NAO_REGISTRADO = "22 - POKEMON_NAO_REGISTRADO"
POKEMON_SHINY = "23 - POKEMON_SHINY"
VALOR_INVALIDO_PP = "24 - VALOR_INVALIDO_PP"
ERRO_FALSE_SWIPE = "25 - ERRO_FALSE_SWIPE"
ERRO_LANCAR_POKEBOLA = "26 - ERRO_LANCAR_POKEBOLA"
SO_TEM_MASTER_BALL = "27 - SO_TEM_MASTER_BALL"
LANCOU_BOLA_ENCONTRADA = "28 - LANCOU_BOLA_ENCONTRADA"
POKEMON_NAO_CAPTURADO = "29 - POKEMON_NAO_CAPTURADO"
ERRO_VERIFICAR_POKE = "30 - ERRO_VERIFICAR_POKE"
COM_IV31 = "31 - COM_IV31"
SEM_IV31 = "32 - SEM_IV31"
ACABOU_POKEBOLAS = "33 - ACABOU_POKEBOLAS"
ERRO_COMPRAR = "34 - ERRO_COMPRAR"
QNTD_PACK_INVALIDA = "35 - QNTD_PACK_INVALIDA"
CABELO_NAO_CADASTRADO = "36 - CABELO_NAO_CADASTRADO"
ITEM_NAO_CADASTRADO = "37 - ITEM_NAO_CADASTRADO"
POKEMON_GUARDADO = "38 - POKEMON_GUARDADO" 
POKEMON_RELEASED = "39 - POKEMON_RELEASED"
STATUS_INVALIDO = "40 - STATUS_INVALIDO"
LIMITE_DINHEIRO_ALCANCADO = "41 - LIMITE_DINHEIRO_ALCANCADO"
SETA_NAO_ENCONTRADA = "42 - SETA_NAO_ENCONTRADA"
MESMA_REGIAO = "43 - MESMA_REGIAO"
REGIAO_DESTINO_INVALIDA = "44 - REGIAO_DESTINO_INVALIDA"
ERRO_TROCAR_REGIAO = "45 - ERRO_TROCAR_REGIAO"
REGIAO_ORIGEM_INVALIDA = "46 - REGIAO_ORIGEM_INVALIDA"
ERRO_PLANTAR_SEMENTES = "47 - ERRO_PLANTAR_SEMENTES"
SEM_SEMENTE_PICANTE = "48 - SEM_SEMENTE_PICANTE"
POSICIONAMENTO_INVALIDO = "49 - POSICIONAMENTO_INVALIDO"
SENTIDO_INVALIDO = "50 - SENTIDO_INVALIDO"
ERRO_PLANTANDO_NA_TIRA_DE_SLOTS = "51 - ERRO_PLANTANDO_NA_TIRA_DE_SLOTS"
MODO_INVALIDO = "52 - MODO_INVALIDO"
ERRO_CAMINHAR_ATE_SLOT = "53 - ERRO_CAMINHAR_ATE_SLOT"
ERRO_REPEL = "54 - ERRO_REPEL"
ERRO_SURF = "55 - ERRO_SURF"
ESCOLHA_INVALIDA = "56 - ESCOLHA_INVALIDA"
ERRO_REGANDO = "57 - ERRO_REGANDO"
TUPLA_INVALIDA = "58 - TUPLA_INVALIDA"
STRING_VAZIA = "59 - STRING VAZIA"
ERRO_CRIANDO_ARQUIVO = "60 - ERRO_CRIANDO_ARQUIVO"
HORDA_NAO_APARECEU = "61 - HORDA_NAO_APARECEU"
ERRO_SWEET_SCENT = "62 - ERRO_SWEET_SCENT"
LISTA_INVALIDA = "63 - LISTA_INVALIDA"
ACHOU_SHINY_NA_HORDA = 1
ERRO_TELEPORT = "64 - ERRO_TELEPORT"
CADASTROU_NOVA_POSICAO = "65 - CADASTROU_NOVA_POSICAO"
POSICOES_JA_CONHECIDAS = "66 - POSICOES_JA_CONHECIDAS"
ERROR_KILL_POKEMON_HORDE = "67 - ERROR_KILL_POKEMON_HORDE"
SEM_SHINY = "68 - SEM_SHINY"
SEM_PACK_POKEBOLAS = "69 - SEM_PACK_POKEBOLAS"
CAPTURA_CONFIRMADA = "70 - CAPTURA_CONFIRMADA"

def PosicaoCidadeFly(cidade="", regiao=""):
    '''
    Retorna a posicao, no mapa, da cidade desejada.
    Pega a posicao das cidades a partir da posicao do botao amarelo do mapa.

    Argumentos: cidade -> string -> deve ser uma das adicionadas ("Vermilion")
                regiao -> string -> regiao da cidade

    Retornos:   posicao da cidade
                CIDADE_NAO_ENCONTRADA
                CIDADE_NAO_CADASTRADA
    '''
    
    if regiao == "Kanto":
        posicaoReferencia = CentroDaImagem(PosicaoEDimensaoDaImagem("RegiaoKanto1.png", "RegiaoKanto2.png", "RegiaoKanto3.png"))
        if posicaoReferencia == IMG_NAO_ENCONTRADA:
            return CIDADE_NAO_ENCONTRADA

        if cidade == "Vermilion":
            posicaoReferenciaParaCidade = (145, -121)
        
        else:
            return CIDADE_NAO_CADASTRADA
        
    elif regiao == "Hoenn":
        posicaoReferencia = CentroDaImagem(PosicaoEDimensaoDaImagem("RegiaoHoenn1.png", "RegiaoHoenn2.png", "RegiaoHoenn3.png"))
        if posicaoReferencia == IMG_NAO_ENCONTRADA:
            return CIDADE_NAO_ENCONTRADA

        if cidade == "Slateport":
            posicaoReferenciaParaCidade = (-98, -98)
        
        elif cidade == "Rustboro":
            posicaoReferenciaParaCidade = (-289, -219)
        
        elif cidade == "Fortree":
            posicaoReferenciaParaCidade = (-2, -340)

        elif cidade == "Mauville":
            posicaoReferenciaParaCidade = (-98, -197)

        elif cidade == "Lilycove":
            posicaoReferenciaParaCidade = (143, -266)

        elif cidade == "Sootopolis":
            posicaoReferenciaParaCidade = (216, -172)

        elif cidade == "Battle Frontier":
            posicaoReferenciaParaCidade = (238, -52)

        else:
            return CIDADE_NAO_CADASTRADA
    
    
    elif regiao == "Unova":
        posicaoReferencia = CentroDaImagem(PosicaoEDimensaoDaImagem("RegiaoUnova1.png", "RegiaoUnova2.png", "RegiaoUnova3.png"))
        if posicaoReferencia == IMG_NAO_ENCONTRADA:
            return CIDADE_NAO_ENCONTRADA
        
        if cidade == "Castelia":
            posicaoReferenciaParaCidade = (175, -47)
        
        elif cidade == "Mistralton":
            posicaoReferenciaParaCidade = (-102, -237)
        
        elif cidade == "Undella":
            posicaoReferenciaParaCidade = (451, -234)

        else:
            return CIDADE_NAO_CADASTRADA

    else:
        return REGIAO_NAO_CADASTRADA
    

    posicaoCidade = (posicaoReferencia[0] + posicaoReferenciaParaCidade[0], posicaoReferencia[1] + posicaoReferenciaParaCidade[1])
    return posicaoCidade

def ClickTecladoVirtual(p_tecla, clicks=1, modo="andar"):
    '''
    Clica na posicao especificada de um modo especifico (com intervalo entre cliques definidos pelo modo).
    As setas e algumas teclas do teclado nao sao reconhecidas pela funcao pyautogui.click, e por isso,
    deve ser usado essa funcao para clicar nelas.

    Argumentos: p_tecla -> tupla com a posicao do pixel
                clicks -> numero de cliques 
                modo -> string -> deve ser uma das adicionadas ("andar" ou "instantaneo")

    Retornos:   OK
                FUNCIONALIDADE_NAO_CADASTRADA
    '''
    if modo == "andar":
        interval = 0.04
    elif modo == "instantaneo":
        interval = 0.0    
    
    else:
        return FUNCIONALIDADE_NAO_CADASTRADA
    
    for count in range(clicks):
        pyautogui.mouseDown(p_tecla[x], p_tecla[y])
        pyautogui.mouseUp(p_tecla[x], p_tecla[y]) 
        time.sleep(interval)

    return OK

def CheckPixel(name="", pixel=(0,0), espera=0.2, tentativas=50):
    '''
    Checa se o pixel específico é da cor esperada. Só é possível verificar pixels já cadastrados nessa função,
    pois somente esses tem suas cores padrões cadastradas. Dependendo do pixel, será necessário especificar a 
    posição dele no momento, pois sua posição pode variar de acordo com as circunstâncias.

    Argumentos: name -> nome do pixel -> string -> deve ser um já cadastrado
                pixel -> posicao do pixel 
                espera -> segundos -> tempo de espera até realizar uma nova checagem
                tentativas -> inteiro positivo -> numero de tentativas para encontrar o pixel

    Retornos:   PIXEL_NAO_CADASTRADO
                FALTANDO_ARGUMENTO_POSICAO_PIXEL
                PIXEL_NAO_ENCONTRADO
                PIXEL_ENCONTRADO
    '''
    
    if name == "AbaBagPokebola":
        corPadrao1 = (229, 230, 231)
        corPadrao2 = (231, 232, 233)
        corPadrao3 = (227, 228, 229)
        # Usa o pixel da chamada da funcao, pois eh relativo

    elif name == "cabeloJoyKanto":
        corPadrao1 = (248, 160, 176)
        corPadrao2 = (246, 159, 175)
        corPadrao3 = (244, 157, 173)
        if pixel == (0,0):
            pixel = (974, 77)
    
    elif name == "cabeloJoyHoenn":
        corPadrao1 = (248, 160, 176)
        corPadrao2 = (246, 159, 175)
        corPadrao3 = (244, 157, 173)
        if pixel == (0,0):
            pixel = (985, 94)
    
    elif name == "fimConversa":
        corPadrao1 = (25, 25, 25)
        corPadrao2 = (25, 25, 25)
        corPadrao3 = (25, 25, 25)
        pixel = (1363, 200)
    
    elif name == "balaoChat":
        corPadrao1 = (255, 255, 255)
        corPadrao2 = (253, 253, 253)
        corPadrao3 = (251, 251, 251)
        pixel = (1363, 200)

    elif name == "cabeloMercador":
        corPadrao1 = (119, 111, 63)
        corPadrao2 = (120, 112, 64)
        corPadrao3 = (118, 110, 63)
        pixel = (832, 190)

    elif name == "portoHoenn":
        corPadrao1 = (167, 63, 103)
        corPadrao2 = (168, 64, 104)
        corPadrao3 = (165, 63, 102)
        pixel = (1298, 72)

    elif name == "Landed a pokemon!":
        corPadrao1 = (85, 85, 85)
        corPadrao2 = (86, 86, 86)
        corPadrao3 = (86, 86, 86)
        pixel = (780, 160)
        tentativas = 1
        espera = 0.0

    elif name == "Not even a nibble...":
        corPadrao1 = (33, 33, 33) 
        corPadrao2 = (34, 34, 34)
        corPadrao3 = (34, 34, 34)
        pixel = (780, 160)
        tentativas = 1
        espera = 0.5
    
    elif name == "Vida":
        corPadrao1 = (162, 77, 77)
        corPadrao2 = (164, 77, 77)
        corPadrao3 = (165, 78, 78)
        if pixel == (0,0):
            pixel = (362, 182)
    
    elif name == "NomePokemon":
        corPadrao1 = (251, 251, 251)
        corPadrao2 = (253, 253, 253)
        corPadrao3 = (255, 255, 255)
        pixel = (325, 182)

    elif name == "hordaApareceu":
        corPadrao1 = (251, 251, 251)
        corPadrao2 = (253, 253, 253)
        corPadrao3 = (255, 255, 255)
        pixel = (598, 172)

    elif name == "Lutar":
        corPadrao1 = (251, 251, 251)
        corPadrao2 = (253, 253, 253)
        corPadrao3 = (255, 255, 255)
        pixel = (375, 690)

    elif name == "Pokebola":
        corPadrao1 = (248, 144, 56)
        corPadrao2 = (246, 143, 56)
        corPadrao3 = (244, 142, 55)
        pixel = (627, 714)
    
    elif name == "GreatBall":
        corPadrao1 = (56, 143, 246)
        corPadrao2 = (55, 142, 244)
        corPadrao3 = (56, 144, 248)
        pixel = (627, 714)
    
    elif name == "UltraBall":   
        corPadrao1 = (111, 127, 143)
        corPadrao2 = (110, 126, 142)
        corPadrao3 = (112, 128, 144)
        pixel = (627, 714)
    
    elif name == "MasterBall":
        corPadrao1 = (173, 55, 236)
        corPadrao2 = (175, 56, 238)
        corPadrao3 = (176, 56, 240)
        pixel = (627, 714)

    elif name == "AbaDeIV":
        corPadrao1 = (251, 251, 251)
        corPadrao2 = (253, 253, 253)
        corPadrao3 = (255, 255, 255)
        # Usa o pixel da chamada da funcao, pois eh relativo
    
    elif name == "IV31":
        corPadrao1 = (101, 253, 101) 
        corPadrao2 = (100, 251, 100)
        corPadrao3 = (102, 255, 102)
        espera = 0.0
        tentativas = 1
        # Usa o pixel da chamada da funcao, pois eh relativo

    elif name == "Sim":
        corPadrao1 = (84, 91, 97) 
        corPadrao2 = (83, 90, 96)
        corPadrao3 = (83, 90, 95)
        pixel = (988, 757)

    else:
        return PIXEL_NAO_CADASTRADO   # Nome do Pixel nao definido na funcao CheckPixel

    if pixel == (0, 0):
        return FALTANDO_ARGUMENTO_POSICAO_PIXEL
    
    
    limite = 0
    while limite <= tentativas:
        im = pyautogui.screenshot()
        cor = im.getpixel(pixel) 
        print("Cor:", cor)
        print("Limite =", limite)
        if cor == corPadrao1 or cor == corPadrao2 or cor == corPadrao3:
            print ("Pixel \"" + name + "\" encontrado")
            return PIXEL_ENCONTRADO
        
        limite += 1
        time.sleep(espera)

    print ("Pixel \"" + name + "\" NÃO encontrado")
    return PIXEL_NAO_ENCONTRADO

def ChecandoQntdPokebolas(p_B):
    '''
    Retorna a quantidade de pokebolas do jogador. Só são considerados packs de 99.

    Argumentos: p_B -> posicão do botão B do teclado virtual

    Retornos:   BOLSA_NAO_ABRIU
                ABA_NAO_ABRIU
                qntd de pokebolas
                None (nenhuma pokebola)
    '''
    # Abre a bolsa
    ClickTecladoVirtual(p_B)

    # Procura onde esta a aba da pokebola
    posicaoBagPokebola = CentroDaImagem(PosicaoEDimensaoDaImagem("BagOpcaoPokebola1.png", "BagOpcaoPokebola2.png",\
    "BagOpcaoPokebola3.png", tentativas=3))
    if posicaoBagPokebola == IMG_NAO_ENCONTRADA:
        print ("Nao abriu a bolsa. Personagem provavelmente esta numa acao diferente")
        return BOLSA_NAO_ABRIU
    
    # Clica na aba
    pyautogui.moveTo(posicaoBagPokebola)
    ClickTecladoVirtual(pyautogui.position(), modo="instantaneo")
    
    # Verifica se a aba abriu
    if not CheckPixel("AbaBagPokebola", pixel=(posicaoBagPokebola[x] - 108, posicaoBagPokebola[y] + 31)):
        print ("Nao abriu a aba de pokebola. Personagem provavelmente esta numa acao diferente")
        return ABA_NAO_ABRIU
    
    # Verifica quantas pokebolas tem e retorna esse numero
    
    imagens = ("Bloco99Pokebola1.png", "Bloco99Pokebola2.png", "Bloco99Pokebola3.png")
    for imagem in imagens:
        lista99Pokebolas = list(pyautogui.locateAllOnScreen(IMAGESDIR + imagem))
        qntdPackPokebola = len(lista99Pokebolas)
        
        if qntdPackPokebola > 0:
            print ("Lista =", lista99Pokebolas)
            pokebolas = 99*qntdPackPokebola
            # Fecha a bolsa
            ClickTecladoVirtual(p_B)
            return pokebolas
    
    pokebolas = 0
    # Fecha a bolsa
    ClickTecladoVirtual(p_B)        
    return pokebolas

def RegiaoAtual(p_F2):
    '''
    Retorna a região atual do personagem.

    Argumentos: p_F2 -> Tupla -> posição do botão F2 no teclado virtual

    Retornos:   Regiao (string)
                REGIAO_NAO_CADASTRADA
    '''
    
    ClickTecladoVirtual(p_F2)

    if ImagemEncontrada("RegiaoKanto1.png", "RegiaoKanto2.png", "RegiaoKanto3.png", tentativas=2):
        regiao = "Kanto"

    elif ImagemEncontrada("RegiaoHoenn1.png", "RegiaoHoenn2.png", "RegiaoHoenn3.png", tentativas=1):
        regiao = "Hoenn"

    elif ImagemEncontrada("RegiaoUnova1.png", "RegiaoUnova2.png", "RegiaoUnova3.png", tentativas=1):
        regiao = "Unova"

    else:
        return REGIAO_NAO_CADASTRADA

    time.sleep(0.3)
    return regiao

def Fly(p_F2, regiao="", cidade=""):
    '''
    Realiza o Fly para uma determinada cidade.

    Argumentos: p_F2 -> tupla -> posicão em pixel do botão F2 do teclado virtual
                regiao -> string -> regiao da cidade
                cidade -> string -> cidade desejada

    Retornos:   CIDADE_NAO_ENCONTRADA
                CIDADE_NAO_CADASTRADA
                REGIAO_NAO_CADASTRADA
                OK
    '''

    if cidade == "":
        print ("Faltando o argumento \"cidade\" na função \"Fly\".")
        return FALTANDO_ARGUMENTOS

    # Se o mapa já não tiver aberto, abre ele.
    if not ImagemEncontrada("TownMap1.png", "TownMap2.png", "TownMap3.png", tentativas=1):
        ClickTecladoVirtual(p_F2)
    
    posicaoCidade = PosicaoCidadeFly(cidade, regiao)
    if posicaoCidade == CIDADE_NAO_ENCONTRADA or posicaoCidade == CIDADE_NAO_CADASTRADA: #Nao foi encontrado o BotaoMapa
        return posicaoCidade

    pyautogui.moveTo(posicaoCidade, duration=0.3)
    
    if regiao == "Unova":
        # Clica mais uma vez.
        ClickTecladoVirtual(pyautogui.position())
    
    ClickTecladoVirtual(pyautogui.position())
    time.sleep(10.0)
    
    return OK

def EstenderRepel(p_Teclas, escolha=""):
    '''
    Estende o uso do repel, ou não.

    Argumentos: p_Teclas -> tupla -> posições de cada tecla do teclado virtual
                escolha -> string -> "Y" ou "N" 

    Retornos:
                OK
                ERRO_REPEL
                ESCOLHA_INVALIDA
    '''
    
    p_Down = p_Teclas[4]
    p_Z = p_Teclas[5]
    
    if not CheckPixel("Sim"):
        print ("O repel não terminou nesse momento, como deveria.")
        return ERRO_REPEL

    if escolha == "Y":
        ClickTecladoVirtual(p_Z)
        
    elif escolha == "N":
        ClickTecladoVirtual(p_Down)
        ClickTecladoVirtual(p_Z)
    else:
        return ESCOLHA_INVALIDA

    time.sleep(0.2)

    return OK

def TrocarRegiao(p_Teclas, regiaoOrigem="", regiaoDestino="", repel="N"):
    '''
    Troca de região para a região de destino.


    Argumentos: regiaoOrigem -> string -> regiao que o personagem está no momento
                regiaoDestino -> string -> regiao de destino
                p_Tecla -> tupla -> posicao de todas as teclas do teclado virtual
                repel -> string -> indica se o personagem está usando repel ou não.

        OBS:
            Valores válidos para "repel": "Y" para "Sim", qualquer outra coisa para "Não".

    Retornos:   OK
                MESMA_REGIAO
                REGIAO_DESTINO_INVALIDA
                ERRO_TROCAR_REGIAO
                REGIAO_ORIGEM_INVALIDA
                ERRO_REPEL
    '''

    p_Left = p_Teclas[1]          
    p_Up = p_Teclas[2]
    p_Right = p_Teclas[3]
    p_Down = p_Teclas[4]
    p_Z = p_Teclas[5]
    p_F2 = p_Teclas[9]


    if regiaoOrigem == regiaoDestino:
        return MESMA_REGIAO

    #### KANTO -> REGIÃO DESTINO ####
    if regiaoOrigem == "Kanto":
        
        # Voando para Vermilion.
        erro = Fly(p_F2, regiao="Kanto", cidade="Vermilion")
        if erro != OK:
            return erro

        # Caminhando até o porto.
        ClickTecladoVirtual(p_Right, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Right, clicks=14)
        ClickTecladoVirtual(p_Down, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Down, clicks=6)
        ClickTecladoVirtual(p_Left, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Left, clicks=3)
        ClickTecladoVirtual(p_Down, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Down, clicks=4)
        ClickTecladoVirtual(p_Right, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Right, clicks=8)
        ClickTecladoVirtual(p_Down, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Down, clicks=9)
        ClickTecladoVirtual(p_Left, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Left, clicks=2)
        ClickTecladoVirtual(p_Down, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Down, clicks=3)

        # Conversando com o cara do porto.
        erro = ContinuarConversa(p_Z)
        if erro != OK:
            return erro
            
        if not ImagemEncontrada("SelecionarRegiao1.png", "SelecionarRegiao2.png", "SelecionarRegiao3.png"):
            return ERRO_TROCAR_REGIAO
        
        if regiaoDestino == "Hoenn":
            ClickTecladoVirtual(p_Z)
        
        elif regiaoDestino == "Sinnoh":
            ClickTecladoVirtual(p_Down)
            time.sleep(0.2)
            ClickTecladoVirtual(p_Z)

        elif regiaoDestino == "Unova":
            ClickTecladoVirtual(p_Down, clicks=2)
            time.sleep(0.2)
            ClickTecladoVirtual(p_Z)
        else:
            return REGIAO_DESTINO_INVALIDA

        # Termina a conversa.
        erro = ContinuarConversa(p_Z)
        if erro != OK:
            return erro

    #### HOENN -> REGIÃO DESTINO ####
    elif regiaoOrigem == "Hoenn":
        
        # Voando para Slateport.
        erro = Fly(p_F2, regiao="Hoenn", cidade="Slateport")
        if erro != OK:
            return erro

        # Caminhando até o porto.
        ClickTecladoVirtual(p_Left, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Left, clicks=7)
        ClickTecladoVirtual(p_Up, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Up, clicks=4)
        ClickTecladoVirtual(p_Right, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Right)

        if repel == "Y":
            # Verifica se o repel acabou e veio a pergunta de se quer estender com mais um.
            erro = EstenderRepel(p_Teclas, escolha="N")
            if erro != OK:
                print ("Erro Função EstenderRepel.")
                return erro

        ClickTecladoVirtual(p_Right, clicks=15)
        ClickTecladoVirtual(p_Up, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Up)
        
        # Entra no Porto.
        ClickTecladoVirtual(p_Up)
        
        # Verifica se entrou.
        if not CheckPixel("portoHoenn"):
            return ERRO_TROCAR_REGIAO
        
        # Anda até a mulher.
        ClickTecladoVirtual(p_Up, clicks=3)
        ClickTecladoVirtual(p_Right, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Right, clicks=4)
        ClickTecladoVirtual(p_Up)
        time.sleep(0.1)

        # Inicia a conversa.
        ClickTecladoVirtual(p_Z)
        
        # Conversando com a mulher do porto.
        erro = ContinuarConversa(p_Z)
        if erro != OK:
            return erro
        
        if not ImagemEncontrada("SelecionarRegiao1.png", "SelecionarRegiao2.png", "SelecionarRegiao3.png"):
            return ERRO_TROCAR_REGIAO
        
        if regiaoDestino == "Kanto":
            ClickTecladoVirtual(p_Z)
        
        elif regiaoDestino == "Sinnoh":
            ClickTecladoVirtual(p_Down)
            time.sleep(0.2)
            ClickTecladoVirtual(p_Z)

        elif regiaoDestino == "Unova":
            ClickTecladoVirtual(p_Down, clicks=2)
            time.sleep(0.2)
            ClickTecladoVirtual(p_Z)
        else:
            return REGIAO_DESTINO_INVALIDA

        # Termina a conversa.
        erro = ContinuarConversa(p_Z)
        if erro != OK:
            return erro

 
    #### UNOVA -> REGIÃO DESTINO ####
    elif regiaoOrigem == "Unova":
        # Voando para Castelia.
        erro = Fly(p_F2, regiao="Unova", cidade="Castelia")
        if erro != OK:
            return erro
        ClickTecladoVirtual(p_Down)
        ClickTecladoVirtual(p_Left, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Left, clicks=44)
        ClickTecladoVirtual(p_Down, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Down, clicks=6)
        time.sleep(7)
        ClickTecladoVirtual(p_Left, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Left, clicks=3)
        ClickTecladoVirtual(p_Down, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Down, clicks=5)
        ClickTecladoVirtual(p_Left, clicks=2, modo="instantaneo")
        time.sleep(0.1)
        
        # Inicia a conversa.
        ClickTecladoVirtual(p_Z)

        # Conversando com a mulher do porto.
        erro = ContinuarConversa(p_Z)
        if erro != OK:
            return erro
            
        if not ImagemEncontrada("SelecionarRegiao1.png", "SelecionarRegiao2.png", "SelecionarRegiao3.png"):
            return ERRO_TROCAR_REGIAO
        
        if regiaoDestino == "Kanto":
            ClickTecladoVirtual(p_Z)
        
        elif regiaoDestino == "Hoenn":
            ClickTecladoVirtual(p_Down)
            time.sleep(0.2)
            ClickTecladoVirtual(p_Z)
        
        elif regiaoDestino == "Sinnoh":
            ClickTecladoVirtual(p_Down, clicks=2)
            time.sleep(0.2)
            ClickTecladoVirtual(p_Z)

        else:
            return REGIAO_DESTINO_INVALIDA

        # Termina a conversa.
        erro = ContinuarConversa(p_Z)
        if erro != OK:
            return erro
            
    else:
        return REGIAO_ORIGEM_INVALIDA
    
    # Tempo de espera até chegar na região.
    time.sleep(7)

    return OK
        
def ContinuarConversa(p_Z, clicks=1):
    '''
    Continua a conversa apertando Z. Essa função NECESSITA de que o fim da mensagem
    seja demarcado por um símbolo de seta para baixo. Se não tiver a seta na mensagem
    essa função NÃO VAI FUNCIONAR.
    
    Argumentos: p_Z -> tupla -> posição do botão Z do teclado virtual
                clicks -> inteiro positivo -> número de cliques em sequência
    
    Retornos:   OK
                SETA_NAO_ENCONTRADA
    '''
    
    while clicks > 0:

        if not CheckPixel("fimConversa", espera=0.1):
            print ("Erro função ContinuarConversa. A seta não foi encontrada.")
            return SETA_NAO_ENCONTRADA

        time.sleep(0.1)

        ClickTecladoVirtual(p_Z, modo="instantaneo")
        clicks -=1
    
    return OK

def EntrarCP(p_Up, regiao="Kanto"):
    '''
    Entra no centro pokemon e se posiciona em frente a enfermeira Joy.

    Argumentos: p_Up -> tupla -> posicao em pixel da seta para cima
                p_Z -> tupla -> posicao em pixel do botao Z
                regiao -> string -> região do CP

    Retornos:   OK
                NAO_ENTROU_NO_CP
                PIXEL_NAO_CADASTRADO
                
    '''
    ClickTecladoVirtual(p_Up, clicks=2, modo="instantaneo") #Entrando no CP 
    
    if regiao == "Kanto":
        pixelReferencia = "cabeloJoyKanto"
    
    elif regiao == "Hoenn":
        pixelReferencia = "cabeloJoyHoenn"

    else:
        return PIXEL_NAO_CADASTRADO
    
    #Checando se o personagem esta dentro do CP como programado
    if not CheckPixel(pixelReferencia): 
        print ("Personagem não entrou no CP")
        return NAO_ENTROU_NO_CP
    time.sleep(0.2)
    
    # Andando em direção a ela
    ClickTecladoVirtual(p_Up, clicks=4, modo="andar") #Andando ateh a Joy 
    time.sleep(0.2)
    
    return OK

def UsarCPESair(p_Z, p_Down, regiao="Kanto"):
    '''
    Entra no centro pokemon e se posiciona em frente a enfermeira Joy.

    Argumentos: 
                p_Z -> tupla -> posicao em pixel do botao Z
                p_Down -> tupla -> posicao em pixel da seta para baixo
                regiao -> string -> região do CP

    Retornos:   OK
                PIXEL_NAO_CADASTRADO
                ERRO_CP
    '''
    
    # Iniciando a conversa.
    ClickTecladoVirtual(p_Z) 
    
    # Continuando a conversa.
    erro = ContinuarConversa(p_Z)
    if erro != OK:
        return erro

    if regiao == "Hoenn":
        # Continuando a conversa.
        erro = ContinuarConversa(p_Z)
        if erro != OK:
            return erro

    # Selecionando Yes.
    if not CheckPixel("Sim"):
        print ("Não encontrou o botão \"Sim\" para recuperar vida.")
        return ERRO_CP

    ClickTecladoVirtual(p_Z, modo="instantaneo") 

    # Terminando a conversa.
    erro = ContinuarConversa(p_Z, clicks=4)
    if erro != OK:
        return erro

    # Andando até a porta do CP
    ClickTecladoVirtual(p_Down, clicks=2, modo="instantaneo")  
    ClickTecladoVirtual(p_Down, clicks=3, modo="andar") 
    
    # Verificando regiao e se está tudo OK
    if regiao == "Kanto":
        pixelReferencia = "cabeloJoyKanto"
    
    elif regiao == "Hoenn":
        pixelReferencia = "cabeloJoyHoenn"

    else:
        return PIXEL_NAO_CADASTRADO

    if not CheckPixel(pixelReferencia):
        print ("Personagem entrou no CP mas agora nao estah na posicao de saida como deveria")
        return ERRO_CP

    #Sai do CP    
    ClickTecladoVirtual(p_Down, clicks=1, modo="andar")  
    time.sleep(2.0)

    return OK

def EntrarUsarESairCP(p_Up, p_Z, p_Down, regiao="Kanto"):
    '''
    Entra, recupera vida no centro pokemon e sai.

    Argumentos: p_Up -> tupla -> posicao em pixel da seta para cima
                p_Z -> tupla -> posicao em pixel do botao Z
                p_Down -> tupla -> posicao em pixel da seta para baixo
                regiao -> string -> região do CP

    Retornos:   OK
                NAO_ENTROU_NO_CP
                ERRO_CP
                SETA_NAO_ENCONTRADA
                PIXEL_NAO_CADASTRADO           
    '''
    
    erro = EntrarCP(p_Up, regiao)
    if erro != OK:
        print ("Erro entrando no CP.")
        return erro
    
    erro = UsarCPESair(p_Z, p_Down, regiao)
    if erro != OK:
        print ("Erro usando o CP.")
        return erro
    
    return OK

def CaminharAtePokeMarket(cidade, p_Left, p_Up, p_Right, p_Down):
    '''
    Caminha até o Poke Market. 
    Jogador precisa estar na porta do CP do lado de fora, e virado pra fora.

    Argumentos: cidade -> string -> cidade que o personagem se encontra
                p_Tecla -> tupla -> Posicao da tecla especificada do teclado virtual

    Retornos:   CIDADE_NAO_CADASTRADA
                OK
    '''

    if cidade == "Vermilion":
        ClickTecladoVirtual(p_Right, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Right, clicks=14)
        ClickTecladoVirtual(p_Down, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Down, clicks=6)
        ClickTecladoVirtual(p_Left, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Left, clicks=3)
        ClickTecladoVirtual(p_Down, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Down, clicks=3)
        ClickTecladoVirtual(p_Right, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Right, clicks=2)
        # Entra no Poke-Market.
        ClickTecladoVirtual(p_Up, clicks=2, modo="instantaneo")

    else:
        print ("Erro função CaminharProMarket: Cidade não cadastrada")
        return CIDADE_NAO_CADASTRADA

    return OK

def Comprar(item, p_Left, p_Up, p_Right, p_Down, p_Z, p_ESC, qntdPack=1, regiao="Kanto"):
    '''
    Entra no poke market e compra o item de acordo com a quantidade de packs desejada.

    Argumentos: item -> string -> item que vai comprar
                p_Tecla -> tupla -> Posicao da tecla especificada do teclado virtual
                qntdPack -> unsigned int -> qntd de Packs de 99 desejada
                regiao -> string -> regiao que reside o mercado

    Retornos:   OK
                ERRO_COMPRAR
                QNTD_PACK_INVALIDA
                CABELO_NAO_CADASTRADO
                REGIAO_NAO_CADASTRADA
                ITEM_NAO_CADASTRADO
    '''
    
    if qntdPack <= 0:
        print ("Qntd de pack deve ser > 0")
        return QNTD_PACK_INVALIDA

    if regiao == "Kanto":

        # Indica o momento que entrar no PM 
        if not CheckPixel("cabeloMercador"):
            return CABELO_NAO_CADASTRADO

        # Dentro do mercado

        # Andando até o vendedor
        ClickTecladoVirtual(p_Up, clicks=4)
        ClickTecladoVirtual(p_Left)
        time.sleep(0.2)
        
        # Iniciando a conversa com ele.
        ClickTecladoVirtual(p_Z, modo="instantaneo")
        
        # Continua até aparecer os itens.
        erro = ContinuarConversa(p_Z)
        if erro != OK:
            return erro

        # Verificando qual item a pessoa quer comprar
        if item != "Pokebola":
            return ITEM_NAO_CADASTRADO

        #Apertando Quantia Max
        posicaoQuantiaMax = CentroDaImagem(PosicaoEDimensaoDaImagem("QuantiaMax1.png", "QuantiaMax2.png", "QuantiaMax3.png", 
                                        tentativas=5, espera=0.5))
        
        if posicaoQuantiaMax == IMG_NAO_ENCONTRADA: 
            return ERRO_COMPRAR 
        
        pyautogui.moveTo(posicaoQuantiaMax)
        ClickTecladoVirtual(posicaoQuantiaMax, modo="instantaneo")

        #Apertando pra comprar
        posicaoComprar = CentroDaImagem(PosicaoEDimensaoDaImagem("Comprar1.png", "Comprar2.png", "Comprar3.png", 
                                    tentativas=5, espera=0.5))
        
        if posicaoComprar == IMG_NAO_ENCONTRADA: 
            return ERRO_COMPRAR

        pyautogui.moveTo(posicaoComprar)
        
        #Compra a qntd packs
        for count in range (qntdPack):
            #Clica em comprar
            ClickTecladoVirtual(posicaoComprar, modo="instantaneo")
            time.sleep(2.0)
            
            #Clica em Quantidade Max
            pyautogui.moveTo(posicaoQuantiaMax)
            ClickTecladoVirtual(posicaoQuantiaMax, modo="instantaneo")
            time.sleep(2.0)

            #Move pro botão comprar
            pyautogui.moveTo(posicaoComprar)

        # Termina a compra
        ClickTecladoVirtual(p_ESC)
        time.sleep(0.2)
        
        # Termina a conversa.
        erro = ContinuarConversa(p_Z)
        if erro != OK:
            return erro

        #Anda até a porta
        ClickTecladoVirtual(p_Down, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Down, clicks=3)
        if not CheckPixel("cabeloMercador"):
            return ERRO_COMPRAR

        # Sai do mercado
        ClickTecladoVirtual(p_Down)
        time.sleep(2.5)

    #end if regiao == "Kanto":
    else:
        return REGIAO_NAO_CADASTRADA

    return OK

def ReconhecerPokemon(pokemon):
    '''
    Começado a batalha, verifica qual é o pokemon encontrado

    Argumentos: pokemon -> string -> deve ser um dos cadastrados
    
    Retornos:   NOME_NAO_APARECEU
                ERRO_RECONHECER_POKE
                MAGIKARP_NAO_ENCONTRADO
                MAGIKARP_ENCONTRADO
                MAGIKARP_SHINY
                TENTACOOL_NAO_ENCONTRADO
                TENTACOOL_ENCONTRADO
                TENTACOOL_SHINY
                POKEMON_NAO_REGISTRADO

    '''
    
    # Verifica se o nome do pokemon já apareceu 
    if not CheckPixel("NomeDoPokemon"):
        print ("Nao apareceu o nome do pokemon. Provavelmente estah numa acao diferente")
        return NOME_NAO_APARECEU 
    
    if pokemon == "Magikarp":
        
        # USAR ESSE PEDACO DE CODIGO QND TIVER ANALISANDO O POKEMON QUE VC QUER CAPTURAR,
        # visto que ele será analisado primeiro.
        pyautogui.moveTo(370, 166, duration=0.3)
        

        posicaoMagikarp = CentroDaImagem(PosicaoEDimensaoDaImagem("MagikarpChuva1.png", "Magikarp2.png", "MagikarpChuva2.png", 
        "MagikarpChuva2Nivel10.png", tentativas=2, espera=0.5))
        print ("Posicao Magikarp = ", posicaoMagikarp) 
        ''' 
        #1 - Level10: (396, 139) , (396, 138) , 
        #2 - <level10: (389, 139) , #3 (389, 138) , #4 (390, 138)
        
        '''
        if posicaoMagikarp == IMG_NAO_ENCONTRADA: # Imagem nao foi reconhecida. Nao eh magikarp ou nao foi reconhecido. Pode ser um shiny ou n.
            return MAGIKARP_NAO_ENCONTRADO 
        
        else: # Magikarp encontrado. Falta saber se eh shiny ou n. 
            if posicaoMagikarp == (396, 139) or posicaoMagikarp == (396, 138) or posicaoMagikarp == (389, 139) or \
                posicaoMagikarp == (389, 138) or posicaoMagikarp == (390, 138) or posicaoMagikarp == (383, 139) or\
                posicaoMagikarp == (383, 138) or posicaoMagikarp == (391, 138) or posicaoMagikarp == (391, 139):
                
                #Magikarp encontrado mas n eh shiny
                
                #Verificar se ja carregou o botao "Lutar" da batalha
                if not CheckPixel("Lutar", tentativas=150):
                    print ("Nao apareceu o botao \"Lutar\". O programa provavelmente estah numa acao diferente")
                    return ERRO_RECONHECER_POKE   #-2
                
                return MAGIKARP_ENCONTRADO
            
            else: # Eh Magikarp mas a posicao nao eh esperada. Pode ser um shiny ou n.
                return MAGIKARP_SHINY #-1

    elif pokemon == "Tentacool":
        posicaoTentacool = CentroDaImagem(PosicaoEDimensaoDaImagem("TentacoolChuva1.png", "TentacoolChuva2.png",
        "TentacoolChuva3.png", tentativas=3))
        print ("Posicao Tentacool = ", posicaoTentacool) 
        '''
        # 1 - (392, 168) 
        # 2 - (393, 137) 
        # 3 - (392, 138) 
        # 4 - (400, 138)
        # 5 - (401, 137)
        '''
        if posicaoTentacool == IMG_NAO_ENCONTRADA: # Imagem nao foi reconhecida. Nao eh tentacool ou a imagem nao foi reconhecida. 
            return TENTACOOL_NAO_ENCONTRADO #1                               # Pode ser um shiny ou n.
            
        else:    
            if posicaoTentacool == (392, 168) or posicaoTentacool == (393, 137) or posicaoTentacool == (392, 138) or\
                posicaoTentacool == (400, 138) or posicaoTentacool == (401, 137) or posicaoTentacool == (387, 138) or\
                posicaoTentacool == (394, 138) or posicaoTentacool == (388, 137) or posicaoTentacool == (395, 137):
                
                #Tentacool encontrado mas n eh shiny
                
                #Verifica se ja carregou o botao "Lutar" da batalha e espera um determinado tempo para ver se aparece
                if not CheckPixel("Lutar", tentativas=150):
                    print ("Nao apareceu o botao \"Lutar\". O programa provavelmente estah numa acao diferente")
                    return ERRO_RECONHECER_POKE
                
                return TENTACOOL_ENCONTRADO
            
            else: # Eh Tentacool mas a posicao nao eh esperada. Pode ser um shiny ou n.
                return TENTACOOL_SHINY
    else:
        print("Pokemon ainda nao implementado")
        return POKEMON_NAO_REGISTRADO

def Pescar(p_F7, p_Z): 
    '''
    Executa a função de pescar até achar algum pokemon, ou acontecer algum erro.

    Argumentos: p_F7 -> tupla -> posição do botão F7
                p_Z -> tupla -> posição do botão Z

    Retornos:   ERRO_PESCAR
                OK
    '''
    repetir = True
    while repetir == True: 
        encontrouPokemon = False
        naoEncontrouPokemon = False
        tentativas = 0
        while encontrouPokemon == False and naoEncontrouPokemon == False and tentativas != 2:
            '''
            Repete o while seguinte para tentar novamente ao apertar pescar de novo
            '''
            pyautogui.click(p_F7[0], p_F7[1]) # Aperta para pescar
            time.sleep(3.6)
            limite = 0
            while encontrouPokemon == False and naoEncontrouPokemon == False and limite != 3:
                '''
                Analisa se deu "Not even a nibble..."(naoEncontrouPokemon) ou
                se deu "Landed a Pokemon!"(encontrouPokemon).
                Se nao deu nenhum dos dois quer dizer que a acao pescar nao foi executada ou 
                o pixel verificador nao apareceu ainda.
                '''
             
                encontrouPokemon = CheckPixel("Landed a pokemon!")
                if encontrouPokemon:
                    ClickTecladoVirtual(p_Z) #Fecha a mensagem "Landed a Pokemon!" 
                    repetir = False # Encontrou algum pokemon. Sai da função.
                    
                else:
                    naoEncontrouPokemon = CheckPixel("Not even a nibble...")
                    if naoEncontrouPokemon:    
                        ClickTecladoVirtual(p_Z) #Fecha a mensagem "Not even a nibble..." 
                        # Volta ao primeiro while e repete a acao de pescar ateh vir a mensagem "Landed a Pokemon!"                   
                    else:
                        #Significa que nenhuma mensagem apareceu. Vai verificar de novo.
                        limite += 1
            
            tentativas += 1 # Se nenhuma mensagem foi encontrada depois de ter ultrapassado o limite, 
                            # tentará pescar novamente para ver se esse é o problema, e verificará novamente.
        
        if encontrouPokemon == False and naoEncontrouPokemon == False:  
        # Se nenhuma mensagem apareceu mesmo apos tantas tentativas.
            return ERRO_PESCAR     
    
    print ("Pokemon encontrado")
    #Pausa ateh comecar a batalha
    time.sleep(5.0)
    return OK

def FalseSwipe(p_Z, pp):
    '''
    Usa o ataque False swipe até a vida do pokemon ficar mínima

    Argumentos: p_Z -> tupla -> posicao em pixel da tecla Z  
                pp -> inteiro positivo -> quantidade atual de PP
    
    Retornos:   VALOR_INVALIDO_PP
                ERRO_FALSE_SWIPE
                qntd de pp

    '''
    if pp < 0:
        return VALOR_INVALIDO_PP
    pouca = False
    while pouca == False and pp != 0:
        #Verificar se ja carregou o botao "Lutar" da batalha
        if not CheckPixel("Lutar"):
            print ("ERRO_FALSE_SWIPE")
            return ERRO_FALSE_SWIPE # -2
        
        # Manda o False swipe 
        ClickTecladoVirtual(p_Z, clicks=2)
        time.sleep(3.2)
        pouca = CheckPixel("Vida")
        pp -= 1

    # TODO: Sugestão: Pode implementar para caso acabe o pp e nao ter deixado a vida pouca, retornar algum outro valor para a main,
    # e a main fazer algo especifico em relacao a isso.
    return pp      

def LancarPokebola(p_Teclas, qntdPokebolas):
    '''
    Lança pokebola, ou lança a bola que tiver (sem ser master ball) se as pokebolas
    acabaram durante a batalha.

    Argumentos: p_Teclas -> lista de posicao das teclas do teclado virtual.
                qntdPokebolas -> inteiro positivo -> qntd atual de pokebolas

    Retornos:   
                OK
                ERRO_LANCAR_POKEBOLA
                SO_TEM_MASTER_BALL
                LANCOU_BOLA_ENCONTRADA
                
    '''
    p_Right = p_Teclas[3]
    p_Down = p_Teclas[4]
    p_Z = p_Teclas[5]
    p_Up = p_Teclas[2]

    # Verifica se já apareceu o botao "Lutar", indicando que pode lancar a pokebola
    if not CheckPixel("Lutar"):
        return ERRO_LANCAR_POKEBOLA   
    
    ClickTecladoVirtual(p_Right)                
    ClickTecladoVirtual(p_Z)
    ClickTecladoVirtual(p_Right, clicks=2)


    ################## SE ACABOU AS POKEBOLAS ENQUANTO LUTAVA ###############

    if qntdPokebolas <= 0:
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
                ClickTecladoVirtual(p_Down)
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
                    ClickTecladoVirtual(p_Up)
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
                        ClickTecladoVirtual(p_Down)
                        if CheckPixel("MasterBall"):
                            # Só tem master ball, dar Run.
                            return SO_TEM_MASTER_BALL

        # Lanca a bola encontrada (pokebola, great ball, ultra ball, ou outra)
        ClickTecladoVirtual(p_Z)
        
        return LANCOU_BOLA_ENCONTRADA
    # End if qntdPokebolas <= 0:   

    if not CheckPixel("Pokebola"):
        print("Pokebola nao estah selecionada como planejado.")
        return ERRO_LANCAR_POKEBOLA
    
    # Lança a pokebola
    ClickTecladoVirtual(p_Z)
    
    return OK

def VerificarPokemonCapturado(manter_pokemon=False, tentativas=7):
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
    ClickTecladoVirtual(posicaoSimboloIV, modo="instantaneo")

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

def GuardarOuRelease(status, p_ESC, isShiny=False):
    '''
    Se tiver algum IV 31, guarda o pokemon capturado.
    Se não tiver, joga ele fora.

    Argumentos: status -> deve ter valor de: COM_IV31 OU SEM_IV31. -> informação se tem IV 31 ou não. 
                p_ESC -> tupla -> posicão do botão ESC do teclado virtual

    Retornos:   POKEMON_GUARDADO
                POKEMON_RELEASED
                STATUS_INVALIDO 

    '''

    if status == COM_IV31 or isShiny:
        ClickTecladoVirtual(p_ESC)# Fecha a aba de status
        
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
        ClickTecladoVirtual(pyautogui.position(), modo="instantaneo")
        
        # Movendo para o botao release
        pyautogui.moveRel(-90, 153)
        ClickTecladoVirtual(pyautogui.position(), modo="instantaneo")
        
        # Clicando em confirmar
        pyautogui.moveTo((961, 522))
        ClickTecladoVirtual((961, 522), modo="instantaneo")
        #Então, volta pro while ateh o PP do false swipe acabar
        return POKEMON_RELEASED

    else:
        return STATUS_INVALIDO

def Virar(sentido, p_Teclas):
    '''
    Vira e anda um passo pro sentido indicado.

    Argumentos: 
                sentido -> string -> para onde o personagem vai virar
                p_Teclas -> tupla -> posição de cada tecla do teclado

    OBS: 
        Valores válidos para "sentido": "esquerda", "direita", "cima" e "baixo"

    Retornos:
                OK
                SENTIDO_INVALIDO
    '''

    #Posicoes de cada tecla
    p_Left = p_Teclas[1]          # Recebem (x,y) 
    p_Up = p_Teclas[2]
    p_Right = p_Teclas[3]
    p_Down = p_Teclas[4]
    

    if sentido == "esquerda":
        ClickTecladoVirtual(p_Left, clicks=2, modo="instantaneo")

    elif sentido == "cima":
        ClickTecladoVirtual(p_Up, clicks=2, modo="instantaneo")

    elif sentido == "direita":
        ClickTecladoVirtual(p_Right, clicks=2, modo="instantaneo")

    elif sentido == "baixo":
        ClickTecladoVirtual(p_Down, clicks=2, modo="instantaneo")

    else:
        print ("Sentido inexistente")
        return SENTIDO_INVALIDO


    return OK

##### PLANTAR BERRIES #####

def PlantarSementesPicantes(p_Z):
    '''
    Seleciona as sementes de acordo com a semente inserida, e planta elas.

    Argumentos: p_Z -> tupla -> posição da tecla Z do teclado virtual
                semente -> string -> semente desejada

    Retornos:   OK
                ERRO_PLANTAR_SEMENTES
                SEM_SEMENTE_PICANTE
    ''' 

    if not ImagemEncontrada("PlantarSementes1.png", "PlantarSementes2.png", "PlantarSementes3.png"):
        print ("Aba \"Plantar Sementes\" não abriu.")
        return ERRO_PLANTAR_SEMENTES
    
    # Seleciona o primeiro slot.
    ClickTecladoVirtual(p_Z)

    # Seleciona a semente picante.
    p_picante = CentroDaImagem(PosicaoEDimensaoDaImagem("SementePicante1.png", "SementePicante2.png", "SementePicante3.png", tentativas=2))
    opcao = 1
    if p_picante == IMG_NAO_ENCONTRADA:
        opcao = 2
        p_picante = CentroDaImagem(PosicaoEDimensaoDaImagem("SementePicanteCentena1.png", "SementePicanteCentena2.png", 
                                                        "SementePicanteCentena3.png", tentativas=1))
        if p_picante == IMG_NAO_ENCONTRADA:
            opcao = 3
        
            p_picante = CentroDaImagem(PosicaoEDimensaoDaImagem("SementePicSelecionada1.png", "SementePicSelecionada2.png", 
                                "SementePicSelecionada3.png", tentativas=1))
            if p_picante == IMG_NAO_ENCONTRADA:
                print ("Jogador não tem semente picante, ou aconteceu algum erro.")
                return SEM_SEMENTE_PICANTE

    pyautogui.moveTo(p_picante)
    ClickTecladoVirtual(p_picante)

    # Clica no segundo Slot
    p_Slot1 = CentroDaImagem(PosicaoEDimensaoDaImagem("Slot1.png", "Slot2.png", "Slot3.png"))
    p_Slot2 = (p_Slot1[x] + 95, p_Slot1[y] - 2) 
    pyautogui.moveTo(p_Slot2)
    ClickTecladoVirtual(p_Slot2)

    # Seleciona a semente picante.
    if opcao == 1:
        p_picante = CentroDaImagem(PosicaoEDimensaoDaImagem("SementePicante1.png", "SementePicante2.png", "SementePicante3.png"))
    
    elif opcao == 2:
        p_picante = CentroDaImagem(PosicaoEDimensaoDaImagem("SementePicanteCentena1.png", "SementePicanteCentena2.png", 
                                                        "SementePicanteCentena3.png"))

    elif opcao == 3:
        p_picante = CentroDaImagem(PosicaoEDimensaoDaImagem("SementePicSelecionada1.png", "SementePicSelecionada2.png", 
                                "SementePicSelecionada3.png"))
    
    if p_picante == IMG_NAO_ENCONTRADA:
        print ("Jogador não tem semente picante, ou aconteceu algum erro.")
        return SEM_SEMENTE_PICANTE

    pyautogui.moveTo(p_picante)
    ClickTecladoVirtual(p_picante)

    # Clica no terceiro Slot
    p_Slot3 = (p_Slot2[x] + 95, p_Slot2[y] - 2)
    pyautogui.moveTo(p_Slot3)
    ClickTecladoVirtual(p_Slot3)
    
    # Seleciona a semente picante.
    if opcao == 1:
        p_picante = CentroDaImagem(PosicaoEDimensaoDaImagem("SementePicante1.png", "SementePicante2.png", "SementePicante3.png"))
    
    elif opcao == 2:
        p_picante = CentroDaImagem(PosicaoEDimensaoDaImagem("SementePicanteCentena1.png", "SementePicanteCentena2.png", 
                                                        "SementePicanteCentena3.png"))

    elif opcao == 3:
        p_picante = CentroDaImagem(PosicaoEDimensaoDaImagem("SementePicSelecionada1.png", "SementePicSelecionada2.png", 
                                "SementePicSelecionada3.png"))
    
    if p_picante == IMG_NAO_ENCONTRADA:
        print ("Jogador não tem semente picante, ou aconteceu algum erro.")
        return SEM_SEMENTE_PICANTE

    pyautogui.moveTo(p_picante)
    ClickTecladoVirtual(p_picante)

    # Clicando em "Plantar Sementes".
    if not ImagemEncontrada("CheriBerry1.png", "CheriBerry2.png", "CheriBerry3.png"):
        print ("Após selecionar as sementes, cheri berry não apareceu.")
        return ERRO_PLANTAR_SEMENTES

    p_botaoPlantar = CentroDaImagem(PosicaoEDimensaoDaImagem("BotaoPlantar1.png", "BotaoPlantar2.png", "BotaoPlantar3.png"))
    pyautogui.moveTo(p_botaoPlantar)
    ClickTecladoVirtual(p_botaoPlantar)

    return OK

def CaminharAteSlotBerry(p_Teclas, cidade="", tentativa=1):  
    '''
    Caminha até o primeiro slot de berry de uma das cidades cadastradas.

    Argumentos: 
                p_Teclas -> tupla -> posicao de todas as teclas do teclado virtual.
                cidade -> strings -> cidade do slot.

    Retornos:   
                OK
                CIDADE_NAO_CADASTRADA
                ERRO_CAMINHAR_ATE_SLOT
    '''
    
    #Posicoes de cada tecla
    p_Left = p_Teclas[1]           
    p_Up = p_Teclas[2]
    p_Right = p_Teclas[3]
    p_Down = p_Teclas[4]
    p_Z = p_Teclas[5]
    p_F2 = p_Teclas[9]
    p_F5 = p_Teclas[10]



    # Andando até o primeiro slot.
    if cidade == "Rustboro":
        
        ClickTecladoVirtual(p_Down, clicks=3)
        ClickTecladoVirtual(p_Left, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Left)
        ClickTecladoVirtual(p_Down, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Down, clicks=11)
        ClickTecladoVirtual(p_Right, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Down, clicks=2, modo="instantaneo")
        
        ClickTecladoVirtual(p_Down, clicks=4)
        ClickTecladoVirtual(p_Down)
        print ("Tomando cuidado com o bug...")
        time.sleep(6)
        print ("Continuando...")
        ClickTecladoVirtual(p_Down, clicks=3)

        ClickTecladoVirtual(p_Right, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Right, clicks=8)
        ClickTecladoVirtual(p_Down, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Down, clicks=12)
        ClickTecladoVirtual(p_Right, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Right, clicks=5)
        ClickTecladoVirtual(p_Down, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Down, clicks=5)
        ClickTecladoVirtual(p_Left, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Left, clicks=25)
        time.sleep(0.1)
    
    
    elif cidade == "Fortree":
        
        ClickTecladoVirtual(p_Down)
        ClickTecladoVirtual(p_Right, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Right, clicks=4)
        ClickTecladoVirtual(p_Up, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Up, clicks=3)
        ClickTecladoVirtual(p_Right, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Right, clicks=21)
        ClickTecladoVirtual(p_Down, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Down, clicks=3)
        ClickTecladoVirtual(p_Right, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Right, clicks=7)

        print ("Tomando cuidado com o bug...")
        time.sleep(4)
        print ("Continuando...")
        
        ClickTecladoVirtual(p_Right, clicks=18)
        ClickTecladoVirtual(p_Up, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Up, clicks=2)
        ClickTecladoVirtual(p_Right, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Right, clicks=18)
        ClickTecladoVirtual(p_Down, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Right, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Down, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Down, clicks=3)

        # Usar Super Repel.
        ClickTecladoVirtual(p_F5)
        time.sleep(4)

        ClickTecladoVirtual(p_Left, clicks=2, modo="instantaneo")
        time.sleep(4)
        
        ClickTecladoVirtual(p_Down, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Down)
        ClickTecladoVirtual(p_Left, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Down, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Left, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Left, clicks=2)
        ClickTecladoVirtual(p_Down, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Down, clicks=3)
        ClickTecladoVirtual(p_Left, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Down, clicks=2, modo="instantaneo")
        
    
    elif cidade == "Mauville":
        
        ClickTecladoVirtual(p_Down, clicks=2)
        ClickTecladoVirtual(p_Right, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Right, clicks=16)
        
        ClickTecladoVirtual(p_Right)
        print ("Tomando cuidado com o bug...")
        time.sleep(4)
        print ("Continuando...")

        ClickTecladoVirtual(p_Right, clicks=16)
        ClickTecladoVirtual(p_Down, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Right, clicks=2, modo="instantaneo")

        # Usa surf.
        erro = UsarSurf(p_Z)
        if erro != OK:
            print ("Erro na função \"CaminharAteSlotBerry\".")
            return erro

        # Surfando...
        pyautogui.mouseDown(p_Right)
        time.sleep(5.5)
        pyautogui.mouseUp(p_Right)
        time.sleep(0.5)

        ClickTecladoVirtual(p_Down, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Down, clicks=3)
        ClickTecladoVirtual(p_Right, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Right, clicks=9)
        ClickTecladoVirtual(p_Up, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Up)
        ClickTecladoVirtual(p_Right, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Right, clicks=35)
        
        print ("Tomando cuidado com o bug...")
        time.sleep(4)
        print ("Continuando...")

        ClickTecladoVirtual(p_Right, clicks=8)
        
        
        ClickTecladoVirtual(p_Down, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Down, clicks=3)
        ClickTecladoVirtual(p_Right, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Right, clicks=4)

        # Um cara bloqueando a passagem.
        passou = False
        while not passou:
            # Passando pelo cara bloqueando a passagem.
            ClickTecladoVirtual(p_Right)
            # Verificando se o personagem passou dele.
            chatApareceu = False
            tentativa = 1
            maxTentativas = 50
            while not chatApareceu and tentativa < maxTentativas:
                ClickTecladoVirtual(p_Z)
                if CheckPixel("fimConversa", espera=0.0, tentativas=1):
                    chatApareceu = True
                tentativa += 1

            if chatApareceu:
                # Fecha a conversa.
                ClickTecladoVirtual(p_Z)
                time.sleep(1.5)
            else:
                passou = True
            
        # Continuando o trajeto até o primeiro slot.
        ClickTecladoVirtual(p_Right, clicks=6)
        ClickTecladoVirtual(p_Up, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Up, clicks=4)
        ClickTecladoVirtual(p_Left, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Left, clicks=6)
        ClickTecladoVirtual(p_Up, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Up, clicks=5)
        ClickTecladoVirtual(p_Left, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Left)
        ClickTecladoVirtual(p_Up, modo="instantaneo")

    elif cidade == "Mistralton":

        ClickTecladoVirtual(p_Left, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Left, clicks=3)
        ClickTecladoVirtual(p_Up, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Up, clicks=7)
        ClickTecladoVirtual(p_Left, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Left, clicks=32)
        ClickTecladoVirtual(p_Down, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Down, clicks=33)


    elif cidade == "Undella":
        
        ClickTecladoVirtual(p_Left, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Left, clicks=6)
        ClickTecladoVirtual(p_Down, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Down, clicks=9)
        ClickTecladoVirtual(p_Left, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Left, clicks=30)
        ClickTecladoVirtual(p_Down, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Down, clicks=7)
        ClickTecladoVirtual(p_Right, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Right, clicks=24)
        ClickTecladoVirtual(p_Down, clicks=2, modo="instantaneo")
        
        print ("Tomando cuidado com o bug...")
        time.sleep(4)
        print ("Continuando...")
        
        ClickTecladoVirtual(p_Down, clicks=23)
        ClickTecladoVirtual(p_Left, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Left, clicks=12)
        ClickTecladoVirtual(p_Down, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Down, clicks=4)
        ClickTecladoVirtual(p_Left, clicks=2, modo="instantaneo")

        # Usa Surf.
        erro = UsarSurf(p_Z)
        
        if erro != OK:
            # Quer dizer que o npc não chegou na área do surf conforme planejado.
            # Refazendo o processo de caminhada.

            # Voando para Undella.
            erro = Fly(p_F2, regiao="Unova", cidade="Undella")
            if erro != OK:
                return erro

            tentativa += 1
            if tentativa <= 5:
                erro = CaminharAteSlotBerry(p_Teclas, cidade="Undella", tentativa=tentativa)
                return erro

            print ("Personagem não conseguiu chegar na posição do primeiro surf em Undella.")
            return ERRO_CAMINHAR_ATE_SLOT

        time.sleep(2)

        # Usa Super repel.
        ClickTecladoVirtual(p_F5)
        
        # Usa Waterfall.
        erro = UsarWaterFall(p_Z)
        if erro != OK:
            print ("Erro na função \"CaminharAteSlotBerry\".")
            return erro

        # Surfando...
        pyautogui.mouseDown(p_Left)
        time.sleep(1.5)
        pyautogui.mouseUp(p_Left)

        # Usa Waterfall.
        erro = UsarWaterFall(p_Z)
        if erro != OK:
            print ("Erro na função \"CaminharAteSlotBerry\".")
            return erro

        # Surfando...
        pyautogui.mouseDown(p_Left)
        time.sleep(2.3)
        pyautogui.mouseUp(p_Left)

        # Vai pra terra.
        ClickTecladoVirtual(p_Down, clicks=2, modo="instantaneo")
        time.sleep(1)

        ClickTecladoVirtual(p_Down, clicks=3)
        ClickTecladoVirtual(p_Left, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Left, clicks=13)
        ClickTecladoVirtual(p_Down, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Down, clicks=2)
        ClickTecladoVirtual(p_Left)

        # Usa Surf.
        erro = UsarSurf(p_Z)
        if erro != OK:
            print ("Erro na função \"CaminharAteSlotBerry\".")
            return erro

        ClickTecladoVirtual(p_Down, clicks=2, modo="instantaneo")

        # Usa Waterfall.
        erro = UsarWaterFall(p_Z)
        if erro != OK:
            print ("Erro na função \"CaminharAteSlotBerry\".")
            return erro

        # Surfando...
        pyautogui.mouseDown(p_Down)
        time.sleep(1.0)
        pyautogui.mouseUp(p_Down)

        ClickTecladoVirtual(p_Left, clicks=2, modo="instantaneo")

        # Sai do surf e vai pra esquerda
        pyautogui.mouseDown(p_Left)
        time.sleep(5)
        pyautogui.mouseUp(p_Left)
        time.sleep(0.2)
        
        ClickTecladoVirtual(p_Up, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Up, clicks=4)
        ClickTecladoVirtual(p_Right, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Up, clicks=2, modo="instantaneo")
        
        # Entrando na floresta.
        ClickTecladoVirtual(p_Up)
        time.sleep(4)

        ClickTecladoVirtual(p_Up, clicks=6)
        ClickTecladoVirtual(p_Left, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Up, modo="instantaneo")

    else:
        return CIDADE_NAO_CADASTRADA

    return OK

def PlantarRegarColherNaTiraDeSlots(p_Teclas, numSlots, sentido="", posicionamento="", modo=""):
    '''
    Planta Cheri Berry na tira de slot no sentido indicado.

    Argumentos: 
            ->  p_Z -> tupla -> obrigatório.    
            ->  p_A -> tupla -> obrigatório. Posição da tecla de regar.    
            ->  numSlots -> inteiro positivo -> Obrigatório. Indica quantos slots tem essa tira.
            ->  p_Left, p_Up, p_Right, p_Down -> tupla -> Desses, só são obrigatórios os que são necessários
            para plantar as berries no sentido desejado.
            ->  sentido -> string -> Obrigatório. Indica o sentido de plantio na tira de slots.
            ->  posicionamento -> string -> Obrigatório. Indica o posicionamento do personagem em relação a tira. 
            ->  modo -> string -> indica o modo da função, se é plantar, regar ou colher.

    OBS:
        Valores válidos para "sentido": "baixo", "direita" e "esquerda"
    
        Valores válidos para "posicionamento": "acima" e "abaixo"

        Valores válidos para "modo": "plantar", "regar", "colher" e "colherEPlantar"

    Retornos:   OK
                FALTANDO_ARGUMENTOS 
                POSICIONAMENTO_INVALIDO
                SENTIDO_INVALIDO
                ERRO_PLANTANDO_NA_TIRA_DE_SLOTS                
                MODO_INVALIDO 
                SETA_NAO_ENCONTRADA
                ERRO_REGANDO
    '''

    #Posicoes de cada tecla
    p_Left = p_Teclas[1]           
    p_Up = p_Teclas[2]
    p_Right = p_Teclas[3]
    p_Down = p_Teclas[4]
    p_Z = p_Teclas[5]
    p_A = p_Teclas[14]


    if sentido == "":
        print ("Erro na função \"PlantandoNaTiraDeSlots\". Faltando argumento \"sentido\".")
        return FALTANDO_ARGUMENTOS

    if modo != "plantar" and modo != "regar" and modo != "colher" and modo != "colherEPlantar":
        print ("Argumento \"modo\" inválido.")
        return MODO_INVALIDO


    #### Verificando o sentido e o posicionamento inserido, para ajustar as variáveis p_Tecla1 e p_Tecla2. ####
    
    if sentido == "baixo":
        p_Tecla1 = p_Down
        p_Tecla2 = p_Left
    
    elif sentido == "direita":
        if posicionamento == "acima":
            p_Tecla1 = p_Right
            p_Tecla2 = p_Down
        
        elif posicionamento == "abaixo":
            p_Tecla1 = p_Right
            p_Tecla2 = p_Up
        
        else:
            print ("Erro na função \"PlantandoNaTiraDeSlots\". Argumento \"posicionamento\" inválido.")
            return POSICIONAMENTO_INVALIDO
    
    elif sentido == "esquerda":
        if posicionamento == "acima":
            p_Tecla1 = p_Left
            p_Tecla2 = p_Down
    
        elif posicionamento == "abaixo":
            p_Tecla1 = p_Left
            p_Tecla2 = p_Up
       
        else:
            print ("Erro na função \"PlantandoNaTiraDeSlots\". Argumento \"posicionamento\" inválido.")
            return POSICIONAMENTO_INVALIDO
            

    else:
        print ("Erro na função \"PlantandoNaTiraDeSlots\". Argumento \"sentido\" inválido.")
        return SENTIDO_INVALIDO
                                                ########

    #### Plantando as Berries na tira ####
    slot = 0
    modoOriginal = modo
    while slot < numSlots:

        if modoOriginal == "colherEPlantar":
            repetir = 1
            modo = "colher"
        else:
            repetir = 0

        while repetir >= 0:
            if modo != "regar":
                # Interagindo com o slot de berry.
                time.sleep(0.5)
                ClickTecladoVirtual(p_Z)
                erro = ContinuarConversa(p_Z)
                if erro != OK:
                    print ("Erro na função \"PlantandoNaTiraDeSlots\"")
                    return erro

                if not CheckPixel("Sim"):
                    print ("Não encontrou o botão \"Sim\" para plantar.")
                    return ERRO_PLANTANDO_NA_TIRA_DE_SLOTS
                
                # Aperta "Sim"
                ClickTecladoVirtual(p_Z)

                if modo == "plantar":
                    
                    # Planta a Cheri Berry.
                    print("Plantando no slot...")
                    
                    if ImagemEncontrada("CheriBerry1.png", "CheriBerry2.png", "CheriBerry3.png", tentativas=3): # Se as sementes já estiverem selecionadas.
                        ClickTecladoVirtual(p_Z)
                    else:
                        erro = PlantarSementesPicantes(p_Z)
                        if erro != OK:
                            print ("Erro na função \"PlantandoNaTiraDeSlots\"")
                            return erro


                # Termina a interação.
                erro = ContinuarConversa(p_Z)
                if erro != OK:
                    print ("Erro na função \"PlantandoNaTiraDeSlots\"")
                    return erro
                time.sleep(0.3)


            if modo != "colher":

                # Tenta regar em um máximo de 2 vezes.
                regou = False
                tentarRegar = 1
                while not regou and tentarRegar <= 2:

                    # Regando esse slot.
                    print ("Regando...")
                    ClickTecladoVirtual(p_A)
                    
                    # Verificando se regou
                    regou = CheckPixel("balaoChat")
                    if not regou:
                        tentarRegar += 1

                if tentarRegar > 2: 
                    print ("Erro regando alguma berry.")
                    return ERRO_REGANDO

                time.sleep(2)

            repetir -= 1

            if repetir == 0: # Significa que acabou de colher e agora vai plantar.
                modo = "plantar"

        if slot < numSlots - 1:
            # Indo para o próximo slot.
            ClickTecladoVirtual(p_Tecla1, clicks=2, modo="instantaneo")
            ClickTecladoVirtual(p_Tecla2, modo="instantaneo")

        slot += 1

    return OK

def CultivarBerriesHoenn(p_Teclas, regiaoOrigem, modo=""):
    '''
    Plantar, regar ou colher todos os slots de Hoenn.

    Argumentos: 
                p_Teclas -> tupla -> lista com todas as posições das teclas
                regiaoOrigem -> string -> Regiao que o personagem se encontra atualmente.
                modo -> string -> indica o modo da função, se é plantar, regar ou colher.

        OBS:
            Valores válidos para "modo": "plantar", "regar", "colher" e "colherEPlantar"

    Retornos:   
                OK

    '''
    
    #Posicoes de cada tecla
    p_Left = p_Teclas[1]          # Recebem (x,y) 
    p_Up = p_Teclas[2]
    p_Right = p_Teclas[3]
    p_Down = p_Teclas[4]
    p_Z = p_Teclas[5]
    p_F1 = p_Teclas[8]
    p_F2 = p_Teclas[9]
    
    
    # Indo para Hoenn, se o personagem não estiver.
    if regiaoOrigem != "Hoenn":
        print ("Mudando para Hoenn...")
        erro = TrocarRegiao(p_Teclas, regiaoOrigem=regiaoOrigem, regiaoDestino="Hoenn")
        if erro != OK:
            return erro
    
    ################################ PLANTANDO EM RUSTBORO ################################
    
    repetir = True
    while repetir:
        # Voando para Rustboro City.
        print ("Usando Fly para Rustboro City...")
        erro = Fly(p_F2, "Hoenn", cidade="Rustboro")
        if erro != OK:
            return erro
        print ("Chegou em Rustboro.")
    
        # Caminhando até o primeiro slot.
        print ("Caminhando para o primeiro slot...")
        CaminharAteSlotBerry(p_Teclas, cidade="Rustboro")
        
        if ChegouNoSlotBerry(p_Down, p_Z, modo):
            repetir = False
    
    print ("Plantando...")
    # Plantando na primeira tira

    erro = PlantarRegarColherNaTiraDeSlots(p_Teclas, 5, sentido="baixo", modo=modo)
    if erro != OK:
        return erro
    
    # Caminhando até a segunda tira.
    ClickTecladoVirtual(p_Up, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Right, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Right, clicks=5)
    ClickTecladoVirtual(p_Up, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Up, clicks=10)
    

    #Plantando na segunda tira
    erro = PlantarRegarColherNaTiraDeSlots(p_Teclas, 3, sentido="direita", posicionamento="abaixo", modo=modo)
    if erro != OK:
        return erro
    
    # Caminhando até a terceira tira.
    ClickTecladoVirtual(p_Right, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Up, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Up)
    ClickTecladoVirtual(p_Left, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Up)
    time.sleep(0.5)
    
    
    # Plantando na terceira tira
    erro = PlantarRegarColherNaTiraDeSlots(p_Teclas, 3, sentido="esquerda", posicionamento="abaixo", modo=modo)
    if erro != OK:
        return erro
    
    ################################ PLANTANDO EM FORTRESS ################################
    
    tentativa = 1
    while tentativa >= 1:
        
        # Voando para Fortree City.
        print ("Usando Fly para Fortree City...")
        erro = Fly(p_F2, "Hoenn", cidade="Fortree")
        if erro != OK:
            return erro
        print ("Chegou em Fortree.")
        
        time.sleep(2)

        # Caso não tenha chegado no primeiro lote.
        if tentativa > 1:
            
            # Gastando os restante de passos de super repel.
            Virar("direita", p_Teclas)
            ClickTecladoVirtual(p_Left)
            Virar("baixo", p_Teclas)
            ClickTecladoVirtual(p_Down, clicks=3)
            ClickTecladoVirtual(p_F1)
                        
            while not CheckPixel("Sim", espera=0.0, tentativas=1):
                pyautogui.mouseDown(p_Left)
                time.sleep(1)
                pyautogui.mouseUp(p_Left)
                pyautogui.mouseDown(p_Right)
                time.sleep(1)
                pyautogui.mouseUp(p_Right)

            # Clica para não estender.
            ClickTecladoVirtual(p_Down)
            ClickTecladoVirtual(p_Z)

            # Voando para Fortree City.
            print ("Usando Fly para Fortree City...")
            erro = Fly(p_F2, "Hoenn", cidade="Fortree")
            if erro != OK:
                return erro
            print ("Chegou em Fortree.")
            
            time.sleep(2)


        # Caminhando até o primeiro slot.
        print ("Caminhando para o primeiro slot...")
        CaminharAteSlotBerry(p_Teclas, cidade="Fortree")
        

        if ChegouNoSlotBerry(p_Down, p_Z, modo):
            # Sai do while.
            tentativa = 0
        else:
            tentativa += 1
        


    # Plantando na primeira tira.
    print ("Plantando...")
    erro = PlantarRegarColherNaTiraDeSlots(p_Teclas, 6, sentido="direita", posicionamento="acima", modo=modo)
    if erro != OK:
        return erro

    ClickTecladoVirtual(p_Up, modo="instantaneo")
    
    # Plantando na segunda tira.
    erro = PlantarRegarColherNaTiraDeSlots(p_Teclas, 4, sentido="esquerda", posicionamento="abaixo", modo=modo)
    if erro != OK:
        return erro
    
    
    ################################ PLANTANDO EM MAUVILLE ################################

    # Voando para Mauville.
    print ("Usando Fly para Mauville City...")
    erro = Fly(p_F2, "Hoenn", cidade="Mauville")
    if erro != OK:
        return erro
    print ("Chegou em Mauville.")
    
    # Caminhando até o primeiro slot.
    print ("Caminhando para o primeiro slot...")
    erro = CaminharAteSlotBerry(p_Teclas, cidade="Mauville")
    if erro != OK:
        return erro

    # Plantando nas tiras.
    print ("Plantando...")
    repetir = 0
    while repetir <= 2:
        # Plantando na tira de cima.
        erro = PlantarRegarColherNaTiraDeSlots(p_Teclas, 2, sentido="direita", posicionamento="abaixo", modo=modo)
        if erro != OK:
            return erro

        ClickTecladoVirtual(p_Down)

        # Plantando na tira de baixo.
        erro = PlantarRegarColherNaTiraDeSlots(p_Teclas, 2, sentido="esquerda", posicionamento="acima", modo=modo)
        if erro != OK:
            return erro

        # Indo pra tira à direita.        
        if repetir <= 1:
            ClickTecladoVirtual(p_Right, clicks=2, modo="instantaneo")
            ClickTecladoVirtual(p_Right, clicks=2)
            ClickTecladoVirtual(p_Up)

        repetir += 1


    return OK

def CultivarBerriesUnova(p_Teclas, regiaoOrigem, modo=""):
    '''
    Plantar, regar ou colher todos os slots de Unova.

    Argumentos: 
                p_Teclas -> tupla -> lista com todas as posições das teclas
                regiaoOrigem -> string -> Regiao que o personagem se encontra atualmente.
                modo -> string -> indica o modo da função, se é plantar, regar ou colher.

        OBS:
            Valores válidos para "modo": "plantar", "regar", "colher" e "colherEPlantar"


    Retornos:   OK
                Muitos outros
    '''

    p_Left = p_Teclas[1]           
    p_Up = p_Teclas[2]
    p_Right = p_Teclas[3]
    p_Down = p_Teclas[4]
    p_Z = p_Teclas[5]
    p_F2 = p_Teclas[9]
    p_F6 = p_Teclas[11]

    
    # Indo para Unova, se o personagem não estiver.
    if regiaoOrigem != "Unova":
        print ("Mudando para Unova...")
        
        # Trocando de região.
        erro = TrocarRegiao(p_Teclas, regiaoOrigem=regiaoOrigem, regiaoDestino="Unova")
        if erro != OK:
            return erro
    

    ################################ PLANTANDO EM MISTRALTON ################################
    
    repetir = True
    while repetir:    
        # Voando para Mistralton City.
        print ("Usando Fly para Mistralton City...")
        
        erro = Fly(p_F2, "Unova", cidade="Mistralton")
        if erro != OK:
            return erro
        print ("Chegou em Mistralton.")
        
        # Caminhando até o primeiro slot.
        print ("Caminhando para o primeiro slot...")
        CaminharAteSlotBerry(p_Teclas, cidade="Mistralton")

        if ChegouNoSlotBerry(p_Down, p_Z, modo):
            repetir = False
    
    # Cultivando nos slots.
    print ("Cultivando...")
    repetir = 0
    while repetir <= 2:

        erro = PlantarRegarColherNaTiraDeSlots(p_Teclas, 6, sentido="direita", posicionamento="acima", modo=modo)
        if erro != OK:
            return erro
                
        ClickTecladoVirtual(p_Right, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Right, clicks=3)
        ClickTecladoVirtual(p_Down, modo="instantaneo")

        erro = PlantarRegarColherNaTiraDeSlots(p_Teclas, 6, sentido="direita", posicionamento="acima", modo=modo)
        if erro != OK:
            return erro

        ClickTecladoVirtual(p_Right, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Down, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Down, clicks=2)
        ClickTecladoVirtual(p_Left, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Up, modo="instantaneo")

        erro = PlantarRegarColherNaTiraDeSlots(p_Teclas, 6, sentido="esquerda", posicionamento="abaixo", modo=modo)
        if erro != OK:
            return erro

        ClickTecladoVirtual(p_Left, clicks=2, modo="instantaneo")
        ClickTecladoVirtual(p_Left, clicks=3)
        ClickTecladoVirtual(p_Up, modo="instantaneo")


        erro = PlantarRegarColherNaTiraDeSlots(p_Teclas, 6, sentido="esquerda", posicionamento="abaixo", modo=modo)
        if erro != OK:
            return erro

        if repetir <= 1:
            ClickTecladoVirtual(p_Down, clicks=2, modo="instantaneo")
            ClickTecladoVirtual(p_Down)

        repetir += 1

    
    ################################ PLANTANDO EM UNDELLA ################################
    
    # Voando para Undella Town.
    print ("Usando Fly para Undella Town...")
    
    erro = Fly(p_F2, "Unova", cidade="Undella")
    if erro != OK:
        return erro
    print ("Chegou em Undella.")

    # Caminhando até o primeiro slot.
    print ("Caminhando para o primeiro slot...")
    erro = CaminharAteSlotBerry(p_Teclas, cidade="Undella")
    if erro != OK:
        print ("Erro CaminharAteSlotBerry em Undella.")
        return erro
    
    # Cultivando nos slots.
    print ("Cultivando...")
    erro = PlantarRegarColherNaTiraDeSlots(p_Teclas, 6, sentido="esquerda", posicionamento="abaixo", modo=modo)
    if erro != OK:
        return erro
    
    ClickTecladoVirtual(p_Left, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Up, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Up, clicks=2)
    ClickTecladoVirtual(p_Right, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Down, modo="instantaneo")

    erro = PlantarRegarColherNaTiraDeSlots(p_Teclas, 6, sentido="direita", posicionamento="acima", modo=modo)
    if erro != OK:
        return erro

    ClickTecladoVirtual(p_Up, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Left, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Left, clicks=7)
    ClickTecladoVirtual(p_Up, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Up)
    ClickTecladoVirtual(p_Right, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Up, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Up)
    ClickTecladoVirtual(p_Right, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Right)
    ClickTecladoVirtual(p_Up, modo="instantaneo")

    erro = PlantarRegarColherNaTiraDeSlots(p_Teclas, 6, sentido="direita", posicionamento="abaixo", modo=modo)
    if erro != OK:
        return erro

    ClickTecladoVirtual(p_Right, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Up, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Up, clicks=2)
    ClickTecladoVirtual(p_Left, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Down, modo="instantaneo")

    erro = PlantarRegarColherNaTiraDeSlots(p_Teclas, 6, sentido="esquerda", posicionamento="acima", modo=modo)
    if erro != OK:
        return erro

    ClickTecladoVirtual(p_Left, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Left, clicks=6)
    ClickTecladoVirtual(p_Down, modo="instantaneo")

    erro = PlantarRegarColherNaTiraDeSlots(p_Teclas, 6, sentido="esquerda", posicionamento="acima", modo=modo)
    if erro != OK:
        return erro

    ClickTecladoVirtual(p_Left, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Down, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Down, clicks=2)
    ClickTecladoVirtual(p_Right, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Up, modo="instantaneo")

    erro = PlantarRegarColherNaTiraDeSlots(p_Teclas, 6, sentido="direita", posicionamento="abaixo", modo=modo)
    if erro != OK:
        return erro

    ClickTecladoVirtual(p_Left, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Left, clicks=5)

    ClickTecladoVirtual(p_Down, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Down)
    ClickTecladoVirtual(p_Left, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Left, clicks=10)
    ClickTecladoVirtual(p_Down, clicks=2, modo="instantaneo")

    erro = PlantarRegarColherNaTiraDeSlots(p_Teclas, 6, sentido="esquerda", posicionamento="acima", modo=modo)
    if erro != OK:
        return erro

    ClickTecladoVirtual(p_Left, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Down, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Down, clicks=2)
    ClickTecladoVirtual(p_Right, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Up, modo="instantaneo")

    erro = PlantarRegarColherNaTiraDeSlots(p_Teclas, 6, sentido="direita", posicionamento="abaixo", modo=modo)
    if erro != OK:
        return erro

    ClickTecladoVirtual(p_Left, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Left, clicks=5)
    ClickTecladoVirtual(p_Up, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Up, clicks=8)

    erro = PlantarRegarColherNaTiraDeSlots(p_Teclas, 6, sentido="direita", posicionamento="abaixo", modo=modo)
    if erro != OK:
        return erro

    ClickTecladoVirtual(p_Right, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Up, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Up)

    
    # Verifica se o repel acabou e se veio a pergunta de estender com mais um.
    erro = EstenderRepel(p_Teclas, escolha="N")

    ClickTecladoVirtual(p_Up)
    ClickTecladoVirtual(p_Left, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Down, modo="instantaneo")

    # Se, na vdd, não foi encontrado a pergunta de estender o repel.
    if erro != OK:
        # Verifica se mesmo assim o personagem chegou no local desejado.
        if not ChegouNoSlotBerry(p_Down, p_Z, modo=modo):
            print ("Erro de posição do personagem. Não chegou na parte de estender o repel.")
            return erro

    erro = PlantarRegarColherNaTiraDeSlots(p_Teclas, 6, sentido="esquerda", posicionamento="acima", modo=modo)
    if erro != OK:
        return erro

    ClickTecladoVirtual(p_Left, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Left)
    ClickTecladoVirtual(p_Up, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Up, clicks=3)
    ClickTecladoVirtual(p_Right, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Right, clicks=2)
    ClickTecladoVirtual(p_Up, modo="instantaneo")
    
    erro = PlantarRegarColherNaTiraDeSlots(p_Teclas, 6, sentido="esquerda", posicionamento="abaixo", modo=modo)
    if erro != OK:
        return erro

    ClickTecladoVirtual(p_Left, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Up, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Up, clicks=2)
    ClickTecladoVirtual(p_Right, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Down, modo="instantaneo")

    erro = PlantarRegarColherNaTiraDeSlots(p_Teclas, 6, sentido="direita", posicionamento="acima", modo=modo)
    if erro != OK:
        return erro

    ClickTecladoVirtual(p_Right, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Down, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Down, clicks=2)
    ClickTecladoVirtual(p_Right, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Right, clicks=3)
    ClickTecladoVirtual(p_Up, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Right, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Up, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Up, clicks=12)
    ClickTecladoVirtual(p_Right, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Right, clicks=5)

    # Usar Repel.
    ClickTecladoVirtual(p_F6)

    # Usa Surf.
    erro = UsarSurf(p_Z)
    if erro != OK:
        print ("Erro na função \"CaminharAteSlotBerry\".")
        return erro

    # Vai surfando pra direita
    pyautogui.mouseDown(p_Right)
    time.sleep(3.5)
    pyautogui.mouseUp(p_Right)
    time.sleep(0.2)

    ClickTecladoVirtual(p_Down, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Down, clicks=2)
    ClickTecladoVirtual(p_Right, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Down, modo="instantaneo")

    erro = PlantarRegarColherNaTiraDeSlots(p_Teclas, 6, sentido="direita", posicionamento="acima", modo=modo)
    if erro != OK:
        return erro

    ClickTecladoVirtual(p_Right, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Down, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Down, clicks=2)
    ClickTecladoVirtual(p_Left, clicks=2, modo="instantaneo")
    ClickTecladoVirtual(p_Up, modo="instantaneo")

    erro = PlantarRegarColherNaTiraDeSlots(p_Teclas, 6, sentido="esquerda", posicionamento="abaixo", modo=modo)
    if erro != OK:
        return erro
    

    return OK

def UsarSurf(p_Z):
    '''
    Usa surf.

    Argumentos: p_Z -> tupla -> posição da tecla Z 
    
    Retornos:   OK
                ERRO_SURF
    '''
    # Aperta Z para surfar.
    time.sleep(0.5)
    ClickTecladoVirtual(p_Z)
    
    # Selecionando Yes.
    if not CheckPixel("Sim"):
        print ("Não encontrou o botão \"Sim\" para surfar.")
        return ERRO_SURF
    
    ClickTecladoVirtual(p_Z)
    
    # Terminar interação.
    erro = ContinuarConversa(p_Z)
    if erro != OK:
        print ("Erro na função \"UsarSurf\".")
        return erro

    time.sleep(4)

    return OK

def UsarWaterFall(p_Z):
    '''
    Usa waterfall.

    Argumentos: p_Z -> tupla -> posição da tecla Z 
    
    Retornos:   OK
                ERRO_WATERFALL
    '''
    # Mesma ideia do surf.
    erro = UsarSurf(p_Z)
    if erro != OK:
        print ("Erro usando Watterfall.")
        return erro

    time.sleep(1)
    return OK

def ChegouNoSlotBerry(p_Down, p_Z, modo):
    '''
    Verifica se o personagem chegou no slot de berry desejado.
    
    Argumentos: 
                p_Down -> tupla -> posição da seta pra baixo 
                p_Z -> tupla -> posição da tecla Z 
                modo -> string -> indica o modo da função, se é plantar, regar ou colher.

        OBS:
            Valores válidos para "modo": "plantar", "regar", "colher" e "colherEPlantar"


    Retornos:   True ou False
    
    '''
    # Interagindo com o slot de berry.
    time.sleep(0.5)
    ClickTecladoVirtual(p_Z)
    
    erro = ContinuarConversa(p_Z)
    if erro != OK:
        print ("Não chegou no slot")
        return False
    
    if modo == "regar":
        erro = ContinuarConversa(p_Z)
        if erro != OK:
            print ("Não chegou no slot")
            return False
        
    if not CheckPixel("Sim"):
        print ("Não chegou no slot")
        return False
    
    # Aperta "Não"
    ClickTecladoVirtual(p_Down)
    time.sleep(0.2)
    ClickTecladoVirtual(p_Z)
    
    if modo == "colher" or modo == "colherEPlantar":
        erro = ContinuarConversa(p_Z)
        if erro != OK:
            print ("Não chegou no slot")
            return False
    

    return True

##### HORDA DE POKEMONS #####

def StringTuplaParaTupla(string):
    '''
    Converte uma string da forma "(a, b)" ou "(a, b, c)", onde a, b e c têm que ser números naturais; para tupla.
    Essa função foi feita para ser usada para pixel e cores do pixel, mas pode ser usada para o que for necessário,
    se possível.

    Argumentos:
                string -> string -> string no formato "(a, b)"
    
    Retorns:    tupla
                TUPLA_INVALIDA
                STRING_VAZIA
    '''
    if len(string) == 0:
        return STRING_VAZIA
    if string[0] != '(':
        return TUPLA_INVALIDA
    if string[-1] == '\n':  
        string = string[0:-1]  # tira o '\n' se a string tiver
    if string[-1] != ')':
        return TUPLA_INVALIDA

    tamanhoString = len(string)
    isTupla = False
    fimString = False
    coordenada = ["", "", ""]
    caracteresValidos = "0123456789,() "
    virgula = 0
    abreParenteses = 0

    for caracter in range(tamanhoString):

        # Verifica se o caracter é inválido.
        caracterValido = False
        for termo in caracteresValidos:
            if string[caracter] == termo:
                caracterValido = True
        if caracterValido == False:
            return TUPLA_INVALIDA
        
        if string[caracter] != ' ':

            # Se achar o ')', tem que ser o fim da string.
            if string[caracter] == ')':
                if caracter + 1 != tamanhoString:
                    return TUPLA_INVALIDA
                fimString = True

            if not fimString:
                if string[caracter] == ',':
                    if not isTupla:
                        return TUPLA_INVALIDA
                    virgula += 1
                    if virgula > 2:
                        return TUPLA_INVALIDA                
                
                elif string[caracter] == '(':
                    isTupla = True
                    abreParenteses += 1
                    if abreParenteses > 1:
                        return TUPLA_INVALIDA  
                
                elif isTupla:
                    coordenada[virgula] += string[caracter]              
    # end for
    x = 0
    y = 1
    z = 2
    if coordenada[x] == "" or coordenada[y] == "":
        return TUPLA_INVALIDA
    if coordenada[z] == "" and virgula == 2:
        return TUPLA_INVALIDA
    if not fimString:
        return TUPLA_INVALIDA

    if virgula == 2:
        pixel = (int(coordenada[x]), int(coordenada[y]), int(coordenada[z]))
    else:
        pixel = (int(coordenada[x]), int(coordenada[y]))
    print (pixel)
    return pixel

def AdquirirDadosHorda(nomeArquivo=""):
    '''
    Retorna todas as posições, registradas no arquivo, de cada pokemon da horda.

    Argumentos: nomeArquivo -> string -> nome do arquivo que contém as posições (sem a extensão)

    Retornos:
                lista posições para cada pokemon da horda (lista de lista)
                ERRO_CRIANDO_ARQUIVO
                TUPLA_INVALIDA

    '''
    if nomeArquivo == "":
        return FALTANDO_ARGUMENTOS

    # Nomeando o arquivo
    nomeArquivo = nomeArquivo + ".txt"
    try:
        hordaFile = open(nomeArquivo, "r")
    except:
        print ("Criando o arquivo...")    
        try:
            hordaFile = open(nomeArquivo, "w")
        except:
            return ERRO_CRIANDO_ARQUIVO
        listaDados = []
        linhasHordaFile = []
    else:
        print ("Arquivo já existia.")

        linhasHordaFile = hordaFile.readlines()
        hordaFile.close()
        listaDados = []
        if len(linhasHordaFile) != 0:
            for linha in linhasHordaFile: 
                listaPosicoes = []
                if len(linha) != 0:
                    if linha[0] != '\n':
                        listaPosicaoString = linha.split(';')
                        print(listaPosicaoString)
                        for posicaoString in listaPosicaoString:
                            posicao = StringTuplaParaTupla(posicaoString)
                            if posicao == TUPLA_INVALIDA:
                                print ("Arquivo não contém tuplas válidas.")
                                return TUPLA_INVALIDA
                            listaPosicoes.append(posicao)
                listaDados.append(listaPosicoes)
    # end else
    qntdDados = len(linhasHordaFile)
    qntdRestanteDados = 5 - qntdDados
    while qntdRestanteDados > 0:
        listaDados.append([])
        qntdRestanteDados -= 1

    return listaDados

def CadastrarPosicaoHorda(nomeArquivo, posicao, linhaAlvo):
    '''
    Cadastra a posição desejada no arquivo da horda. O arquivo da horda tem que estar correto,
    pois essa função não consegue identificar erros.
    
    Argumentos: nomeArquivo -> string -> nome do arquivo com os dados já cadastrados da horda (sem o .txt)
                
                posicao -> tupla -> posição que deseja cadastrar no arquivo
                
                linhaAlvo -> int -> numero da linha correspondente ao pokemon (pokemon do lado inferior
            direito, pokemon do lado inferior esquerdo, etc.)
    
    Retornos:   OK
    '''       
    # Nomeando o arquivo
    nomeArquivo = nomeArquivo + ".txt"
    
    # Abrindo o arquivo.
    try:
        hordaMagikarpFile = open(nomeArquivo, "r")
    except:
        # Criando o arquivo, já que o mesmo não existe.
        hordaMagikarpFile = open(nomeArquivo, "w")
        conteudo = []
    else:
        conteudo = hordaMagikarpFile.readlines()
    
    hordaMagikarpFile.close()
    num_linhas = len(conteudo)
    
    # Se a linha não existir ainda no arquivo, vai criando as linhas até chegar na desejada.
    print ("O que está no arquivo:", conteudo)
    
    if linhaAlvo > num_linhas:
        for aux in range(num_linhas, linhaAlvo):
            if aux == 4:
                conteudo.append('')
            else:
                conteudo.append("\n")

    print ("Antes de insert:", conteudo)

    # Adiciona a posição no início da linha desejada.
    if len(conteudo[linhaAlvo - 1]) == 0:
        conteudo.insert(linhaAlvo - 1, str(posicao))
    elif conteudo[linhaAlvo - 1][0] == '\n':
        conteudo.insert(linhaAlvo - 1, str(posicao))
    else:
        conteudo.insert(linhaAlvo - 1, str(posicao) + ';')

    # Atualiza o arquivo.
    hordaMagikarpFile = open(nomeArquivo, "w")
    print ("Depois de insert:", conteudo)
    hordaMagikarpFile.writelines(conteudo)
    hordaMagikarpFile.close()
    return OK


def ReconhecerHorda(pokemonAlvo, listaPosicoes):
    '''
    Uma vez usado o sweet scent, reconhece cada pokemon da horda, verificando também se é shiny.
    
    Argumentos:
                pokemonAlvo -> string -> pokemon que o script objetiva
                listaPosicoes -> lista com 5 elementos -> lista de posicoes de cada pokemon da horda (lista de lista)

    Retornos:   
                CADASTROU_NOVA_POSICAO
                ACHOU_SHINY_NA_HORDA + int
                SEM_SHINY
            Erros:
                HORDA_NAO_APARECEU
                LISTA_INVALIDA
    '''
    if len(listaPosicoes) != 5:
        print ("Lista de posições, da horda, inválida.")
        return LISTA_INVALIDA

    print ("Lista posições =", listaPosicoes)

    # Verifica se os pokemons já apareceram.
    if not CheckPixel("hordaApareceu"):
        print ("Nao apareceu o nome do pokemon. Provavelmente estah numa acao diferente")
        return HORDA_NAO_APARECEU 

    if pokemonAlvo == "Magikarp":
        for magikarp in range(5):
            # Colocando o cursor em cima do nome do respectivo magikarp.
            pyautogui.moveTo(POSITIONS_HORDE_MOUSE[magikarp], duration=0.1)
        
            posicaoMagikarp = CentroDaImagem(PosicaoEDimensaoDaImagem("MagikarpChuva1.png", 
                    "Magikarp2.png", "MagikarpChuva2.png", "MagikarpChuva2Nivel10.png", tentativas=2, espera=0.0))
        
            # Imagem nao foi reconhecida. Nao eh magikarp ou nao foi reconhecido. Pode ser um shiny ou n.
            if posicaoMagikarp == IMG_NAO_ENCONTRADA: 
                return ACHOU_SHINY_NA_HORDA + magikarp # Indica qual é o pokemon da horda que é shiny.
            
            posicaoMagikarp = (posicaoMagikarp[0], posicaoMagikarp[1])
            print ("Posicao Magikarp:", posicaoMagikarp)

            # Verificando se a posição do magikarp já está cadastrada.
            posicaoJaCadastrada = False
            numPosicoes = len(listaPosicoes[magikarp])
            count = 0
            while (not posicaoJaCadastrada) and (count < numPosicoes):    
                posicaoCadastrada = listaPosicoes[magikarp][count]
                print ("Posicao Cadastrada =", posicaoCadastrada)           
                if posicaoMagikarp == posicaoCadastrada:
                    posicaoJaCadastrada = True
                count += 1
            
            if not posicaoJaCadastrada:
                return ACHOU_SHINY_NA_HORDA + magikarp
                '''
                # -------------------------------------------------------------------- #
                #           Parte dedicada para cadastrar novas hordas                 #
                # -------------------------------------------------------------------- #                  
                hordaFile = FILESDIR + "HordaMagikarp" 
                CadastrarPosicaoHorda(hordaFile, posicaoMagikarp, linhaAlvo=magikarp+1)
                listaPosicoes[magikarp].append(posicaoMagikarp)
                #----------------------------------------------------------------------#

                # Alguma posição, de algum pokemon dessa horda, não era conhecida e foi cadastrada.
                situacao = CADASTROU_NOVA_POSICAO
                '''
    return SEM_SHINY

def KillNonShinyHorde(p_Keys, pokemon_position):
    """Mata todos os pokemons da horda que não sejam shinys

    Args:
        p_Keys (list): Lista dos botoes do teclado virtual
        pokemon_position (int): Posicao do pokemon na horda,
            2   3   4
            1       5

    Returns:
        str: ERROR_KILL_POKEMON_HORDE
        str: OK
    """
    p_Right = p_Keys[3]
    p_Down = p_Keys[4]
    p_Z = p_Keys[5]

    toKillList = [1, 2, 3, 4, 5]
    toKillList.remove(pokemon_position)

    for attack in toKillList:
        # Select the main attack
        ClickTecladoVirtual(p_Z, clicks=2)

        # Choose the pokemon
        if attack == 1:
            ClickTecladoVirtual(p_Down)
            ClickTecladoVirtual(p_Z)
        elif attack == 2:
            ClickTecladoVirtual(p_Z)
        elif attack == 3:
            ClickTecladoVirtual(p_Right)
            ClickTecladoVirtual(p_Z)
        elif attack == 4:
            ClickTecladoVirtual(p_Right, clicks=2)
            ClickTecladoVirtual(p_Z)
        elif attack == 5:
            ClickTecladoVirtual(p_Right, clicks=2)
            ClickTecladoVirtual(p_Down)
            ClickTecladoVirtual(p_Z)
        
        time.sleep(8)
        #Verify if the "Lutar" button has appeared. 
        if not CheckPixel("Lutar", tentativas=80):
            print ("ERRO")
            return ERROR_KILL_POKEMON_HORDE
    return OK

def FalseSwipeHorde(p_Keys, pokemon_position, pp=30):
    """Usa False swipe no pokemon restante da horda.

    Args:
        p_Keys (list): Lista dos botoes do teclado virtual
        pokemon_position (int): Posicao do pokemon na horda,
            2   3   4
            1       5
        pp (int, optional): pp do false swipe. Defaults to 30.

    Returns:
        str: VALOR_INVALIDO_PP
        str: ERRO_FALSE_SWIPE
        str: OK
    """
    if pp < 0:
        return VALOR_INVALIDO_PP
    
    p_Right = p_Keys[3]
    p_Z = p_Keys[5]

    # Pixel "Vida" de cada magikarp
    pixelsList = [(631, 172),(631, 132),(891, 132),(1151, 132),(1151, 172)]
    
    # Pixel "Vida" do pokemon shiny
    pixel = pixelsList[pokemon_position - 1]        
    
    lowLife = False
    while not lowLife and pp > 0:
        
        #Verificar se ja carregou o botao "Lutar" da batalha
        if not CheckPixel("Lutar"):
            print ("ERRO_FALSE_SWIPE")
            return ERRO_FALSE_SWIPE

        ClickTecladoVirtual(p_Z)
        ClickTecladoVirtual(p_Right)
        ClickTecladoVirtual(p_Z, clicks=2)
        
        time.sleep(3.2)
        lowLife = CheckPixel("Vida", pixel)
        pp -= 1

    return OK 

def RegisterShiny(filename):
    # Abrindo o arquivo.
    try:
        shinyMagikarpFile = open(filename, "r")
    except:
        # Criando o arquivo, já que o mesmo não existe.
        shinyMagikarpFile = open(filename, "w")
        conteudo = []
    else:
        conteudo = shinyMagikarpFile.readlines()
        shinyMagikarpFile.close()
        shinyMagikarpFile = open(filename, "w")

    conteudo.append(f"Magikarp shiny - {datetime.datetime.now()}\n")    
    shinyMagikarpFile.writelines(conteudo)
    shinyMagikarpFile.close()
    return OK
