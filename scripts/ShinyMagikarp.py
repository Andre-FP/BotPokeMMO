from functions.utils.parametros import *
from functions.utils.erros import *
from functions.acoes import *
from functions.movimentacao import *
from functions.verificacao import *
from functions.reconhecer_pokemon import *
from functions.atacar_pokemon import *
from functions.capturar import *
from scripts.Login import Login


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
    print (f"Adquirindo dados do arquivo {HORDA_MAGIKARP_FILE}...")
    listaPosicoesPokemon = AdquirirDadosHorda(HORDA_MAGIKARP_FILE)
    if listaPosicoesPokemon == ERRO_CRIANDO_ARQUIVO or listaPosicoesPokemon == TUPLA_INVALIDA:
        print ("Erro Adquirindo dados de horda de magikarp")
        return listaPosicoesPokemon

    print ("Lista de posicoes:", listaPosicoesPokemon)
    try:
        with open(ENCOUNTERS_FILE) as f: 
            encontros = int(f.read())
    except:
        encontros = 0

    while True:
        print("Indo capturar...")
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
            
            # Esperando para ficar mais próximo de carregar a batalha
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
                print("Matando todos os não shinies...")
                # Mata todos os não shinies da horda
                erro = KillNonShinyHorde(reconhecimento)
                if erro != OK:
                    return erro
                
                print("Usando o false swipe no shiny...")
                # Usa false swipe no pokemon shiny até ficar com 1 de vida
                erro = FalseSwipeHorde(reconhecimento, pp=30)                    
                if erro != OK:
                    return erro
                
                # Fica lançando pokebola até capturar. Lança GreatBall 
                # ou UltraBall se a pokebola acabar.
                print("Capturando...")
                confirmacao = POKEMON_NAO_CAPTURADO
                while confirmacao == POKEMON_NAO_CAPTURADO:
                    erro = LancarPokebola(qntdPokebolas=totalDePokebolas)
                    if erro != OK:
                        return erro
                    
                    totalDePokebolas -= 1
                    confirmacao = VerificarPokemonCapturado(manter_pokemon=True)
                
                print("Magikarp Shiny Capturado !!!!!! :DDDDDDDDDD")
                print("Salvando e registrando ele.")
                # Guardando o pokemon e registrando que um shiny foi capturado
                Teclado(t_ESC)
                RegisterShiny(FOUND_SHINY_FILE, encontros)

                # Zerando o número de encontros para recomeçar a contagem
                encontros = 0
                with open(ENCOUNTERS_FILE, "w") as f: 
                    f.write(str(encontros))
                
                # Recomeçar indo pro centro pokemon, para recuperar o PP e vida.
                time.sleep(4) # Esperando sair da batalha
                break 
            
            else:
                print("Posicoes ja conhecidas.")
                print("Usando RUN...")
                
                # Apertando Run.
                Teclado(t_Right)
                Teclado(t_Down)
                Teclado(t_Z)
            
                encontros += 1
                with open(ENCOUNTERS_FILE, "w") as f: 
                    f.write(str(encontros))

                print("Encontros:", encontros)
            
            # Esperando voltar da batalha
            time.sleep(3)

        #End for

        print("Indo para o Centro Pokemon...")
        print("Usando teleport...")
        Teclado(t_Teleport)
        
        # --------------------------------------------------------------------#
        # Faz uma última verificação se conseguiu dar run na 
        # última batalha. (Esse erro não aconteceria para o caso
        # de captura de shiny, só no caso de "Run")

        ######### VERIFICA SE USOU TELEPORT #########
        if not CheckPixel("balaoChat"):

            # Verifica se não conseguiu escapar da batalha anterior.
            # Se não conseguiu, usa "Run" até conseguir.
            RunUntilRunHorde()

            print("Usando Teleport de novo...")

            Teclado(t_Teleport)
            if not CheckPixel("balaoChat"):
                print("Não apareceu o balão do teleport.")
                return ERRO_TELEPORT
        # --------------------------------------------------------------------#
        print("Teleport usado com sucesso.")
        time.sleep(2)

        print("Verificando se chegou no Centro Pokemon...")

        if not CheckPixel("cabeloJoyHoenn", pixel=(986, 349)):
            print ("Personagem não conseguiu utilizar o teleport.")
            return ERRO_TELEPORT
        
        print("Usando o CP e saindo...")

        erro = UsarCPESair(regiao="Hoenn")
        if erro != OK:
            print ("Erro em UsarCPESair")
            return erro