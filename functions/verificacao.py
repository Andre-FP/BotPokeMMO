from functions.utils.parametros import *
from functions.utils.erros import *
from functions.tela import *
from functions.teclado import Teclado
import functions.acoes as acoes


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

def EncontrarAbaPokebola(bola="Pokebola"):
    count = 0
    # Se não chegou na aba de pokebolas, da mochila,
    # vai pra direita até encontrar
    while not CheckPixel(bola, tentativas=2) and count < 3:
        Teclado(t_Right)
        count += 1
    
    if count < 3: return OK

    # cont == 3 quer dizer que foi até o final e +1 e não encontrou.
    # Começa a ir pra esquerda pra ver se encontra.
    while not CheckPixel(bola, tentativas=2) and count > 0:
        Teclado(t_Left)
        count -= 1

    if count > 0: return OK

    # cont == 0 quer dizer que foi até o final e -1 e não encontrou.
    return ERRO_FIND_POKEBOLA_TAB

##### PLANTAR BERRIES #####

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
    
    erro = acoes.ContinuarConversa()
    if erro != OK:
        print ("Não chegou no slot")
        return False
    
    if modo == "regar":
        erro = acoes.ContinuarConversa()
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
        erro = acoes.ContinuarConversa()
        if erro != OK:
            print ("Não chegou no slot")
            return False
    

    return True
