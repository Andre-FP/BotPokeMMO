from functions.utils.parametros import *
from functions.utils.erros import *
from functions.berries import *
from functions.verificacao import *
from Login import Login

def BotCultivarBerry(modo="", berry="CheriBerry", jogo="aberto"):
    '''
    Planta berries em todos os slots do jogo.

    Args: 
        berry(str):
            Berry que deseja plantar
        jogo(str):
            se o jogo tá aberto ou fechado
        modo(str):
            indica o modo da função, se é plantar, regar ou colher.
            Valores válidos para "modo": "plantar", "regar", 
            "colher" e "colherEPlantar".

    Retornos: Um monte.
    '''

    if jogo == "fechado":
        Login("CultivarBerry")
    
    # Verificando a região atual 
    regiao = RegiaoAtual()
    
    # Cultivando em Hoenn
    erro = CultivarBerriesHoenn(regiao, modo=modo)
    if erro != OK:
        print ("Erro na função \"CultivarBerriesHoenn\".")
        return erro
    
    # Mudando para Unova.
    erro = TrocarRegiao(regiaoOrigem="Hoenn", regiaoDestino="Unova", repel="Y")
    if erro != OK:
        return erro
      
    # Cultivando em Unova
    erro = CultivarBerriesUnova(regiaoOrigem="Unova", modo=modo)    
    if erro != OK:
        print ("Erro na função \"CultivarBerriesUnova\".")
        return erro
    
    return OK