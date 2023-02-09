from functions.utils.parametros import *
from functions.utils.erros import *
from functions.utils.utils import StringTuplaParaTupla
from functions.tela import CentroDaImagem, PosicaoEDimensaoDaImagem, CheckPixel
import datetime



def ReconhecerPokemon(pokemon):
    '''
    Começado a batalha, verifica qual é o pokemon encontrado

    Args: 
        pokemon(str):
            deve ser um dos cadastrados
    
    Returns:   
        NOME_NAO_APARECEU
        ERRO_RECONHECER_POKE
        MAGIKARP_NAO_ENCONTRADO
        MAGIKARP_ENCONTRADO
        MAGIKARP_SHINY
        TENTACOOL_NAO_ENCONTRADO
        TENTACOOL_ENCONTRADO
        TENTACOOL_SHINY
        POKEMON_NAO_REGISTRADO

    '''
    # Verifica se o nome do pokemon já apareceu 
    if not CheckPixel("NomeDoPokemon"):
        print ("Nao apareceu o nome do pokemon. Provavelmente estah numa acao diferente")
        return NOME_NAO_APARECEU 
    
    if pokemon == "Magikarp":
        
        # USAR ESSE PEDACO DE CODIGO QND TIVER ANALISANDO O POKEMON QUE VC QUER CAPTURAR,
        # visto que ele será analisado primeiro.
        pyautogui.moveTo(370, 166, duration=0.3)
        

        posicaoMagikarp = CentroDaImagem(PosicaoEDimensaoDaImagem("MagikarpChuva1.png", "Magikarp2.png", "MagikarpChuva2.png", 
        "MagikarpChuva2Nivel10.png", tentativas=2, espera=0.5))
        print ("Posicao Magikarp = ", posicaoMagikarp) 
        ''' 
        #1 - Level10: (396, 139) , (396, 138) , 
        #2 - <level10: (389, 139) , #3 (389, 138) , #4 (390, 138)
        
        '''
        if posicaoMagikarp == IMG_NAO_ENCONTRADA: # Imagem nao foi reconhecida. Nao eh magikarp ou nao foi reconhecido. Pode ser um shiny ou n.
            return MAGIKARP_NAO_ENCONTRADO 
        
        else: # Magikarp encontrado. Falta saber se eh shiny ou n. 
            if posicaoMagikarp == (396, 139) or posicaoMagikarp == (396, 138) or posicaoMagikarp == (389, 139) or \
                posicaoMagikarp == (389, 138) or posicaoMagikarp == (390, 138) or posicaoMagikarp == (383, 139) or\
                posicaoMagikarp == (383, 138) or posicaoMagikarp == (391, 138) or posicaoMagikarp == (391, 139):
                
                #Magikarp encontrado mas n eh shiny
                
                #Verificar se ja carregou o botao "Lutar" da batalha
                if not CheckPixel("Lutar", tentativas=150):
                    print ("Nao apareceu o botao \"Lutar\". O programa provavelmente estah numa acao diferente")
                    return ERRO_RECONHECER_POKE   #-2
                
                return MAGIKARP_ENCONTRADO
            
            else: # Eh Magikarp mas a posicao nao eh esperada. Pode ser um shiny ou n.
                return MAGIKARP_SHINY #-1

    elif pokemon == "Tentacool":
        posicaoTentacool = CentroDaImagem(PosicaoEDimensaoDaImagem("TentacoolChuva1.png", "TentacoolChuva2.png",
        "TentacoolChuva3.png", tentativas=3))
        print ("Posicao Tentacool = ", posicaoTentacool) 
        '''
        # 1 - (392, 168) 
        # 2 - (393, 137) 
        # 3 - (392, 138) 
        # 4 - (400, 138)
        # 5 - (401, 137)
        '''
        if posicaoTentacool == IMG_NAO_ENCONTRADA: # Imagem nao foi reconhecida. Nao eh tentacool ou a imagem nao foi reconhecida. 
            return TENTACOOL_NAO_ENCONTRADO #1                               # Pode ser um shiny ou n.
            
        else:    
            if posicaoTentacool == (392, 168) or posicaoTentacool == (393, 137) or posicaoTentacool == (392, 138) or\
                posicaoTentacool == (400, 138) or posicaoTentacool == (401, 137) or posicaoTentacool == (387, 138) or\
                posicaoTentacool == (394, 138) or posicaoTentacool == (388, 137) or posicaoTentacool == (395, 137):
                
                #Tentacool encontrado mas n eh shiny
                
                #Verifica se ja carregou o botao "Lutar" da batalha e espera um determinado tempo para ver se aparece
                if not CheckPixel("Lutar", tentativas=150):
                    print ("Nao apareceu o botao \"Lutar\". O programa provavelmente estah numa acao diferente")
                    return ERRO_RECONHECER_POKE
                
                return TENTACOOL_ENCONTRADO
            
            else: # Eh Tentacool mas a posicao nao eh esperada. Pode ser um shiny ou n.
                return TENTACOOL_SHINY
    else:
        print("Pokemon ainda nao implementado")
        return POKEMON_NAO_REGISTRADO

################## RECONHECIMENTO EM HORDA ##################

def AdquirirDadosHorda(nomeArquivo=""):
    '''
    Retorna todas as posições, registradas no arquivo, de cada pokemon da horda.

    Args: 
        nomeArquivo(str):
            nome do arquivo que contém as posições (sem a extensão)

    Returns:
        lista posições para cada pokemon da horda (lista de lista)
        ERRO_CRIANDO_ARQUIVO
        TUPLA_INVALIDA

    '''
    if nomeArquivo == "":
        return FALTANDO_ARGUMENTOS

    try:
        hordaFile = open(nomeArquivo, "r")
    except:
        print ("Criando o arquivo...")    
        try:
            hordaFile = open(nomeArquivo, "w")
        except:
            return ERRO_CRIANDO_ARQUIVO
        listaDados = []
        linhasHordaFile = []
    else:
        print ("Arquivo já existia.")

        linhasHordaFile = hordaFile.readlines()
        hordaFile.close()
        listaDados = []
        if len(linhasHordaFile) != 0:
            for linha in linhasHordaFile: 
                listaPosicoes = []
                if len(linha) != 0:
                    if linha[0] != '\n':
                        listaPosicaoString = linha.split(';')
                        print(listaPosicaoString)
                        for posicaoString in listaPosicaoString:
                            posicao = StringTuplaParaTupla(posicaoString)
                            if posicao == TUPLA_INVALIDA:
                                print ("Arquivo não contém tuplas válidas.")
                                return TUPLA_INVALIDA
                            listaPosicoes.append(posicao)
                listaDados.append(listaPosicoes)
    # end else
    qntdDados = len(linhasHordaFile)
    qntdRestanteDados = 5 - qntdDados
    while qntdRestanteDados > 0:
        listaDados.append([])
        qntdRestanteDados -= 1

    return listaDados

def CadastrarPosicaoHorda(nomeArquivo, posicao, linhaAlvo):
    '''
    Cadastra a posição desejada no arquivo da horda. O arquivo da horda tem que estar correto,
    pois essa função não consegue identificar erros.
    
    Args: 
        nomeArquivo(str):
            nome do arquivo com os dados já cadastrados da horda (sem o .txt)    
        posicao(tuple):
            posição que deseja cadastrar no arquivo
        linhaAlvo(int):
            numero da linha correspondente ao pokemon (pokemon do lado inferior
            direito, pokemon do lado inferior esquerdo, etc.)
    
    Returns:   
        OK
    '''       
    # Abrindo o arquivo.
    try:
        hordaMagikarpFile = open(nomeArquivo, "r")
    except:
        # Criando o arquivo, já que o mesmo não existe.
        hordaMagikarpFile = open(nomeArquivo, "w")
        conteudo = []
    else:
        conteudo = hordaMagikarpFile.readlines()
    
    hordaMagikarpFile.close()
    num_linhas = len(conteudo)
    
    # Se a linha não existir ainda no arquivo, vai criando as linhas até chegar na desejada.
    print ("O que está no arquivo:", conteudo)
    
    if linhaAlvo > num_linhas:
        for aux in range(num_linhas, linhaAlvo):
            if aux == 4:
                conteudo.append('')
            else:
                conteudo.append("\n")

    print ("Antes de insert:", conteudo)

    # Adiciona a posição no início da linha desejada.
    if len(conteudo[linhaAlvo - 1]) == 0:
        conteudo.insert(linhaAlvo - 1, str(posicao))
    elif conteudo[linhaAlvo - 1][0] == '\n':
        conteudo.insert(linhaAlvo - 1, str(posicao))
    else:
        conteudo.insert(linhaAlvo - 1, str(posicao) + ';')

    # Atualiza o arquivo.
    hordaMagikarpFile = open(nomeArquivo, "w")
    print ("Depois de insert:", conteudo)
    hordaMagikarpFile.writelines(conteudo)
    hordaMagikarpFile.close()
    return OK

# TESTADO !!!!: O QUE IDENTIFICOU O SHINY FOI A POSIÇÃO DO CENTRO DO BALÃO
# MOTIVO: O NOME "shiny magikarp" TEM UM CENTRO DIFERENTE DE "Magikarp", O
#         QUE PROVOCA QUE O BALÃO SE DESLOQUE PARA A ESQUERDA.
#
# OBS: A IMAGEM DO BALÃO SHINY É A ***MESMA*** DO BALÃO DO POKEMON NORMAL.
#      O SCRIPT IDENTIFICOU O BALÃO COMO UM DOS EXISTENTES.
def ReconhecerHorda(pokemonAlvo, listaPosicoes, cadastrar=False):
    '''
    Uma vez usado o sweet scent, reconhece cada pokemon da horda, 
    verificando também se é shiny.
    
    Args:
        pokemonAlvo(str):
            pokemon que o script objetiva
        listaPosicoes(list):
            Lista com 5 elementos. Lista de posicoes de cada 
            pokemon da horda (lista de lista)

    Returns:   
        CADASTROU_NOVA_POSICAO
        ACHOU_SHINY_NA_HORDA + int
        SEM_SHINY
        Erros:
            HORDA_NAO_APARECEU
            LISTA_INVALIDA
    '''
    if len(listaPosicoes) != 5:
        print ("Lista de posições, da horda, inválida.")
        return LISTA_INVALIDA

    print ("Lista posições =", listaPosicoes)

    # Verifica se os pokemons já apareceram.
    if not CheckPixel("hordaApareceu"):
        print ("Nao apareceu o nome do pokemon. Provavelmente estah numa acao diferente")
        return HORDA_NAO_APARECEU 

    situacao = SEM_SHINY
    if pokemonAlvo == "Magikarp":
        for magikarp in range(5):
            # Colocando o cursor em cima do nome do respectivo magikarp.
            pyautogui.moveTo(POSITIONS_HORDE_MOUSE[magikarp], duration=0.1)
        
            posicaoMagikarp = CentroDaImagem(PosicaoEDimensaoDaImagem("Magikarp1.png", 
                    "Magikarp2.png", "Magikarp3.png", tentativas=2, espera=0.0))
        
            # Imagem nao foi reconhecida. Nao eh magikarp ou nao foi reconhecido. Pode ser um shiny ou n.
            if posicaoMagikarp == IMG_NAO_ENCONTRADA: 
                return ACHOU_SHINY_NA_HORDA + magikarp # Indica qual é o pokemon da horda que é shiny.
            
            posicaoMagikarp = (posicaoMagikarp[0], posicaoMagikarp[1])
            print ("Posicao Magikarp:", posicaoMagikarp)

            # Verificando se a posição do magikarp já está cadastrada.
            posicaoJaCadastrada = False
            numPosicoes = len(listaPosicoes[magikarp])
            count = 0
            while (not posicaoJaCadastrada) and (count < numPosicoes):    
                posicaoCadastrada = listaPosicoes[magikarp][count]
                print ("Posicao Cadastrada =", posicaoCadastrada)           
                if posicaoMagikarp == posicaoCadastrada:
                    posicaoJaCadastrada = True
                count += 1
            
            if not posicaoJaCadastrada:
                if not cadastrar:
                    return ACHOU_SHINY_NA_HORDA + magikarp
                # -------------------------------------------------------------------- #
                #           Parte dedicada para cadastrar novas hordas                 #
                # -------------------------------------------------------------------- #                  
                hordaFile = HORDA_MAGIKARP_FILE
                CadastrarPosicaoHorda(hordaFile, posicaoMagikarp, linhaAlvo=magikarp+1)
                listaPosicoes[magikarp].append(posicaoMagikarp)
                #----------------------------------------------------------------------#

                # Alguma posição, de algum pokemon dessa horda, não era conhecida e foi cadastrada.
                situacao = CADASTROU_NOVA_POSICAO
                
    return situacao

def RegisterShiny(filename, encontros):
    # Abrindo o arquivo.
    try:
        shinyMagikarpFile = open(filename, "r")
    except:
        # Criando o arquivo, já que o mesmo não existe.
        shinyMagikarpFile = open(filename, "w")
        conteudo = []
    else:
        conteudo = shinyMagikarpFile.readlines()
        shinyMagikarpFile.close()
        shinyMagikarpFile = open(filename, "w")

    conteudo.append(f"Magikarp shiny - {datetime.datetime.now()} - {encontros} encontros\n")    
    shinyMagikarpFile.writelines(conteudo)
    shinyMagikarpFile.close()
    return OK