from functions.utils.parametros import *
from functions.utils.erros import *
from functions.tela import *
from functions.teclado import Teclado
from functions.verificacao import PosicaoCidadeFly


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

def RunUntilRunHorde():
    '''
    Verifica se está na batalha. Se estiver, usa "Run" até 
    fugir.
    
    Returns:
        str: ERRO_RUN
        str: NAO_ESTA_NA_BATALHA
        str: OK
    '''
    # Verifica se fugiu verificando se a barra do pokemon ainda está lá
    naoFugiu = CheckPixel("hordaApareceu", tentativas=15)

    if not naoFugiu: 
        print("Jogo não está mais na batalha. Provavelmente fugiu antes, mas demorou pra carregar.")            
        return NAO_ESTA_NA_BATALHA
    
    while naoFugiu:
        print("Não fugiu da batalha.")            
        print('Esperando o botão "Lutar" aparecer...')            
        
        # Espera até o botão "Lutar" ficar disponível novamente
        if not CheckPixel("Lutar", tentativas=100):
            print('"Lutar" não apareceu. Pode ser erro (passou pelo teste "hordaApareceu" mas não por esse),')            
            print('ou indicar que na verdade fugiu, conseguiu passar pelo teste "hordaApareceu"')
            print('por isso  passou pela outra verificação')            
            return ERRO_RUN
        
        print('Dando RUN...')            

        # Apertando Run.
        Teclado(t_Right)
        Teclado(t_Down)
        Teclado(t_Z)

        time.sleep(5) # Dando um tempo para ver se vai fugir

        print('Verificando se fugiu com sucesso...')            
        # Verifica se fugiu verificando se a barra do pokemon ainda está lá
        naoFugiu = CheckPixel("hordaApareceu", tentativas=15)
    
    print('Fugiu com sucesso.')            
    return USOU_RUN

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

