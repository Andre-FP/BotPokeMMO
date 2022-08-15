import datetime
import sys
sys.path.append('..')
from .configuracoesIniciais import *
import keyboard

POSITIONS_HORDE_MOUSE = [(672, 158), (672, 118), (930, 118), (1192, 118), (1192, 155)]
HORDA_FILE = "HordaMagikarp.txt"
FOUND_SHINY_FILE = "FoundShinyMagikarp.txt"

#Teclas
t_Bike = TECLAS["Bike"]
t_Fly = TECLAS["Fly"]
t_Bolsa = TECLAS["Bolsa"]
t_Up = TECLAS["Up"]
t_Left = TECLAS["Left"]
t_Down = TECLAS["Down"]
t_Right = TECLAS["Right"]
t_Z = TECLAS["Z"]
t_X = TECLAS["X"]
t_Regar = TECLAS["Regar"]
t_ESC = TECLAS["ESC"]
t_Pescar = TECLAS["Pescar"]
t_SuperRepel = TECLAS["SuperRepel"]
t_Repel = TECLAS["Repel"]
t_SweetScent = TECLAS["SweetScent"]
t_Teleport = TECLAS["Teleport"]


#ERROS:
CIDADE_NAO_CADASTRADA = "3 - CIDADE_NAO_CADASTRADA"
CIDADE_NAO_ENCONTRADA = "4 - CIDADE_NAO_ENCONTRADA"
REGIAO_NAO_CADASTRADA = "5 - REGIAO_NAO_CADASTRADA"
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
ERRO_RUN = "71 - ERRO_RUN"
NAO_ESTA_NA_BATALHA = "72 - NAO_ESTA_NA_BATALHA"
USOU_RUN = "73 - USOU_RUN"

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
    
    elif name == "fim_conversa_joy":
        corPadrao1 = (0, 0, 0) 
        corPadrao2 = (0, 0, 0) 
        corPadrao3 = (0, 0, 0) 
        pixel = (1237, 160)
    
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

def ChecandoQntdPokebolas():
    '''
    Retorna a quantidade de pokebolas do jogador. Só são considerados packs de 99.

    Argumentos: t_Bolsa -> posicão do botão B do teclado virtual

    Retornos:   BOLSA_NAO_ABRIU
                ABA_NAO_ABRIU
                qntd de pokebolas
                None (nenhuma pokebola)
    '''
    # Abre a bolsa
    Teclado(t_Bolsa)

    # Procura onde esta a aba da pokebola
    posicaoBagPokebola = CentroDaImagem(PosicaoEDimensaoDaImagem("BagOpcaoPokebola1.png", "BagOpcaoPokebola2.png",\
    "BagOpcaoPokebola3.png", tentativas=3))
    if posicaoBagPokebola == IMG_NAO_ENCONTRADA:
        print ("Nao abriu a bolsa. Personagem provavelmente esta numa acao diferente")
        return BOLSA_NAO_ABRIU
    
    # Clica na aba
    pyautogui.moveTo(posicaoBagPokebola)
    pyautogui.click()
    
    # Verifica se a aba abriu
    if not CheckPixel("AbaBagPokebola", pixel=(posicaoBagPokebola[x] - 108, posicaoBagPokebola[y] + 31)):
        print ("Nao abriu a aba de pokebola. Personagem provavelmente esta numa acao diferente")
        return ABA_NAO_ABRIU
    
    # Verifica quantas pokebolas tem e retorna esse numero
    
    imagens = ("Bloco99Pokebola1.png", "Bloco99Pokebola2.png", "Bloco99Pokebola3.png")
    for imagem in imagens:
        lista99Pokebolas = list(pyautogui.locateAllOnScreen(
            os.path.join(IMAGESDIR, "Bloco99Pokebola1.png")
        ))
        
        qntdPackPokebola = len(lista99Pokebolas)
        
        if qntdPackPokebola > 0:
            print ("Lista =", lista99Pokebolas)
            pokebolas = 99*qntdPackPokebola
            # Fecha a bolsa
            Teclado(t_Bolsa)
            return pokebolas
    
    pokebolas = 0
    # Fecha a bolsa
    Teclado(t_Bolsa)        
    return pokebolas

def RegiaoAtual():
    '''
    Retorna a região atual do personagem.

    Argumentos: t_Fly -> Tupla -> posição do botão F2 no teclado virtual

    Retornos:   Regiao (string)
                REGIAO_NAO_CADASTRADA
    '''
    
    Teclado(t_Fly)

    if ImagemEncontrada("RegiaoKanto1.png", "RegiaoKanto2.png", "RegiaoKanto3.png", tentativas=2):
        regiao = "Kanto"

    elif ImagemEncontrada("RegiaoHoenn1.png", "RegiaoHoenn2.png", "RegiaoHoenn3.png", tentativas=1):
        regiao = "Hoenn"

    elif ImagemEncontrada("RegiaoUnova1.png", "RegiaoUnova2.png", "RegiaoUnova3.png", tentativas=1):
        regiao = "Unova"

    else:
        return REGIAO_NAO_CADASTRADA

    time.sleep(0.5)
    return regiao

def Fly(regiao="", cidade=""):
    '''
    Realiza o Fly para uma determinada cidade.

    Args: 
        regiao(str):
            regiao da cidade
        cidade(str):
            cidade desejada

    Returns:   
        CIDADE_NAO_ENCONTRADA
        CIDADE_NAO_CADASTRADA
        REGIAO_NAO_CADASTRADA
        OK
    '''
    if cidade == "":
        print ("Faltando o argumento \"cidade\" na função \"Fly\".")
        return FALTANDO_ARGUMENTOS

    # Se o mapa já não tiver aberto, abre ele.
    if not ImagemEncontrada("TownMap1.png", "TownMap2.png", "TownMap3.png", tentativas=1):
        Teclado(t_Fly)
    
    posicaoCidade = PosicaoCidadeFly(cidade, regiao)
    if posicaoCidade == CIDADE_NAO_ENCONTRADA or posicaoCidade == CIDADE_NAO_CADASTRADA: #Nao foi encontrado o BotaoMapa
        return posicaoCidade

    pyautogui.moveTo(posicaoCidade, duration=0.3)
    
    if regiao == "Unova":
        # Clica mais uma vez.
        pyautogui.click()

    pyautogui.click()
    time.sleep(10.0)
    
    return OK

def EstenderRepel(escolha=""):
    '''
    Estende o uso do repel, ou não.
        
    Args: 
        escolha(str):
            "Y" ou "N" 

    Returns:
        OK
        ERRO_REPEL
        ESCOLHA_INVALIDA
    '''
    if not CheckPixel("Sim"):
        print ("O repel não terminou nesse momento, como deveria.")
        return ERRO_REPEL

    if escolha == "Y":
        Teclado(t_Z)
        
    elif escolha == "N":
        Teclado(t_Down)
        Teclado(t_Z)
    else:
        return ESCOLHA_INVALIDA

    time.sleep(0.2)

    return OK

def TrocarRegiao(regiaoOrigem="", regiaoDestino="", repel="N"):
    '''
    Troca de região para a região de destino.


    Argumentos: 
        regiaOrigem(str): 
            regiao que o personagem está no momento
        regiaoDestino(str): 
        repel(str):
            indica se o personagem está usando repel ou não.
            Valores válidos para "repel": "Y" para "Sim", 
            qualquer outra coisa para "Não".

    Retornos:   
        OK
        MESMA_REGIAO
        REGIAO_DESTINO_INVALIDA
        ERRO_TROCAR_REGIAO
        REGIAO_ORIGEM_INVALIDA
        ERRO_REPEL
    '''

    if regiaoOrigem == regiaoDestino:
        return MESMA_REGIAO

    #### KANTO -> REGIÃO DESTINO ####
    if regiaoOrigem == "Kanto":
        
        # Voando para Vermilion.
        erro = Fly(regiao="Kanto", cidade="Vermilion")
        if erro != OK:
            return erro

        # Caminhando até o porto.
        Teclado(t_Right, clicks=2, modo="andar")
        Teclado(t_Right, clicks=14)
        Teclado(t_Down, clicks=2, modo="andar")
        Teclado(t_Down, clicks=6)
        Teclado(t_Left, clicks=2, modo="andar")
        Teclado(t_Left, clicks=3)
        Teclado(t_Down, clicks=2, modo="andar")
        Teclado(t_Down, clicks=4)
        Teclado(t_Right, clicks=2, modo="andar")
        Teclado(t_Right, clicks=8)
        Teclado(t_Down, clicks=2, modo="andar")
        Teclado(t_Down, clicks=9)
        Teclado(t_Left, clicks=2, modo="andar")
        Teclado(t_Left, clicks=2)
        Teclado(t_Down, clicks=2, modo="andar")
        Teclado(t_Down, clicks=3)

        # Conversando com o cara do porto.
        erro = ContinuarConversa()
        if erro != OK:
            return erro
            
        if not ImagemEncontrada("SelecionarRegiao1.png", "SelecionarRegiao2.png", "SelecionarRegiao3.png"):
            return ERRO_TROCAR_REGIAO
        
        if regiaoDestino == "Hoenn":
            Teclado(t_Z)
        
        elif regiaoDestino == "Sinnoh":
            Teclado(t_Down)
            time.sleep(0.2)
            Teclado(t_Z)

        elif regiaoDestino == "Unova":
            Teclado(t_Down, clicks=2)
            time.sleep(0.2)
            Teclado(t_Z)
        else:
            return REGIAO_DESTINO_INVALIDA

        # Termina a conversa.
        erro = ContinuarConversa()
        if erro != OK:
            return erro

    #### HOENN -> REGIÃO DESTINO ####
    elif regiaoOrigem == "Hoenn":
        
        # Voando para Slateport.
        erro = Fly(regiao="Hoenn", cidade="Slateport")
        if erro != OK:
            return erro

        # Caminhando até o porto.
        Teclado(t_Left, clicks=2, modo="andar")
        Teclado(t_Left, clicks=7)
        Teclado(t_Up, clicks=2, modo="andar")
        Teclado(t_Up, clicks=4)
        Teclado(t_Right, clicks=2, modo="andar")
        Teclado(t_Right)

        if repel == "Y":
            # Verifica se o repel acabou e veio a pergunta de se quer estender com mais um.
            erro = EstenderRepel(escolha="N")
            if erro != OK:
                print ("Erro Função EstenderRepel.")
                return erro

        Teclado(t_Right, clicks=15)
        Teclado(t_Up, clicks=2, modo="andar")
        Teclado(t_Up)
        
        # Entra no Porto.
        Teclado(t_Up)
        
        # Verifica se entrou.
        if not CheckPixel("portoHoenn"):
            return ERRO_TROCAR_REGIAO
        
        # Anda até a mulher.
        Teclado(t_Up, clicks=3)
        Teclado(t_Right, clicks=2, modo="andar")
        Teclado(t_Right, clicks=4)
        Teclado(t_Up)
        time.sleep(0.1)

        # Inicia a conversa.
        Teclado(t_Z)
        
        # Conversando com a mulher do porto.
        erro = ContinuarConversa()
        if erro != OK:
            return erro
        
        if not ImagemEncontrada("SelecionarRegiao1.png", "SelecionarRegiao2.png", "SelecionarRegiao3.png"):
            return ERRO_TROCAR_REGIAO
        
        if regiaoDestino == "Kanto":
            Teclado(t_Z)
        
        elif regiaoDestino == "Sinnoh":
            Teclado(t_Down)
            time.sleep(0.2)
            Teclado(t_Z)

        elif regiaoDestino == "Unova":
            Teclado(t_Down, clicks=2)
            time.sleep(0.2)
            Teclado(t_Z)
        else:
            return REGIAO_DESTINO_INVALIDA

        # Termina a conversa.
        erro = ContinuarConversa()
        if erro != OK:
            return erro

 
    #### UNOVA -> REGIÃO DESTINO ####
    elif regiaoOrigem == "Unova":
        # Voando para Castelia.
        erro = Fly(regiao="Unova", cidade="Castelia")
        if erro != OK:
            return erro
        Teclado(t_Down)
        Teclado(t_Left, clicks=2, modo="andar")
        Teclado(t_Left, clicks=44)
        Teclado(t_Down, clicks=2, modo="andar")
        Teclado(t_Down, clicks=6)
        time.sleep(7)
        Teclado(t_Left, clicks=2, modo="andar")
        Teclado(t_Left, clicks=3)
        Teclado(t_Down, clicks=2, modo="andar")
        Teclado(t_Down, clicks=5)
        Teclado(t_Left, clicks=2, modo="andar")
        time.sleep(0.1)
        
        # Inicia a conversa.
        Teclado(t_Z)

        # Conversando com a mulher do porto.
        erro = ContinuarConversa()
        if erro != OK:
            return erro
            
        if not ImagemEncontrada("SelecionarRegiao1.png", "SelecionarRegiao2.png", "SelecionarRegiao3.png"):
            return ERRO_TROCAR_REGIAO
        
        if regiaoDestino == "Kanto":
            Teclado(t_Z)
        
        elif regiaoDestino == "Hoenn":
            Teclado(t_Down)
            time.sleep(0.2)
            Teclado(t_Z)
        
        elif regiaoDestino == "Sinnoh":
            Teclado(t_Down, clicks=2)
            time.sleep(0.2)
            Teclado(t_Z)

        else:
            return REGIAO_DESTINO_INVALIDA

        # Termina a conversa.
        erro = ContinuarConversa()
        if erro != OK:
            return erro
            
    else:
        return REGIAO_ORIGEM_INVALIDA
    
    # Tempo de espera até chegar na região.
    time.sleep(7)

    return OK
        
def ContinuarConversa(clicks=1):
    '''
    Continua a conversa apertando Z. Essa função NECESSITA de que o fim da mensagem
    seja demarcado por um símbolo de seta para baixo. Se não tiver a seta na mensagem
    essa função NÃO VAI FUNCIONAR.
    
    Args: 
        clicks(int):
            número de cliques.
    
    Returns:   
        OK
        SETA_NAO_ENCONTRADA
    '''
    
    while clicks > 0:

        if not CheckPixel("fimConversa", espera=0.1):
            print ("Erro função ContinuarConversa. A seta não foi encontrada.")
            return SETA_NAO_ENCONTRADA

        time.sleep(0.1)

        Teclado(t_Z, modo="andar")
        clicks -=1
    
    return OK

def EntrarCP(regiao="Kanto"):
    '''
    Entra no centro pokemon e se posiciona em frente a enfermeira Joy.

    Argumentos:
        regiao -> string -> região do CP

    Retornos:   
        OK
        NAO_ENTROU_NO_CP
        PIXEL_NAO_CADASTRADO        
    '''
    Teclado(t_Up, modo="correr", virar=True)
    Teclado(t_Up, modo="correr") #Entrando no CP 
    
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
    Teclado(t_Up, clicks=4, modo="correr") #Andando ateh a Joy 
    time.sleep(0.2)
    
    return OK

def UsarCPESair(regiao="Kanto"):
    '''
    Entra no centro pokemon e se posiciona em frente a enfermeira Joy.

    Args: 
        regiao(str):
            região do CP

    Returns:   
        OK
        PIXEL_NAO_CADASTRADO
        ERRO_CP
    '''
    # Iniciando a conversa.
    Teclado(t_Z) 
    
    # Continuando a conversa.
    erro = ContinuarConversa()
    if erro != OK:
        return erro

    if regiao == "Hoenn":
        # Continuando a conversa.
        erro = ContinuarConversa()
        if erro != OK:
            return erro

    # Selecionando Yes.
    if not CheckPixel("Sim"):
        print ("Não encontrou o botão \"Sim\" para recuperar vida.")
        return ERRO_CP

    Teclado(t_Z) 

    # Terminando a conversa.
    erro = ContinuarConversa(clicks=4)
    if erro != OK:
        return erro

    if not CheckPixel("fim_conversa_joy"):
        print ("Não encerrou a conversa como deveria.")
        return ERRO_CP
    
    time.sleep(0.5)

    # Andando até a porta do CP
    Teclado(t_Down, virar=True, modo="correr")  
    Teclado(t_Down, clicks=4, modo="correr")  
    
    # Verificando regiao e se está tudo OK
    if regiao == "Kanto":
        pixelReferencia = "cabeloJoyKanto"
    
    elif regiao == "Hoenn":
        pixelReferencia = "cabeloJoyHoenn"

    else:
        return PIXEL_NAO_CADASTRADO

    # Verificando se chegou na porta do CP, e andando para baixo
    # caso não tenha chegado
    tentativas = 1
    while not CheckPixel(pixelReferencia):
        print("Não está na porta do CP.")
        tentativas += 1
        if tentativas > 6:
            print ("Personagem entrou no CP mas agora nao estah na posicao de saida como deveria")
            return ERRO_CP
        print("Andando uma casa para baixo")
        Teclado(t_Down, modo="correr")  

    #Sai do CP    
    Teclado(t_Down, clicks=1, modo="correr")  
    time.sleep(2.0)
    return OK

def EntrarUsarESairCP(regiao="Kanto"):
    '''
    Entra, recupera vida no centro pokemon e sai.

    Argumentos: 
        regiao(str):
            região do CP.

    Returns:   
        OK
        NAO_ENTROU_NO_CP
        ERRO_CP
        SETA_NAO_ENCONTRADA
        PIXEL_NAO_CADASTRADO           
    '''
    erro = EntrarCP(regiao)
    if erro != OK:
        print ("Erro entrando no CP.")
        return erro
    
    erro = UsarCPESair(regiao)
    if erro != OK:
        print ("Erro usando o CP.")
        return erro
    
    return OK

def CaminharAtePokeMarket(cidade):
    '''
    Caminha até o Poke Market. 
    Jogador precisa estar na porta do CP do lado de fora, e virado pra fora.

    Args: 
        cidade(str):
            cidade que o personagem se encontra

    Returns:   
        CIDADE_NAO_CADASTRADA
        OK
    '''
    if cidade == "Vermilion":
        Teclado(t_Right, clicks=2, modo="andar")
        Teclado(t_Right, clicks=14)
        Teclado(t_Down, clicks=2, modo="andar")
        Teclado(t_Down, clicks=6)
        Teclado(t_Left, clicks=2, modo="andar")
        Teclado(t_Left, clicks=3)
        Teclado(t_Down, clicks=2, modo="andar")
        Teclado(t_Down, clicks=3)
        Teclado(t_Right, clicks=2, modo="andar")
        Teclado(t_Right, clicks=2)
        # Entra no Poke-Market.
        Teclado(t_Up, clicks=2, modo="andar")

    else:
        print ("Erro função CaminharProMarket: Cidade não cadastrada")
        return CIDADE_NAO_CADASTRADA

    return OK

def Comprar(item, qntdPack=1, regiao="Kanto"):
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
        Teclado(t_Up, clicks=4)
        Teclado(t_Left)
        time.sleep(0.2)
        
        # Iniciando a conversa com ele.
        Teclado(t_Z, modo="andar")
        
        # Continua até aparecer os itens.
        erro = ContinuarConversa()
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
        pyautogui.click()

        #Apertando pra comprar
        posicaoComprar = CentroDaImagem(PosicaoEDimensaoDaImagem("Comprar1.png", "Comprar2.png", "Comprar3.png", 
                                    tentativas=5, espera=0.5))
        
        if posicaoComprar == IMG_NAO_ENCONTRADA: 
            return ERRO_COMPRAR

        pyautogui.moveTo(posicaoComprar)
        
        #Compra a qntd packs
        for count in range (qntdPack):
            #Clica em comprar
            pyautogui.click()
            time.sleep(2.0)
            
            #Clica em Quantidade Max
            pyautogui.moveTo(posicaoQuantiaMax)
            pyautogui.click()
            time.sleep(2.0)

            #Move pro botão comprar
            pyautogui.moveTo(posicaoComprar)

        # Termina a compra
        Teclado(t_ESC)
        time.sleep(0.2)
        
        # Termina a conversa.
        erro = ContinuarConversa()
        if erro != OK:
            return erro

        #Anda até a porta
        Teclado(t_Down, clicks=2, modo="andar")
        Teclado(t_Down, clicks=3)
        if not CheckPixel("cabeloMercador"):
            return ERRO_COMPRAR

        # Sai do mercado
        Teclado(t_Down)
        time.sleep(2.5)

    #end if regiao == "Kanto":
    else:
        return REGIAO_NAO_CADASTRADA

    return OK

def ReconhecerPokemon(pokemon):
    '''
    Começado a batalha, verifica qual é o pokemon encontrado

    Args: 
        pokemon(str):
            deve ser um dos cadastrados
    
    Returns:   
        NOME_NAO_APARECEU
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

def Pescar(): 
    '''
    Executa a função de pescar até achar algum pokemon, ou acontecer algum erro.

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
            Teclado(t_Pescar) # Aperta para pescar
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
                    Teclado(t_Z) #Fecha a mensagem "Landed a Pokemon!" 
                    repetir = False # Encontrou algum pokemon. Sai da função.
                    
                else:
                    naoEncontrouPokemon = CheckPixel("Not even a nibble...")
                    if naoEncontrouPokemon:    
                        Teclado(t_Z) #Fecha a mensagem "Not even a nibble..." 
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

def FalseSwipe(pp):
    '''
    Usa o ataque False swipe até a vida do pokemon ficar mínima

    Args: 
        pp(int):
            quantidade atual de PP
    
    Returns:
        VALOR_INVALIDO_PP
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
        Teclado(t_Z, clicks=2)
        time.sleep(3.2)
        pouca = CheckPixel("Vida")
        pp -= 1

    # TODO: Sugestão: Pode implementar para caso acabe o pp e nao ter deixado a vida pouca, retornar algum outro valor para a main,
    # e a main fazer algo especifico em relacao a isso.
    return pp      

def EncontrarAbaPokebola(bola="Pokebola"):
    count = 0
    # Se não chegou na aba de pokebolas, da mochila,
    # vai pra direita até encontrar
    while not CheckPixel(bola) and count < 4:
        Teclado(t_Right)
        count += 1
    
    if count < 4: return OK

    # cont == 4 quer dizer que foi até o final e +1 e não encontrou.
    # Começa a ir pra esquerda pra ver se encontra.
    while not CheckPixel(bola) and count > 0:
        Teclado(t_Left)
        count -= 1

    if count > 0: return OK

    # cont == 0 quer dizer que foi até o final e -1 e não encontrou.
    return ERRO_FIND_POKEBOLA_TAB


def LancarPokebola(qntdPokebolas):
    '''
    Lança pokebola, ou lança a bola que tiver (sem ser master ball) se as pokebolas
    acabaram durante a batalha.

    Args: 
        qntdPokebolas(int):
            qntd atual de pokebolas

    Returns:   
        OK
        ERRO_LANCAR_POKEBOLA
        SO_TEM_MASTER_BALL
        LANCOU_BOLA_ENCONTRADA    
    '''
    # Verifica se já apareceu o botao "Lutar", indicando que pode lançar a pokebola
    if not CheckPixel("Lutar"):
        return ERRO_LANCAR_POKEBOLA   
    
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
        # TODO: Testar e ver se realmente as pokebolas ficam nessa ordem. 
        #       (premier poderia ficar na frente da great?)
        #
        # Pokebola é verificada para ver se tem pokebolas residuais (< 99)
        outras_bolas = ["Pokebola", "GreatBall", "UltraBall"]
        for bola in outras_bolas:
            encontrou = EncontrarAbaPokebola(bola=bola)
            if encontrou == OK: break

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
                            return SO_TEM_MASTER_BALL

        # Lanca a bola encontrada (pokebola, great ball, ultra ball, ou outra)
        Teclado(t_Z)
        
        return LANCOU_BOLA_ENCONTRADA
    # End if qntdPokebolas <= 0:   

    if not CheckPixel("Pokebola"):
        print("Pokebola nao estah selecionada como planejado.")
        return ERRO_LANCAR_POKEBOLA
    
    # Lança a pokebola
    Teclado(t_Z)
    
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

def Virar(sentido):
    '''
    Vira e anda um passo pro sentido indicado.

    Args: 
        sentido(str):
            para onde o personagem vai virar. Valores válidos para 
            "sentido": "esquerda", "direita", "cima" e "baixo"

    Returns:
        OK
        SENTIDO_INVALIDO
    '''
    if sentido == "esquerda":
        Teclado(t_Left, clicks=2, modo="andar")

    elif sentido == "cima":
        Teclado(t_Up, clicks=2, modo="andar")

    elif sentido == "direita":
        Teclado(t_Right, clicks=2, modo="andar")

    elif sentido == "baixo":
        Teclado(t_Down, clicks=2, modo="andar")

    else:
        print ("Sentido inexistente")
        return SENTIDO_INVALIDO

    return OK

##### PLANTAR BERRIES #####

def PlantarSementesPicantes():
    '''
    Seleciona as sementes de acordo com a semente inserida, e planta elas.

    Args: 
        #TODO semente(str):
            semente desejada

    Returns:   
        OK
        ERRO_PLANTAR_SEMENTES
        SEM_SEMENTE_PICANTE
    ''' 

    if not ImagemEncontrada("PlantarSementes1.png", "PlantarSementes2.png", "PlantarSementes3.png"):
        print ("Aba \"Plantar Sementes\" não abriu.")
        return ERRO_PLANTAR_SEMENTES
    
    # Seleciona o primeiro slot.
    Teclado(t_Z)

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
    pyautogui.click()

    # Clica no segundo Slot
    p_Slot1 = CentroDaImagem(PosicaoEDimensaoDaImagem("Slot1.png", "Slot2.png", "Slot3.png"))
    p_Slot2 = (p_Slot1[x] + 95, p_Slot1[y] - 2) 
    pyautogui.moveTo(p_Slot2)
    pyautogui.click()

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
    pyautogui.click()

    # Clica no terceiro Slot
    p_Slot3 = (p_Slot2[x] + 95, p_Slot2[y] - 2)
    pyautogui.moveTo(p_Slot3)
    pyautogui.click()
    
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
    pyautogui.click()

    # Clicando em "Plantar Sementes".
    if not ImagemEncontrada("CheriBerry1.png", "CheriBerry2.png", "CheriBerry3.png"):
        print ("Após selecionar as sementes, cheri berry não apareceu.")
        return ERRO_PLANTAR_SEMENTES

    p_botaoPlantar = CentroDaImagem(PosicaoEDimensaoDaImagem("BotaoPlantar1.png", "BotaoPlantar2.png", "BotaoPlantar3.png"))
    pyautogui.moveTo(p_botaoPlantar)
    pyautogui.click()

    return OK

def CaminharAteSlotBerry(cidade="", tentativa=1):  
    '''
    Caminha até o primeiro slot de berry de uma das cidades cadastradas.

    Args: 
        cidade(str):
            cidade do slot.

    Returns:   
        OK
        CIDADE_NAO_CADASTRADA
        ERRO_CAMINHAR_ATE_SLOT
    '''
    # Andando até o primeiro slot.
    if cidade == "Rustboro":
        
        Teclado(t_Down, clicks=3)
        Teclado(t_Left, clicks=2, modo="andar")
        Teclado(t_Left)
        Teclado(t_Down, clicks=2, modo="andar")
        Teclado(t_Down, clicks=11)
        Teclado(t_Right, clicks=2, modo="andar")
        Teclado(t_Down, clicks=2, modo="andar")
        
        Teclado(t_Down, clicks=4)
        Teclado(t_Down)
        print ("Tomando cuidado com o bug...")
        time.sleep(6)
        print ("Continuando...")
        Teclado(t_Down, clicks=3)

        Teclado(t_Right, clicks=2, modo="andar")
        Teclado(t_Right, clicks=8)
        Teclado(t_Down, clicks=2, modo="andar")
        Teclado(t_Down, clicks=12)
        Teclado(t_Right, clicks=2, modo="andar")
        Teclado(t_Right, clicks=5)
        Teclado(t_Down, clicks=2, modo="andar")
        Teclado(t_Down, clicks=5)
        Teclado(t_Left, clicks=2, modo="andar")
        Teclado(t_Left, clicks=25)
        time.sleep(0.1)
    
    
    elif cidade == "Fortree":
        
        Teclado(t_Down)
        Teclado(t_Right, clicks=2, modo="andar")
        Teclado(t_Right, clicks=4)
        Teclado(t_Up, clicks=2, modo="andar")
        Teclado(t_Up, clicks=3)
        Teclado(t_Right, clicks=2, modo="andar")
        Teclado(t_Right, clicks=21)
        Teclado(t_Down, clicks=2, modo="andar")
        Teclado(t_Down, clicks=3)
        Teclado(t_Right, clicks=2, modo="andar")
        Teclado(t_Right, clicks=7)

        print ("Tomando cuidado com o bug...")
        time.sleep(4)
        print ("Continuando...")
        
        Teclado(t_Right, clicks=18)
        Teclado(t_Up, clicks=2, modo="andar")
        Teclado(t_Up, clicks=2)
        Teclado(t_Right, clicks=2, modo="andar")
        Teclado(t_Right, clicks=18)
        Teclado(t_Down, clicks=2, modo="andar")
        Teclado(t_Right, clicks=2, modo="andar")
        Teclado(t_Down, clicks=2, modo="andar")
        Teclado(t_Down, clicks=3)

        # Usar Super Repel.
        Teclado(t_SuperRepel)
        time.sleep(4)

        Teclado(t_Left, clicks=2, modo="andar")
        time.sleep(4)
        
        Teclado(t_Down, clicks=2, modo="andar")
        Teclado(t_Down)
        Teclado(t_Left, clicks=2, modo="andar")
        Teclado(t_Down, clicks=2, modo="andar")
        Teclado(t_Left, clicks=2, modo="andar")
        Teclado(t_Left, clicks=2)
        Teclado(t_Down, clicks=2, modo="andar")
        Teclado(t_Down, clicks=3)
        Teclado(t_Left, clicks=2, modo="andar")
        Teclado(t_Down, clicks=2, modo="andar")
        
    
    elif cidade == "Mauville":
        
        Teclado(t_Down, clicks=2)
        Teclado(t_Right, clicks=2, modo="andar")
        Teclado(t_Right, clicks=16)
        
        Teclado(t_Right)
        print ("Tomando cuidado com o bug...")
        time.sleep(4)
        print ("Continuando...")

        Teclado(t_Right, clicks=16)
        Teclado(t_Down, clicks=2, modo="andar")
        Teclado(t_Right, clicks=2, modo="andar")

        # Usa surf.
        erro = UsarSurf()
        if erro != OK:
            print ("Erro na função \"CaminharAteSlotBerry\".")
            return erro

        # Surfando...
        keyboard.press(t_Right)
        time.sleep(5.5)
        keyboard.release(t_Right)
        time.sleep(0.5)

        Teclado(t_Down, clicks=2, modo="andar")
        Teclado(t_Down, clicks=3)
        Teclado(t_Right, clicks=2, modo="andar")
        Teclado(t_Right, clicks=9)
        Teclado(t_Up, clicks=2, modo="andar")
        Teclado(t_Up)
        Teclado(t_Right, clicks=2, modo="andar")
        Teclado(t_Right, clicks=35)
        
        print ("Tomando cuidado com o bug...")
        time.sleep(4)
        print ("Continuando...")

        Teclado(t_Right, clicks=8)
        
        
        Teclado(t_Down, clicks=2, modo="andar")
        Teclado(t_Down, clicks=3)
        Teclado(t_Right, clicks=2, modo="andar")
        Teclado(t_Right, clicks=4)

        # Um cara bloqueando a passagem.
        passou = False
        while not passou:
            # Passando pelo cara bloqueando a passagem.
            Teclado(t_Right)
            # Verificando se o personagem passou dele.
            chatApareceu = False
            tentativa = 1
            maxTentativas = 50
            while not chatApareceu and tentativa < maxTentativas:
                Teclado(t_Z)
                if CheckPixel("fimConversa", espera=0.0, tentativas=1):
                    chatApareceu = True
                tentativa += 1

            if chatApareceu:
                # Fecha a conversa.
                Teclado(t_Z)
                time.sleep(1.5)
            else:
                passou = True
            
        # Continuando o trajeto até o primeiro slot.
        Teclado(t_Right, clicks=6)
        Teclado(t_Up, clicks=2, modo="andar")
        Teclado(t_Up, clicks=4)
        Teclado(t_Left, clicks=2, modo="andar")
        Teclado(t_Left, clicks=6)
        Teclado(t_Up, clicks=2, modo="andar")
        Teclado(t_Up, clicks=5)
        Teclado(t_Left, clicks=2, modo="andar")
        Teclado(t_Left)
        Teclado(t_Up, modo="andar")

    elif cidade == "Mistralton":

        Teclado(t_Left, clicks=2, modo="andar")
        Teclado(t_Left, clicks=3)
        Teclado(t_Up, clicks=2, modo="andar")
        Teclado(t_Up, clicks=7)
        Teclado(t_Left, clicks=2, modo="andar")
        Teclado(t_Left, clicks=32)
        Teclado(t_Down, clicks=2, modo="andar")
        Teclado(t_Down, clicks=33)


    elif cidade == "Undella":
        
        Teclado(t_Left, clicks=2, modo="andar")
        Teclado(t_Left, clicks=6)
        Teclado(t_Down, clicks=2, modo="andar")
        Teclado(t_Down, clicks=9)
        Teclado(t_Left, clicks=2, modo="andar")
        Teclado(t_Left, clicks=30)
        Teclado(t_Down, clicks=2, modo="andar")
        Teclado(t_Down, clicks=7)
        Teclado(t_Right, clicks=2, modo="andar")
        Teclado(t_Right, clicks=24)
        Teclado(t_Down, clicks=2, modo="andar")
        
        print ("Tomando cuidado com o bug...")
        time.sleep(4)
        print ("Continuando...")
        
        Teclado(t_Down, clicks=23)
        Teclado(t_Left, clicks=2, modo="andar")
        Teclado(t_Left, clicks=12)
        Teclado(t_Down, clicks=2, modo="andar")
        Teclado(t_Down, clicks=4)
        Teclado(t_Left, clicks=2, modo="andar")

        # Usa Surf.
        erro = UsarSurf()
        
        if erro != OK:
            # Quer dizer que o npc não chegou na área do surf conforme planejado.
            # Refazendo o processo de caminhada.

            # Voando para Undella.
            erro = Fly(regiao="Unova", cidade="Undella")
            if erro != OK:
                return erro

            tentativa += 1
            if tentativa <= 5:
                erro = CaminharAteSlotBerry(cidade="Undella", tentativa=tentativa)
                return erro

            print ("Personagem não conseguiu chegar na posição do primeiro surf em Undella.")
            return ERRO_CAMINHAR_ATE_SLOT

        time.sleep(2)

        # Usa Super repel.
        Teclado(t_SuperRepel)
        
        # Usa Waterfall.
        erro = UsarWaterFall()
        if erro != OK:
            print ("Erro na função \"CaminharAteSlotBerry\".")
            return erro

        # Surfando...
        keyboard.press(t_Left)
        time.sleep(1.5)
        keyboard.release(t_Left)

        # Usa Waterfall.
        erro = UsarWaterFall()
        if erro != OK:
            print ("Erro na função \"CaminharAteSlotBerry\".")
            return erro

        # Surfando...
        keyboard.press(t_Left)
        time.sleep(2.3)
        keyboard.release(t_Left)

        # Vai pra terra.
        Teclado(t_Down, clicks=2, modo="andar")
        time.sleep(1)

        Teclado(t_Down, clicks=3)
        Teclado(t_Left, clicks=2, modo="andar")
        Teclado(t_Left, clicks=13)
        Teclado(t_Down, clicks=2, modo="andar")
        Teclado(t_Down, clicks=2)
        Teclado(t_Left)

        # Usa Surf.
        erro = UsarSurf()
        if erro != OK:
            print ("Erro na função \"CaminharAteSlotBerry\".")
            return erro

        Teclado(t_Down, clicks=2, modo="andar")

        # Usa Waterfall.
        erro = UsarWaterFall()
        if erro != OK:
            print ("Erro na função \"CaminharAteSlotBerry\".")
            return erro

        # Surfando...
        keyboard.press(t_Down)
        time.sleep(1.0)
        keyboard.release(t_Down)

        Teclado(t_Left, clicks=2, modo="andar")

        # Sai do surf e vai pra esquerda
        keyboard.press(t_Left)
        time.sleep(5)
        keyboard.release(t_Left)
        time.sleep(0.2)
        
        Teclado(t_Up, clicks=2, modo="andar")
        Teclado(t_Up, clicks=4)
        Teclado(t_Right, clicks=2, modo="andar")
        Teclado(t_Up, clicks=2, modo="andar")
        
        # Entrando na floresta.
        Teclado(t_Up)
        time.sleep(4)

        Teclado(t_Up, clicks=6)
        Teclado(t_Left, clicks=2, modo="andar")
        Teclado(t_Up, modo="andar")

    else:
        return CIDADE_NAO_CADASTRADA

    return OK

def PlantarRegarColherNaTiraDeSlots(numSlots, sentido="", posicionamento="", modo=""):
    '''
    Planta Cheri Berry na tira de slot no sentido indicado.

    Argumentos: 
        numSlots(int):
            Obrigatório. Indica quantos slots tem essa tira.
        sentido(str):
            Obrigatório. Indica o sentido de plantio na tira de slots.
        posicionamento(str):
            Obrigatório. Indica o posicionamento do personagem em relação a tira. 
        modo(str):
            indica o modo da função, se é plantar, regar ou colher.

    OBS:
        Valores válidos para "sentido": "baixo", "direita" e "esquerda"
    
        Valores válidos para "posicionamento": "acima" e "abaixo"

        Valores válidos para "modo": "plantar", "regar", "colher" e "colherEPlantar"

    Returns:
        OK
        FALTANDO_ARGUMENTOS 
        POSICIONAMENTO_INVALIDO
        SENTIDO_INVALIDO
        ERRO_PLANTANDO_NA_TIRA_DE_SLOTS                
        MODO_INVALIDO 
        SETA_NAO_ENCONTRADA
        ERRO_REGANDO
    '''
    if sentido == "":
        print ("Erro na função \"PlantandoNaTiraDeSlots\". Faltando argumento \"sentido\".")
        return FALTANDO_ARGUMENTOS

    if modo != "plantar" and modo != "regar" and modo != "colher" and modo != "colherEPlantar":
        print ("Argumento \"modo\" inválido.")
        return MODO_INVALIDO

    #### Verificando o sentido e o posicionamento inserido, para ajustar as variáveis p_Tecla1 e p_Tecla2. ####
    
    if sentido == "baixo":
        p_Tecla1 = t_Down
        p_Tecla2 = t_Left
    
    elif sentido == "direita":
        if posicionamento == "acima":
            p_Tecla1 = t_Right
            p_Tecla2 = t_Down
        
        elif posicionamento == "abaixo":
            p_Tecla1 = t_Right
            p_Tecla2 = t_Up
        
        else:
            print ("Erro na função \"PlantandoNaTiraDeSlots\". Argumento \"posicionamento\" inválido.")
            return POSICIONAMENTO_INVALIDO
    
    elif sentido == "esquerda":
        if posicionamento == "acima":
            p_Tecla1 = t_Left
            p_Tecla2 = t_Down
    
        elif posicionamento == "abaixo":
            p_Tecla1 = t_Left
            p_Tecla2 = t_Up
       
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
                Teclado(t_Z)
                erro = ContinuarConversa()
                if erro != OK:
                    print ("Erro na função \"PlantandoNaTiraDeSlots\"")
                    return erro

                if not CheckPixel("Sim"):
                    print ("Não encontrou o botão \"Sim\" para plantar.")
                    return ERRO_PLANTANDO_NA_TIRA_DE_SLOTS
                
                # Aperta "Sim"
                Teclado(t_Z)

                if modo == "plantar":
                    
                    # Planta a Cheri Berry.
                    print("Plantando no slot...")
                    
                    if ImagemEncontrada("CheriBerry1.png", "CheriBerry2.png", "CheriBerry3.png", tentativas=3): # Se as sementes já estiverem selecionadas.
                        Teclado(t_Z)
                    else:
                        erro = PlantarSementesPicantes()
                        if erro != OK:
                            print ("Erro na função \"PlantandoNaTiraDeSlots\"")
                            return erro

                # Termina a interação.
                erro = ContinuarConversa()
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
                    Teclado(t_Regar)
                    
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
            Teclado(p_Tecla1, clicks=2, modo="andar")
            Teclado(p_Tecla2, modo="andar")

        slot += 1

    return OK

def CultivarBerriesHoenn(regiaoOrigem, modo=""):
    '''
    Plantar, regar ou colher todos os slots de Hoenn.

    Args: 
        regiaoOrigem(str):
            Regiao que o personagem se encontra atualmente.
        modo(str):
            indica o modo da função, se é plantar, regar ou colher.
            Valores válidos para "modo": "plantar", "regar", 
            "colher" e "colherEPlantar".

    Retornos:   
        OK
    '''
    # Indo para Hoenn, se o personagem não estiver.
    if regiaoOrigem != "Hoenn":
        print ("Mudando para Hoenn...")
        erro = TrocarRegiao(regiaoOrigem=regiaoOrigem, regiaoDestino="Hoenn")
        if erro != OK:
            return erro
    
    ################################ PLANTANDO EM RUSTBORO ################################
    
    repetir = True
    while repetir:
        # Voando para Rustboro City.
        print ("Usando Fly para Rustboro City...")
        erro = Fly("Hoenn", cidade="Rustboro")
        if erro != OK:
            return erro
        print ("Chegou em Rustboro.")
    
        # Caminhando até o primeiro slot.
        print ("Caminhando para o primeiro slot...")
        CaminharAteSlotBerry(cidade="Rustboro")
        
        if ChegouNoSlotBerry(modo):
            repetir = False
    
    print ("Plantando...")
    # Plantando na primeira tira

    erro = PlantarRegarColherNaTiraDeSlots(5, sentido="baixo", modo=modo)
    if erro != OK:
        return erro
    
    # Caminhando até a segunda tira.
    Teclado(t_Up, clicks=2, modo="andar")
    Teclado(t_Right, clicks=2, modo="andar")
    Teclado(t_Right, clicks=5)
    Teclado(t_Up, clicks=2, modo="andar")
    Teclado(t_Up, clicks=10)
    

    #Plantando na segunda tira
    erro = PlantarRegarColherNaTiraDeSlots(3, sentido="direita", posicionamento="abaixo", modo=modo)
    if erro != OK:
        return erro
    
    # Caminhando até a terceira tira.
    Teclado(t_Right, clicks=2, modo="andar")
    Teclado(t_Up, clicks=2, modo="andar")
    Teclado(t_Up)
    Teclado(t_Left, clicks=2, modo="andar")
    Teclado(t_Up)
    time.sleep(0.5)
    
    
    # Plantando na terceira tira
    erro = PlantarRegarColherNaTiraDeSlots(3, sentido="esquerda", posicionamento="abaixo", modo=modo)
    if erro != OK:
        return erro
    
    ################################ PLANTANDO EM FORTRESS ################################
    
    tentativa = 1
    while tentativa >= 1:
        
        # Voando para Fortree City.
        print ("Usando Fly para Fortree City...")
        erro = Fly("Hoenn", cidade="Fortree")
        if erro != OK:
            return erro
        print ("Chegou em Fortree.")
        
        time.sleep(2)

        # Caso não tenha chegado no primeiro lote.
        if tentativa > 1:
            
            # Gastando os restante de passos de super repel.
            Virar("direita")
            Teclado(t_Left)
            Virar("baixo")
            Teclado(t_Down, clicks=3)
            Teclado(t_Bike)
                        
            while not CheckPixel("Sim", espera=0.0, tentativas=1):
                keyboard.press(t_Left)
                time.sleep(1)
                keyboard.release(t_Left)
                keyboard.release(t_Right)
                time.sleep(1)
                keyboard.release(t_Right)

            # Clica para não estender.
            Teclado(t_Down)
            Teclado(t_Z)

            # Voando para Fortree City.
            print ("Usando Fly para Fortree City...")
            erro = Fly("Hoenn", cidade="Fortree")
            if erro != OK:
                return erro
            print ("Chegou em Fortree.")
            
            time.sleep(2)


        # Caminhando até o primeiro slot.
        print("Caminhando para o primeiro slot...")
        CaminharAteSlotBerry(cidade="Fortree")
        

        if ChegouNoSlotBerry(modo):
            # Sai do while.
            tentativa = 0
        else:
            tentativa += 1
        


    # Plantando na primeira tira.
    print ("Plantando...")
    erro = PlantarRegarColherNaTiraDeSlots(6, sentido="direita", posicionamento="acima", modo=modo)
    if erro != OK:
        return erro

    Teclado(t_Up, modo="andar")
    
    # Plantando na segunda tira.
    erro = PlantarRegarColherNaTiraDeSlots(4, sentido="esquerda", posicionamento="abaixo", modo=modo)
    if erro != OK:
        return erro
    
    
    ################################ PLANTANDO EM MAUVILLE ################################

    # Voando para Mauville.
    print ("Usando Fly para Mauville City...")
    erro = Fly("Hoenn", cidade="Mauville")
    if erro != OK:
        return erro
    print ("Chegou em Mauville.")
    
    # Caminhando até o primeiro slot.
    print ("Caminhando para o primeiro slot...")
    erro = CaminharAteSlotBerry(cidade="Mauville")
    if erro != OK:
        return erro

    # Plantando nas tiras.
    print ("Plantando...")
    repetir = 0
    while repetir <= 2:
        # Plantando na tira de cima.
        erro = PlantarRegarColherNaTiraDeSlots(2, sentido="direita", posicionamento="abaixo", modo=modo)
        if erro != OK:
            return erro

        Teclado(t_Down)

        # Plantando na tira de baixo.
        erro = PlantarRegarColherNaTiraDeSlots(2, sentido="esquerda", posicionamento="acima", modo=modo)
        if erro != OK:
            return erro

        # Indo pra tira à direita.        
        if repetir <= 1:
            Teclado(t_Right, clicks=2, modo="andar")
            Teclado(t_Right, clicks=2)
            Teclado(t_Up)

        repetir += 1


    return OK

def CultivarBerriesUnova(regiaoOrigem, modo=""):
    '''
    Plantar, regar ou colher todos os slots de Unova.

    Args: 
        regiaoOrigem(str):
            Regiao que o personagem se encontra atualmente.
        modo(str):
            indica o modo da função, se é plantar, regar ou colher.
            Valores válidos para "modo": "plantar", "regar", 
            "colher" e "colherEPlantar".

    Returns:
        OK
        Muitos outros
    '''
    # Indo para Unova, se o personagem não estiver.
    if regiaoOrigem != "Unova":
        print ("Mudando para Unova...")
        
        # Trocando de região.
        erro = TrocarRegiao(regiaoOrigem=regiaoOrigem, regiaoDestino="Unova")
        if erro != OK:
            return erro
    

    ################################ PLANTANDO EM MISTRALTON ################################
    
    repetir = True
    while repetir:    
        # Voando para Mistralton City.
        print ("Usando Fly para Mistralton City...")
        
        erro = Fly("Unova", cidade="Mistralton")
        if erro != OK:
            return erro
        print ("Chegou em Mistralton.")
        
        # Caminhando até o primeiro slot.
        print ("Caminhando para o primeiro slot...")
        CaminharAteSlotBerry(cidade="Mistralton")

        if ChegouNoSlotBerry(modo):
            repetir = False
    
    # Cultivando nos slots.
    print ("Cultivando...")
    repetir = 0
    while repetir <= 2:

        erro = PlantarRegarColherNaTiraDeSlots(6, sentido="direita", posicionamento="acima", modo=modo)
        if erro != OK:
            return erro
                
        Teclado(t_Right, clicks=2, modo="andar")
        Teclado(t_Right, clicks=3)
        Teclado(t_Down, modo="andar")

        erro = PlantarRegarColherNaTiraDeSlots(6, sentido="direita", posicionamento="acima", modo=modo)
        if erro != OK:
            return erro

        Teclado(t_Right, clicks=2, modo="andar")
        Teclado(t_Down, clicks=2, modo="andar")
        Teclado(t_Down, clicks=2)
        Teclado(t_Left, clicks=2, modo="andar")
        Teclado(t_Up, modo="andar")

        erro = PlantarRegarColherNaTiraDeSlots(6, sentido="esquerda", posicionamento="abaixo", modo=modo)
        if erro != OK:
            return erro

        Teclado(t_Left, clicks=2, modo="andar")
        Teclado(t_Left, clicks=3)
        Teclado(t_Up, modo="andar")


        erro = PlantarRegarColherNaTiraDeSlots(6, sentido="esquerda", posicionamento="abaixo", modo=modo)
        if erro != OK:
            return erro

        if repetir <= 1:
            Teclado(t_Down, clicks=2, modo="andar")
            Teclado(t_Down)

        repetir += 1

    
    ################################ PLANTANDO EM UNDELLA ################################
    
    # Voando para Undella Town.
    print ("Usando Fly para Undella Town...")
    
    erro = Fly("Unova", cidade="Undella")
    if erro != OK:
        return erro
    print ("Chegou em Undella.")

    # Caminhando até o primeiro slot.
    print ("Caminhando para o primeiro slot...")
    erro = CaminharAteSlotBerry(cidade="Undella")
    if erro != OK:
        print ("Erro CaminharAteSlotBerry em Undella.")
        return erro
    
    # Cultivando nos slots.
    print ("Cultivando...")
    erro = PlantarRegarColherNaTiraDeSlots(6, sentido="esquerda", posicionamento="abaixo", modo=modo)
    if erro != OK:
        return erro
    
    Teclado(t_Left, clicks=2, modo="andar")
    Teclado(t_Up, clicks=2, modo="andar")
    Teclado(t_Up, clicks=2)
    Teclado(t_Right, clicks=2, modo="andar")
    Teclado(t_Down, modo="andar")

    erro = PlantarRegarColherNaTiraDeSlots(6, sentido="direita", posicionamento="acima", modo=modo)
    if erro != OK:
        return erro

    Teclado(t_Up, clicks=2, modo="andar")
    Teclado(t_Left, clicks=2, modo="andar")
    Teclado(t_Left, clicks=7)
    Teclado(t_Up, clicks=2, modo="andar")
    Teclado(t_Up)
    Teclado(t_Right, clicks=2, modo="andar")
    Teclado(t_Up, clicks=2, modo="andar")
    Teclado(t_Up)
    Teclado(t_Right, clicks=2, modo="andar")
    Teclado(t_Right)
    Teclado(t_Up, modo="andar")

    erro = PlantarRegarColherNaTiraDeSlots(6, sentido="direita", posicionamento="abaixo", modo=modo)
    if erro != OK:
        return erro

    Teclado(t_Right, clicks=2, modo="andar")
    Teclado(t_Up, clicks=2, modo="andar")
    Teclado(t_Up, clicks=2)
    Teclado(t_Left, clicks=2, modo="andar")
    Teclado(t_Down, modo="andar")

    erro = PlantarRegarColherNaTiraDeSlots(6, sentido="esquerda", posicionamento="acima", modo=modo)
    if erro != OK:
        return erro

    Teclado(t_Left, clicks=2, modo="andar")
    Teclado(t_Left, clicks=6)
    Teclado(t_Down, modo="andar")

    erro = PlantarRegarColherNaTiraDeSlots(6, sentido="esquerda", posicionamento="acima", modo=modo)
    if erro != OK:
        return erro

    Teclado(t_Left, clicks=2, modo="andar")
    Teclado(t_Down, clicks=2, modo="andar")
    Teclado(t_Down, clicks=2)
    Teclado(t_Right, clicks=2, modo="andar")
    Teclado(t_Up, modo="andar")

    erro = PlantarRegarColherNaTiraDeSlots(6, sentido="direita", posicionamento="abaixo", modo=modo)
    if erro != OK:
        return erro

    Teclado(t_Left, clicks=2, modo="andar")
    Teclado(t_Left, clicks=5)

    Teclado(t_Down, clicks=2, modo="andar")
    Teclado(t_Down)
    Teclado(t_Left, clicks=2, modo="andar")
    Teclado(t_Left, clicks=10)
    Teclado(t_Down, clicks=2, modo="andar")

    erro = PlantarRegarColherNaTiraDeSlots(6, sentido="esquerda", posicionamento="acima", modo=modo)
    if erro != OK:
        return erro

    Teclado(t_Left, clicks=2, modo="andar")
    Teclado(t_Down, clicks=2, modo="andar")
    Teclado(t_Down, clicks=2)
    Teclado(t_Right, clicks=2, modo="andar")
    Teclado(t_Up, modo="andar")

    erro = PlantarRegarColherNaTiraDeSlots(6, sentido="direita", posicionamento="abaixo", modo=modo)
    if erro != OK:
        return erro

    Teclado(t_Left, clicks=2, modo="andar")
    Teclado(t_Left, clicks=5)
    Teclado(t_Up, clicks=2, modo="andar")
    Teclado(t_Up, clicks=8)

    erro = PlantarRegarColherNaTiraDeSlots(6, sentido="direita", posicionamento="abaixo", modo=modo)
    if erro != OK:
        return erro

    Teclado(t_Right, clicks=2, modo="andar")
    Teclado(t_Up, clicks=2, modo="andar")
    Teclado(t_Up)

    
    # Verifica se o repel acabou e se veio a pergunta de estender com mais um.
    erro = EstenderRepel(escolha="N")

    Teclado(t_Up)
    Teclado(t_Left, clicks=2, modo="andar")
    Teclado(t_Down, modo="andar")

    # Se, na vdd, não foi encontrado a pergunta de estender o repel.
    if erro != OK:
        # Verifica se mesmo assim o personagem chegou no local desejado.
        if not ChegouNoSlotBerry(modo=modo):
            print ("Erro de posição do personagem. Não chegou na parte de estender o repel.")
            return erro

    erro = PlantarRegarColherNaTiraDeSlots(6, sentido="esquerda", posicionamento="acima", modo=modo)
    if erro != OK:
        return erro

    Teclado(t_Left, clicks=2, modo="andar")
    Teclado(t_Left)
    Teclado(t_Up, clicks=2, modo="andar")
    Teclado(t_Up, clicks=3)
    Teclado(t_Right, clicks=2, modo="andar")
    Teclado(t_Right, clicks=2)
    Teclado(t_Up, modo="andar")
    
    erro = PlantarRegarColherNaTiraDeSlots(6, sentido="esquerda", posicionamento="abaixo", modo=modo)
    if erro != OK:
        return erro

    Teclado(t_Left, clicks=2, modo="andar")
    Teclado(t_Up, clicks=2, modo="andar")
    Teclado(t_Up, clicks=2)
    Teclado(t_Right, clicks=2, modo="andar")
    Teclado(t_Down, modo="andar")

    erro = PlantarRegarColherNaTiraDeSlots(6, sentido="direita", posicionamento="acima", modo=modo)
    if erro != OK:
        return erro

    Teclado(t_Right, clicks=2, modo="andar")
    Teclado(t_Down, clicks=2, modo="andar")
    Teclado(t_Down, clicks=2)
    Teclado(t_Right, clicks=2, modo="andar")
    Teclado(t_Right, clicks=3)
    Teclado(t_Up, clicks=2, modo="andar")
    Teclado(t_Right, clicks=2, modo="andar")
    Teclado(t_Up, clicks=2, modo="andar")
    Teclado(t_Up, clicks=12)
    Teclado(t_Right, clicks=2, modo="andar")
    Teclado(t_Right, clicks=5)

    # Usar Repel.
    Teclado(t_Repel)

    # Usa Surf.
    erro = UsarSurf()
    if erro != OK:
        print ("Erro na função \"CaminharAteSlotBerry\".")
        return erro

    # Vai surfando pra direita
    keyboard.release(t_Right)
    time.sleep(3.5)
    keyboard.release(t_Right)
    time.sleep(0.2)

    Teclado(t_Down, clicks=2, modo="andar")
    Teclado(t_Down, clicks=2)
    Teclado(t_Right, clicks=2, modo="andar")
    Teclado(t_Down, modo="andar")

    erro = PlantarRegarColherNaTiraDeSlots(6, sentido="direita", posicionamento="acima", modo=modo)
    if erro != OK:
        return erro

    Teclado(t_Right, clicks=2, modo="andar")
    Teclado(t_Down, clicks=2, modo="andar")
    Teclado(t_Down, clicks=2)
    Teclado(t_Left, clicks=2, modo="andar")
    Teclado(t_Up, modo="andar")

    erro = PlantarRegarColherNaTiraDeSlots(6, sentido="esquerda", posicionamento="abaixo", modo=modo)
    if erro != OK:
        return erro
    

    return OK

def UsarSurf():
    '''
    Usa surf.

    Argumentos: t_Z -> tupla -> posição da tecla Z 
    
    Retornos:   OK
                ERRO_SURF
    '''
    # Aperta Z para surfar.
    time.sleep(0.5)
    Teclado(t_Z)
    
    # Selecionando Yes.
    if not CheckPixel("Sim"):
        print ("Não encontrou o botão \"Sim\" para surfar.")
        return ERRO_SURF
    
    Teclado(t_Z)
    
    # Terminar interação.
    erro = ContinuarConversa()
    if erro != OK:
        print ("Erro na função \"UsarSurf\".")
        return erro

    time.sleep(4)

    return OK

def UsarWaterFall():
    '''
    Usa waterfall.

    Argumentos: t_Z -> tupla -> posição da tecla Z 
    
    Retornos:   OK
                ERRO_WATERFALL
    '''
    # Mesma ideia do surf.
    erro = UsarSurf()
    if erro != OK:
        print ("Erro usando Watterfall.")
        return erro

    time.sleep(1)
    return OK

def ChegouNoSlotBerry(modo):
    '''
    Verifica se o personagem chegou no slot de berry desejado.
    
    Args: 
        modo(str):
            indica o modo da função, se é plantar, regar ou colher.

        OBS:
            Valores válidos para "modo": "plantar", "regar", "colher" e "colherEPlantar"

    Retornos:   True ou False
    
    '''
    # Interagindo com o slot de berry.
    time.sleep(0.5)
    Teclado(t_Z)
    
    erro = ContinuarConversa()
    if erro != OK:
        print ("Não chegou no slot")
        return False
    
    if modo == "regar":
        erro = ContinuarConversa()
        if erro != OK:
            print ("Não chegou no slot")
            return False
        
    if not CheckPixel("Sim"):
        print ("Não chegou no slot")
        return False
    
    # Aperta "Não"
    Teclado(t_Down)
    time.sleep(0.2)
    Teclado(t_Z)
    
    if modo == "colher" or modo == "colherEPlantar":
        erro = ContinuarConversa()
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

    Args:
        string(str):
            string no formato "(a, b)"
    
    Returns:
        tupla
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
    print(pixel)
    return pixel

def AdquirirDadosHorda(nomeArquivo=""):
    '''
    Retorna todas as posições, registradas no arquivo, de cada pokemon da horda.

    Args: 
        nomeArquivo(str):
            nome do arquivo que contém as posições (sem a extensão)

    Returns:
        lista posições para cada pokemon da horda (lista de lista)
        ERRO_CRIANDO_ARQUIVO
        TUPLA_INVALIDA

    '''
    if nomeArquivo == "":
        return FALTANDO_ARGUMENTOS

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
    
    Args: 
        nomeArquivo(str):
            nome do arquivo com os dados já cadastrados da horda (sem o .txt)    
        posicao(tuple):
            posição que deseja cadastrar no arquivo
        linhaAlvo(int):
            numero da linha correspondente ao pokemon (pokemon do lado inferior
            direito, pokemon do lado inferior esquerdo, etc.)
    
    Returns:   
        OK
    '''       
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

# TESTADO !!!!: O QUE IDENTIFICOU O SHINY FOI A POSIÇÃO DO CENTRO DO BALÃO
# MOTIVO: O NOME "shiny magikarp" TEM UM CENTRO DIFERENTE DE "Magikarp", O
#         QUE PROVOCA QUE O BALÃO SE DESLOQUE PARA A ESQUERDA.
#
# OBS: A IMAGEM DO BALÃO SHINY É A ***MESMA*** DO BALÃO DO POKEMON NORMAL.
#      O SCRIPT IDENTIFICOU O BALÃO COMO UM DOS EXISTENTES.
def ReconhecerHorda(pokemonAlvo, listaPosicoes, cadastrar=False):
    '''
    Uma vez usado o sweet scent, reconhece cada pokemon da horda, 
    verificando também se é shiny.
    
    Args:
        pokemonAlvo(str):
            pokemon que o script objetiva
        listaPosicoes(list):
            Lista com 5 elementos. Lista de posicoes de cada 
            pokemon da horda (lista de lista)

    Returns:   
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

    situacao = SEM_SHINY
    if pokemonAlvo == "Magikarp":
        for magikarp in range(5):
            # Colocando o cursor em cima do nome do respectivo magikarp.
            pyautogui.moveTo(POSITIONS_HORDE_MOUSE[magikarp], duration=0.1)
        
            posicaoMagikarp = CentroDaImagem(PosicaoEDimensaoDaImagem("Magikarp1.png", 
                    "Magikarp2.png", "Magikarp3.png", tentativas=2, espera=0.0))
        
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
                if not cadastrar:
                    return ACHOU_SHINY_NA_HORDA + magikarp
                # -------------------------------------------------------------------- #
                #           Parte dedicada para cadastrar novas hordas                 #
                # -------------------------------------------------------------------- #                  
                hordaFile = os.path.join(FILESDIR, HORDA_FILE) 
                CadastrarPosicaoHorda(hordaFile, posicaoMagikarp, linhaAlvo=magikarp+1)
                listaPosicoes[magikarp].append(posicaoMagikarp)
                #----------------------------------------------------------------------#

                # Alguma posição, de algum pokemon dessa horda, não era conhecida e foi cadastrada.
                situacao = CADASTROU_NOVA_POSICAO
                
    return situacao

def KillNonShinyHorde(pokemon_position):
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
    toKillList = [1, 2, 3, 4, 5]
    toKillList.remove(pokemon_position)

    for attack in toKillList:
        # Select the main attack
        Teclado(t_Z, clicks=2)

        # Choose the pokemon
        if attack == 1:
            Teclado(t_Down)
            Teclado(t_Z)
        elif attack == 2:
            Teclado(t_Z)
        elif attack == 3:
            Teclado(t_Right)
            Teclado(t_Z)
        elif attack == 4:
            Teclado(t_Right, clicks=2)
            Teclado(t_Z)
        elif attack == 5:
            Teclado(t_Right, clicks=2)
            Teclado(t_Down)
            Teclado(t_Z)
        
        time.sleep(8)
        #Verify if the "Lutar" button has appeared. 
        if not CheckPixel("Lutar", tentativas=80):
            print ("ERRO")
            return ERROR_KILL_POKEMON_HORDE
    return OK

def FalseSwipeHorde(pokemon_position, pp=30):
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

        # Seleciona o false swipe e clica
        Teclado(t_Z)
        Teclado(t_Right)
        Teclado(t_Z, clicks=2)
        
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

def RunUntilRunHorde():
    '''
    Verifica se está na batalha. Se estiver, usa "Run" até 
    fugir.
    
    Returns:
        str: ERRO_RUN
        str: NAO_ESTA_NA_BATALHA
        str: OK
    '''
    naoFugiu = CheckPixel("hordaApareceu", tentativas=2)
    entrouWhile = False
    while naoFugiu:
        entrouWhile = True
        if not CheckPixel("Lutar"):
            return ERRO_RUN
        
        # Apertando Run.
        Teclado(t_Right)
        Teclado(t_Down)
        Teclado(t_Z)
        
        time.sleep(5)
        naoFugiu = CheckPixel("hordaApareceu", tentativas=2)
    
    if not entrouWhile:
        return NAO_ESTA_NA_BATALHA
    return USOU_RUN