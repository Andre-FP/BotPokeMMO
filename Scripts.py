from utils.Functions import *

ERRO_PLANTAR_BERRY = "57 - ERRO_PLANTAR_BERRY"

def BotCapturarMagikarp(dinheiro, jogo="aberto"):
    
    # Qntd. de packs que da pra comprar
    qntdMaxPacksPokebola = int(dinheiro/19800)
    
    maxCompraPorIda = 3

    comprasDe3Packs = int(qntdMaxPacksPokebola / maxCompraPorIda)
    
    # Essa é a última compra. A quantidade de packs a ser comprada é de acordo com o valor dela. 
    compraResidual = qntdMaxPacksPokebola % maxCompraPorIda
    

    idasAoMercado = comprasDe3Packs
    #Se a divisão não foi exata, então terá uma ida ao mercado para compra residual.
    if compraResidual != 0:
        idasAoMercado += 1


    print ("Máximo de idas ao mercado:", idasAoMercado)    

    ##### INÍCIO DO PROGRAMA #####
    
    pyautogui.FAILSAFE = True
    
    if jogo == "fechado":
        p_Teclas = Login("CapturarMagikarp")
    else:
        p_Teclas = ObterPosicoesTeclas()

    if p_Teclas == TECLA_NAO_ENCONTRADA:
        print ("Erro Login")
        return TECLA_NAO_ENCONTRADA
   
    #Posicoes de cada tecla
    p_Left = p_Teclas[1]          # Recebem (x,y) 
    p_Up = p_Teclas[2]
    p_Right = p_Teclas[3]
    p_Down = p_Teclas[4]
    p_Z = p_Teclas[5]
    p_B = p_Teclas[7]
    p_F2 = p_Teclas[9]
    p_F7 = p_Teclas[12]
    p_ESC = p_Teclas[15]

    # Verificando a qntd de pokebolas que o personagem tem
    print ("Verificando a quantidade de pokebolas...")
    totalDePokebolas = ChecandoQntdPokebolas(p_B)
    if totalDePokebolas == BOLSA_NAO_ABRIU or totalDePokebolas == ABA_NAO_ABRIU:
        return totalDePokebolas
    
    print ("Quantidade:", totalDePokebolas, "pokebolas")
    
    # Verificando a região atual 
    regiao = RegiaoAtual(p_F2)
    
    # Indo para Kanto, se o personagem não estiver.
    if regiao != "Kanto":
        print ("Mudando para Kanto...")
        erro = TrocarRegiao(p_Teclas, regiaoOrigem=regiao, regiaoDestino="Kanto")
        if erro != OK:
            return erro

    print ("Chega antes do while")

    # Entrando em loop até o dinheiro e as pokebolas acabarem.
    while idasAoMercado > 0 or totalDePokebolas > 0:

        print ("Chega depois do while")
        
        #Usar fly para Vermilion
        print ("Usando fly para Vermilion...")
        funcionamento = Fly(p_F2, "Kanto", "Vermilion")
        if funcionamento != OK:
            print ("Erro na funcao Fly")
            return funcionamento
        
        print ("Chegou em Vermilion.")
        
        
        # Quando acabar as pokebolas, comprar mais.
        if totalDePokebolas == 0:
            print ("Acabou as pokebolas.")
            
            pack99 = maxCompraPorIda
            
            if compraResidual > 0 and idasAoMercado == 1:
                # Na última ida, a qntd de packs depende do dinheiro que sobrou.
                pack99 = compraResidual    
            

            #Andando até o Poke Market
            print ("Andando até o Poke Market...")
            CaminharAtePokeMarket("Vermilion", p_Left, p_Up, p_Right, p_Down)

            #Entrando e comprando os packs de pokebolas
            print ("Entrando e comprando mais pokebolas...")
            

            funcionamento = Comprar("Pokebola", p_Left, p_Up, p_Right, p_Down, p_Z, p_ESC, qntdPack=pack99, regiao="Kanto")
            if funcionamento != OK:
                print ("Erro #", funcionamento, " na função \"Comprar\"", sep="")
                return funcionamento

            # Reduzindo em 1
            idasAoMercado -= 1    

            totalDePokebolas = 99*pack99
            print ("Quantidade:", totalDePokebolas, "pokebolas")
            
            #Voltando pra posição inicial
            print ("Usando fly para Vermilion...")
            funcionamento = Fly(p_F2, "Kanto", "Vermilion")
            if funcionamento != OK:
                print ("Erro na funcao Fly")
                return funcionamento
            print ("Chegou em Vermilion.")
            

        while totalDePokebolas > 0:
            
            #Entra no Centro Pokemon (CP), recupera vida e sai
            print ("Entrando no pokemon e recuperando vida...")
            funcionamento = EntrarUsarESairCP(p_Up, p_Z, p_Down)
            if funcionamento != OK:
                print("Erro na funcao EntrarUsarESairCP")
                return funcionamento
            
            #Andando ateh o mar
            print ("Andando até o mar...")
            ClickTecladoVirtual(p_Down, clicks=5, modo="andar")  
            
            pp = 30 
            while pp > 0 and totalDePokebolas > 0:    
            ###### ----------- Pescar ----------- ##########
                
                print("Pescando...")
                funcionamento = Pescar(p_F7, p_Z)
                if funcionamento != OK:
                    print("Personagem nao esta na posicao de pesca")
                    return funcionamento
                
            ########### Verificar qual eh o pokemon encontrado ###########
                isShiny = False
                tryAgain = True
                tentativas = 1
                while tryAgain:
                    tryAgain = False
                    print("Verificando se eh Magikarp...")
                    
                    reconhecimento = ReconhecerPokemon("Magikarp")
                    
                    if reconhecimento == MAGIKARP_ENCONTRADO:
                        print ("Magikarp encontrado.")
                        #Entra no processo de captura
                    
                    elif reconhecimento == MAGIKARP_SHINY:
                        print ("Magikarp encontrado mas sua posicao eh desconhecida. Pode ser um shiny magikarp ou a sua posicao nao foi cadastrada")
                        
                        # Escreve em um arquivo que encontrou um magikarp shiny
                        shinyFoundFile = open("shinyFoundFile.txt", "a")
                        shinyFoundFile.write("M")
                        shinyFoundFile.close()
                        isShiny = True
                        reconhecimento = POKEMON_SHINY

                    elif reconhecimento == ERRO_RECONHECER_POKE:
                        # Programa nao encontrou o botao "Lutar"
                        return ERRO_RECONHECER_POKE
                    
                    elif reconhecimento == NOME_NAO_APARECEU:
                        print ("Nao encontrado o nome do pokemon. Aconteceu algum erro no inicio da batalha\
                            ou o personagem nao esta na acao correta")
                        return NOME_NAO_APARECEU

                    else: #reconhecimento == MAGIKARP_NAO_ENCONTRADO:
                        print ("Nao eh um Magikarp.")
                        print ("Verificando se eh Tentacool...")
                        
                        reconhecimento = ReconhecerPokemon("Tentacool")
                        if reconhecimento == TENTACOOL_ENCONTRADO:
                            print ("Tentacool encontrado")
                            #Vai fugir da batalha.
                        
                        elif reconhecimento == TENTACOOL_SHINY:
                            print ("Tentacool encontrado mas sua posicao eh desconhecida. Pode ser um shiny tentacool ou a sua posicao nao foi cadastrada")
                            
                            # Escreve em um arquivo que encontrou um tentacool shiny 
                            shinyFoundFile = open("shinyFoundFile.txt", "a")
                            shinyFoundFile.write("T")
                            shinyFoundFile.close()
                            isShiny = True
                            reconhecimento = POKEMON_SHINY
                        
                        elif reconhecimento == ERRO_RECONHECER_POKE:
                        # Programa nao encontrou o botao "Lutar"
                            return ERRO_RECONHECER_POKE

                        else: #reconhecimento == TENTACOOL_NAO_ENCONTRADO:
                            print ("Também não é um Tentacool.") 
                            
                            if tentativas == 1:
                                print ("Tentando de novo...")
                                tentativas += 1
                                pyautogui.moveTo(350, 200, duration=1.5)
                                tryAgain = True
                                # Volta pro "while tryagain:"                             
                            
                            else:
                                print ("Sendo assim, eh algum pokemon shiny (magikarp ou tentacool), ou a imagem desse pokemon nao foi cadastrada")
                                
                                # Escreve em um arquivo que encontrou um shiny 
                                shinyFoundFile = open("shinyFoundFile.txt", "a")
                                shinyFoundFile.write("1")
                                shinyFoundFile.close()
                                isShiny = True
                                reconhecimento = POKEMON_SHINY
                    
            ################# Dentro da Batalha ##################
                
                if reconhecimento == TENTACOOL_ENCONTRADO:
                    # Apertar Run
                    print ("Fugindo...")
                    ClickTecladoVirtual(p_Right)
                    ClickTecladoVirtual(p_Down)
                    ClickTecladoVirtual(p_Z)
                    time.sleep(2.0)
                else:
                    # Dar False Swipe ateh a vida ficar minima
                    pp = FalseSwipe(p_Z, pp)
                    if pp == ERRO_FALSE_SWIPE:
                        print ("Nao foi encontrado o botao Lutar")
                        return ERRO_FALSE_SWIPE
                    
                    print ("PP =", pp)
            
            ################## Capturar o pokemon ####################
                    
                    Capturou = False  
                    # Enquanto o pokemon n for capturado
                    while not Capturou:
                        print ("Lancando pokebola...")
                        
                        acontecimento = LancarPokebola(p_Teclas, totalDePokebolas)
                        
                        if acontecimento == ERRO_LANCAR_POKEBOLA:
                            return ERRO_LANCAR_POKEBOLA
                        
                        elif acontecimento == SO_TEM_MASTER_BALL:
                            # TODO: Verificar se é um pokemon shiny e se for, lançar a master ball mesmo
                            return SO_TEM_MASTER_BALL

                        totalDePokebolas -= 1

                        # Checkando se o pokemon foi capturado. Se foi, checa seus status
                        situacao = VerificarPokemonCapturado()
                        if situacao != POKEMON_NAO_CAPTURADO:
                            Capturou = True                            
                        
                    print ("Pokemon capturado")                    
            
            ################## Guardando ou jogando fora #####################

                    
                    escolha = GuardarOuRelease(situacao, p_ESC, isShiny)

                    if escolha == POKEMON_GUARDADO:
                        print ("Pokemon guardado.")
                    
                    elif escolha == POKEMON_RELEASED:
                        print ("Pokemon jogado fora.")
                    
                    else:
                        print ("Erro #", situacao, ". Passou pela \"GuardarOuRelease\", mas seu argumento \"situacao\" ja estava invalido")
                        return ERRO_VERIFICAR_POKE
                    
                    #Volta pro "while pp > 0:", reiniciando o processo na parte da pesca 
                    #ateh o PP do false swipe acabar
                        
            
            #Fim do PP ou acabou as pokebolas
            
            
            if pp == 0:
                #Andando ate o CP
                ClickTecladoVirtual(p_Up, clicks=2, modo="instantaneo") 
                ClickTecladoVirtual(p_Up, clicks=4) 

    return LIMITE_DINHEIRO_ALCANCADO

def BotCultivarBerry(modo="", berry="CheriBerry", jogo="aberto"):
    '''
    Planta berries em todos os slots do jogo.

    Argumentos: berry -> string -> Berry que deseja plantar
                jogo -> string -> se o jogo tá aberto ou fechado
                modo -> string -> indica o modo da função, se é plantar, regar ou colher.

        OBS:
            Valores válidos para "modo": "plantar", "regar", "colher" e "colherEPlantar"

    Retornos: Um monte.
    '''

    if jogo == "fechado":
        p_Teclas = Login("CultivarBerry")
    else:
        p_Teclas = ObterPosicoesTeclas()
    
    if p_Teclas == TECLA_NAO_ENCONTRADA:
        print ("Erro Login")
        return TECLA_NAO_ENCONTRADA
   
    #Posicoes de cada tecla
    p_Left = p_Teclas[1]          # Recebem (x,y) 
    p_Up = p_Teclas[2]
    p_Right = p_Teclas[3]
    p_Down = p_Teclas[4]
    p_Z = p_Teclas[5]
    p_B = p_Teclas[7]
    p_F1 = p_Teclas[8]
    p_F2 = p_Teclas[9]
    p_F5 = p_Teclas[10]
    p_F6 = p_Teclas[11]
    p_F7 = p_Teclas[12]
    p_ESC = p_Teclas[15]
    p_A = p_Teclas[16]

    
    # Verificando a região atual 
    regiao = RegiaoAtual(p_F2)
    
    # Cultivando em Hoenn
    erro = CultivarBerriesHoenn(p_Teclas, regiao, modo=modo)
    if erro != OK:
        print ("Erro na função \"CultivarBerriesHoenn\".")
        return erro
    

    # Mudando para Unova.
    erro = TrocarRegiao(p_Teclas, regiaoOrigem="Hoenn", regiaoDestino="Unova", repel="Y")
    if erro != OK:
        return erro
      
    
    # Cultivando em Unova
    erro = CultivarBerriesUnova(p_Teclas, regiaoOrigem="Unova", modo=modo)    
    if erro != OK:
        print ("Erro na função \"CultivarBerriesUnova\".")
        return erro
    
    return OK

def BotMagikarpShiny(jogo="aberto"):
    '''
    Procura um magikarp shiny em Sootopolis, na horda de magikarp, e o captura. 
    
    Argumentos: Nenhum

    Retornos:   OK
                Muitos outros
    '''

    if jogo == "fechado":
        p_Teclas = Login("MagikarpShiny")
    else:
        p_Teclas = ObterPosicoesTeclas()
    
    if p_Teclas == TECLA_NAO_ENCONTRADA:
        print ("Erro Login")
        return TECLA_NAO_ENCONTRADA
   
    #Posicoes de cada tecla
    p_Left = p_Teclas[1]          # Recebem (x,y) 
    p_Up = p_Teclas[2]
    p_Right = p_Teclas[3]
    p_Down = p_Teclas[4]
    p_Z = p_Teclas[5]
    p_B = p_Teclas[7]
    p_F1 = p_Teclas[8]
    p_F2 = p_Teclas[9]
    p_F5 = p_Teclas[10]
    p_F6 = p_Teclas[11]
    p_F7 = p_Teclas[12]
    p_F8 = p_Teclas[13]
    p_F9 = p_Teclas[14]
    p_ESC = p_Teclas[15]
    p_A = p_Teclas[16]

    # Verificando a região atual 
    regiao = RegiaoAtual(p_F2)

    # Indo para Hoenn, se o personagem não estiver.
    if regiao != "Hoenn":
        print ("Mudando para Hoenn...")
        erro = TrocarRegiao(p_Teclas, regiaoOrigem=regiao, regiaoDestino="Hoenn")
        if erro != OK:
            return erro

    #Usar fly para Sootopolis
    print ("Usando fly para Sootopolis...")
    funcionamento = Fly(p_F2, "Hoenn", "Sootopolis")
    if funcionamento != OK:
        print ("Erro na funcao Fly")
        return funcionamento

    #Entra no Centro Pokemon (CP), recupera vida e sai
    print ("Entrando no CP e recuperando vida...")
    funcionamento = EntrarUsarESairCP(p_Up, p_Z, p_Down, "Hoenn")
    if funcionamento != OK:
        print("Erro na funcao EntrarUsarESairCP")
        return funcionamento
    
    # Verificando a qntd de pokebolas que o personagem tem
    print ("Verificando a quantidade de pokebolas...")
    totalDePokebolas = ChecandoQntdPokebolas(p_B)
    if totalDePokebolas == BOLSA_NAO_ABRIU or totalDePokebolas == ABA_NAO_ABRIU:
        return totalDePokebolas
    elif totalDePokebolas == 0:
        print("Nenhuma pokebola encontrada. É necessário ao menos")
        print("um pack de pokebolas para rodar esse script.")
        return SEM_PACK_POKEBOLAS

    # Adquirindo os dados necessários.
    print (f"Adquirindo dados do arquivo {FILESDIR}HordaMagikarp.txt...")
    listaPosicoesPokemon = AdquirirDadosHorda(FILESDIR + "HordaMagikarp")
    if listaPosicoesPokemon == ERRO_CRIANDO_ARQUIVO or listaPosicoesPokemon == TUPLA_INVALIDA:
        print ("Erro Adquirindo dados de horda de magikarp")
        return listaPosicoesPokemon

    print ("Lista de posicoes:", listaPosicoesPokemon)
    
    while True:
        ClickTecladoVirtual(p_Down, clicks=6)
        Virar("esquerda", p_Teclas) 
        ClickTecladoVirtual(p_Left, clicks=2)
        
        erro = UsarSurf(p_Z)
        if erro != OK:
            print ("Erro usando Surf")
            return erro
        
        for count in range(6):    
            # Usando sweet scent
            ClickTecladoVirtual(p_F8)
            
            if not CheckPixel("balaoChat"):
                print ("Não foi usado sweet scent.")
                return ERRO_SWEET_SCENT

            time.sleep(5)
            
            # Identificando cada magikarp da horda.
            reconhecimento = ReconhecerHorda("Magikarp", listaPosicoesPokemon)
            
            if reconhecimento == CADASTROU_NOVA_POSICAO:
                print("Nova posição cadastrada.")
                input("Aperte qualquer coisa para continuar...")
            
            # Se for um pokemon shiny
            elif type(reconhecimento) == int:
                print("Pokemon shiny encontrado!")
                erro = KillNonShinyHorde(p_Teclas, reconhecimento)
                if erro != OK:
                    return erro
                erro = FalseSwipeHorde(p_Teclas, reconhecimento, pp=30)                    
                if erro != OK:
                    return erro
                confirmacao = POKEMON_NAO_CAPTURADO
                while confirmacao == POKEMON_NAO_CAPTURADO:
                    erro = LancarPokebola(p_Teclas, qntdPokebolas=50)
                    if erro != OK:
                        return erro
                    confirmacao = VerificarPokemonCapturado(manter_pokemon=True)
                ClickTecladoVirtual(p_ESC)
                RegisterShiny(FILESDIR + "FoundShinyMagikarp.txt")

            else:
                print("Posicoes ja conhecidas.")

                # Apertando Run.
                ClickTecladoVirtual(p_Right)
                ClickTecladoVirtual(p_Down)
                ClickTecladoVirtual(p_Z)
            time.sleep(3)
        #End for

        # Usando teleport
        ClickTecladoVirtual(p_F9)
        time.sleep(2)

        if not CheckPixel("cabeloJoyHoenn", pixel=(986, 349)):
            print ("Personagem não conseguiu utilizar o teleport.")
            return ERRO_TELEPORT

        erro = UsarCPESair(p_Z, p_Down, regiao="Hoenn")
        if erro != OK:
            print ("Erro em UsarCPESair")
            return erro
    
BotMagikarpShiny("aberto")