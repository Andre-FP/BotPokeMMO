from functions.utils.parametros import *
from functions.utils.erros import *


def PosicaoEDimensaoDaImagem(imagem1=None, imagem2=None, imagem3=None, imagem4=None, espera = 0.0, tentativas=11):
    '''
    O tempo de execucao dessa funcao com o tempo de espera = 0.0 eh de mais ou menos 2.2 segundos usando HD.
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
        pixel = (627, 613)
    
    elif name == "GreatBall":
        corPadrao1 = (56, 143, 246)
        corPadrao2 = (55, 142, 244)
        corPadrao3 = (56, 144, 248)
        pixel = (627, 613)
    
    elif name == "UltraBall":   
        corPadrao1 = (111, 127, 143)
        corPadrao2 = (110, 126, 142)
        corPadrao3 = (112, 128, 144)
        pixel = (627, 613)
    
    elif name == "MasterBall":
        corPadrao1 = (173, 55, 236)
        corPadrao2 = (175, 56, 238)
        corPadrao3 = (176, 56, 240)
        pixel = (627, 613)

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