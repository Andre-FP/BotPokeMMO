from functions.utils.parametros import *
from functions.utils.erros import *
from functions.teclado import Teclado
from functions.acoes import Fly, ContinuarConversa, EstenderRepel, UsarSurf, UsarWaterFall
from functions.tela import *


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