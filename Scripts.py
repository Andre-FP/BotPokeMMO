from PIL.Image import ENCODERS
from utils.Functions import *

ERRO_PLANTAR_BERRY = "57 - ERRO_PLANTAR_BERRY"
FILES_FOLDERS = os.path.join(os.path.dirname(__file__), "arquivos")
HORDA_FILE = "HordaMagikarp.txt"
FOUND_SHINY_FILE = "FoundShinyMagikarp.txt"
ENCONTERS_FILE = os.path.join(FILES_FOLDERS, "Encounters.txt")

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
        Login("CapturarMagikarp")

    # Verificando a qntd de pokebolas que o personagem tem
    print ("Verificando a quantidade de pokebolas...")
    totalDePokebolas = ChecandoQntdPokebolas()
    if totalDePokebolas == BOLSA_NAO_ABRIU or totalDePokebolas == ABA_NAO_ABRIU:
        return totalDePokebolas
    
    print ("Quantidade:", totalDePokebolas, "pokebolas")
    
    # Verificando a região atual 
    regiao = RegiaoAtual()
    
    # Indo para Kanto, se o personagem não estiver.
    if regiao != "Kanto":
        print ("Mudando para Kanto...")
        erro = TrocarRegiao(regiaoOrigem=regiao, regiaoDestino="Kanto")
        if erro != OK:
            return erro

    print ("Chega antes do while")

    # Entrando em loop até o dinheiro e as pokebolas acabarem.
    while idasAoMercado > 0 or totalDePokebolas > 0:

        print ("Chega depois do while")
        
        #Usar fly para Vermilion
        print ("Usando fly para Vermilion...")
        funcionamento = Fly("Kanto", "Vermilion")
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
            CaminharAtePokeMarket("Vermilion")

            #Entrando e comprando os packs de pokebolas
            print ("Entrando e comprando mais pokebolas...")
            

            funcionamento = Comprar("Pokebola", qntdPack=pack99, regiao="Kanto")
            if funcionamento != OK:
                print ("Erro #", funcionamento, " na função \"Comprar\"", sep="")
                return funcionamento

            # Reduzindo em 1
            idasAoMercado -= 1    

            totalDePokebolas = 99*pack99
            print ("Quantidade:", totalDePokebolas, "pokebolas")
            
            #Voltando pra posição inicial
            print ("Usando fly para Vermilion...")
            funcionamento = Fly("Kanto", "Vermilion")
            if funcionamento != OK:
                print ("Erro na funcao Fly")
                return funcionamento
            print ("Chegou em Vermilion.")
            

        while totalDePokebolas > 0:
            
            #Entra no Centro Pokemon (CP), recupera vida e sai
            print ("Entrando no pokemon e recuperando vida...")
            funcionamento = EntrarUsarESairCP()
            if funcionamento != OK:
                print("Erro na funcao EntrarUsarESairCP")
                return funcionamento
            
            #Andando ateh o mar
            print ("Andando até o mar...")
            Teclado(t_Down, clicks=5, modo="andar")  
            
            pp = 30 
            while pp > 0 and totalDePokebolas > 0:    
            ###### ----------- Pescar ----------- ##########
                
                print("Pescando...")
                funcionamento = Pescar()
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
                    Teclado(t_Right)
                    Teclado(t_Down)
                    Teclado(t_Z)
                    time.sleep(2.0)
                else:
                    # Dar False Swipe ateh a vida ficar minima
                    pp = FalseSwipe(pp)
                    if pp == ERRO_FALSE_SWIPE:
                        print ("Nao foi encontrado o botao Lutar")
                        return ERRO_FALSE_SWIPE
                    
                    print ("PP =", pp)
            
            ################## Capturar o pokemon ####################
                    
                    Capturou = False  
                    # Enquanto o pokemon n for capturado
                    while not Capturou:
                        print ("Lancando pokebola...")
                        
                        acontecimento = LancarPokebola(totalDePokebolas)
                        
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

                    
                    escolha = GuardarOuRelease(situacao, isShiny)

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
                Teclado(t_Up, clicks=2, modo="andar") 
                Teclado(t_Up, clicks=4) 

    return LIMITE_DINHEIRO_ALCANCADO

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

def BotMagikarpShiny(aberto=True, cadastrar=False):
    '''
    Procura um magikarp shiny em Sootopolis, na horda de magikarp, e o captura. 

    Returns:   
        OK
        Muitos outros
    '''

    if not aberto:
        erro = Login("MagikarpShiny")
        if erro != OK:
            return erro
    
    # Verificando a região atual 
    regiao = RegiaoAtual()

    # Indo para Hoenn, se o personagem não estiver.
    if regiao != "Hoenn":
        print ("Mudando para Hoenn...")
        erro = TrocarRegiao(regiaoOrigem=regiao, regiaoDestino="Hoenn")
        if erro != OK:
            return erro

    #Usar fly para Sootopolis
    print ("Usando fly para Sootopolis...")
    funcionamento = Fly("Hoenn", "Sootopolis")
    if funcionamento != OK:
        print ("Erro na funcao Fly")
        return funcionamento

    Teclado(t_X)

    #Entra no Centro Pokemon (CP), recupera vida e sai
    print ("Entrando no CP e recuperando vida...")
    funcionamento = EntrarUsarESairCP("Hoenn")
    if funcionamento != OK:
        print("Erro na funcao EntrarUsarESairCP")
        return funcionamento
    
    # Verificando a qntd de pokebolas que o personagem tem
    print ("Verificando a quantidade de pokebolas...")
    totalDePokebolas = ChecandoQntdPokebolas()
    if totalDePokebolas == BOLSA_NAO_ABRIU or totalDePokebolas == ABA_NAO_ABRIU:
        return totalDePokebolas
    elif totalDePokebolas == 0:
        print("Nenhuma pokebola encontrada. É necessário ao menos")
        print("um pack de pokebolas para rodar esse script.")
        return SEM_PACK_POKEBOLAS
    
    # Adquirindo os dados necessários.
    print (f"Adquirindo dados do arquivo {FILESDIR}{HORDA_FILE}...")
    listaPosicoesPokemon = AdquirirDadosHorda(os.path.join(FILESDIR, HORDA_FILE))
    if listaPosicoesPokemon == ERRO_CRIANDO_ARQUIVO or listaPosicoesPokemon == TUPLA_INVALIDA:
        print ("Erro Adquirindo dados de horda de magikarp")
        return listaPosicoesPokemon

    print ("Lista de posicoes:", listaPosicoesPokemon)
    try:
        with open(ENCONTERS_FILE) as f: 
            encontros = int(f.read())
    except:
        encontros = 0

    while True:
        Teclado(t_Bike)
        time.sleep(0.5)
        Teclado(t_Down, clicks=6, modo="bike")
        Teclado(t_Left, modo="bike", virar=True)
        Teclado(t_Left, clicks=3, modo="bike")
        
        erro = UsarSurf()
        if erro != OK:
            print ("Erro usando Surf")
            return erro
        
        for count in range(6):    
            # Usando sweet scent
            Teclado(t_SweetScent)

            ######### VERIFICA SE USOU SWEET SCENT ########
            if not CheckPixel("balaoChat", tentativas=25):
                
                # Tenta usar de novo
                Teclado(t_SweetScent)
                
                # Se não aparecer de novo, verifica se não conseguiu escapar 
                # da batalha anterior
                if not CheckPixel("balaoChat", tentativas=25):
                    
                    # Se não conseguiu, usa "Run" até conseguir.
                    erro = RunUntilRunHorde()
                    if erro != USOU_RUN:
                        return erro

                    # Usando sweet scent
                    Teclado(t_SweetScent)
                    if not CheckPixel("balaoChat"):
                        return ERRO_SWEET_SCENT
            ###############################################
            
            time.sleep(5)
            
            # Identificando cada magikarp da horda.
            print("cadastrar =", cadastrar)
            reconhecimento = ReconhecerHorda("Magikarp", listaPosicoesPokemon, cadastrar)
            
            # Prosseguindo depois de aparecer o botão de Lutar
            if not CheckPixel("Lutar"):
                return ERRO_RUN

            if reconhecimento == CADASTROU_NOVA_POSICAO:
                print("Nova posição cadastrada.")
                input("Aperte qualquer coisa para continuar...")
                
                # Apertando Run.
                Teclado(t_Right)
                Teclado(t_Down)
                Teclado(t_Z)

            # Se for um pokemon shiny
            elif type(reconhecimento) == int:
                print("Pokemon shiny encontrado!")
                erro = KillNonShinyHorde(reconhecimento)
                if erro != OK:
                    return erro
                erro = FalseSwipeHorde(reconhecimento, pp=30)                    
                if erro != OK:
                    return erro
                confirmacao = POKEMON_NAO_CAPTURADO
                while confirmacao == POKEMON_NAO_CAPTURADO:
                    erro = LancarPokebola(qntdPokebolas=50)
                    if erro != OK:
                        return erro
                    confirmacao = VerificarPokemonCapturado(manter_pokemon=True)
                Teclado(t_ESC)
                RegisterShiny(os.path.join(FILESDIR, FOUND_SHINY_FILE))

            else:
                print("Posicoes ja conhecidas.")
                
                # Apertando Run.
                Teclado(t_Right)
                Teclado(t_Down)
                Teclado(t_Z)
            
            encontros += 1
            with open(ENCONTERS_FILE, "w") as f: 
                f.write(str(encontros))

            print("Encontros:", encontros)
            time.sleep(3)
        #End for

        # Usando teleport
        Teclado(t_Teleport)
        
        # ---------------------------------------------------------------------#
        # Faz uma última verificação se conseguiu dar run na 
        # última batalha. (Esse erro não aconteceria para o caso
        # de captura de shiny, só no caso de "Run")

        ######### VERIFICA SE USOU TELEPORT ########
        if not CheckPixel("balaoChat"):

            # Verifica se não conseguiu escapar da batalha anterior.
            # Se não conseguiu, usa "Run" até tentar.
            erro = RunUntilRunHorde()
            if erro != USOU_RUN:
                return erro

            # Usando teleport
            Teclado(t_Teleport)
        # ---------------------------------------------------------------------#
        time.sleep(2)

        if not CheckPixel("cabeloJoyHoenn", pixel=(986, 349)):
            print ("Personagem não conseguiu utilizar o teleport.")
            return ERRO_TELEPORT

        erro = UsarCPESair(regiao="Hoenn")
        if erro != OK:
            print ("Erro em UsarCPESair")
            return erro