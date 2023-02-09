from functions.utils.parametros import *
from functions.utils.erros import *
from functions.tela import CheckPixel
from functions.teclado import Teclado


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
    # TODO: Verificar se matou o pokemon atacado.

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