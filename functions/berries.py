from functions.acoes import Fly, UsarSurf, ContinuarConversa, EstenderRepel
from functions.movimentacao import CaminharAteSlotBerry, TrocarRegiao, Virar
from functions.tela import *
from functions.teclado import Teclado
from functions.verificacao import ChegouNoSlotBerry


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
