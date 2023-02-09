import sys
sys.path.append("..")
from BotPokeMMO.utils.Functions import *

def main():
    p_Teclas = ObterPosicoesTeclas()

    if p_Teclas == TECLA_NAO_ENCONTRADA:
        print ("Erro Login")
        return TECLA_NAO_ENCONTRADA

    #Posicoes de cada tecla
    t_Left = p_Teclas[1]          # Recebem (x,y) 
    p_Up = p_Teclas[2]
    t_Right = p_Teclas[3]
    t_Down = p_Teclas[4]
    t_Z = p_Teclas[5]
    t_Bolsa = p_Teclas[7]
    p_F1 = p_Teclas[8]
    t_Fly = p_Teclas[9]
    t_SuperRepel = p_Teclas[10]
    t_Repel = p_Teclas[11]
    p_F7 = p_Teclas[12]
    t_SweetScent = p_Teclas[13]
    p_F9 = p_Teclas[14]
    t_ESC = p_Teclas[15]
    t_Regar = p_Teclas[16]
    
    #Usar fly para Sootopolis
    print ("Usando fly para Sootopolis...")
    funcionamento = Fly(t_Fly, "Hoenn", "Sootopolis")
    if funcionamento != OK:
        print ("Erro na funcao Fly")
        return funcionamento

    #Entra no Centro Pokemon (CP), recupera vida e sai
    print ("Entrando no CP e recuperando vida...")
    funcionamento = EntrarUsarESairCP(p_Up, t_Z, t_Down, "Hoenn")
    if funcionamento != OK:
        print("Erro na funcao EntrarUsarESairCP")
        return funcionamento
    
    # Verificando a qntd de pokebolas que o personagem tem
    print ("Verificando a quantidade de pokebolas...")
    totalDePokebolas = ChecandoQntdPokebolas(t_Bolsa)
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
    
    ClickTecladoVirtual(t_Down, clicks=6)
    Virar("esquerda", p_Teclas) 
    ClickTecladoVirtual(t_Left, clicks=2)
    
    erro = UsarSurf(t_Z)
    if erro != OK:
        print ("Erro usando Surf")
        return erro
    
    for position in range(6):    
        # Usando sweet scent
        ClickTecladoVirtual(t_SweetScent)
            
        useAgain = True
        while not CheckPixel("balaoChat"):
            if not useAgain:
                print ("Não foi usado sweet scent.")
                return ERRO_SWEET_SCENT

            # Tentando mais uma vez
            ClickTecladoVirtual(t_SweetScent)
            useAgain = False
                
        time.sleep(5)
        
        # Identificando cada magikarp da horda.
        ReconhecerHorda("Magikarp", listaPosicoesPokemon)  
        
        # Se for um pokemon shiny
        print("Pokemon shiny encontrado!")
        erro = KillNonShinyHorde(p_Teclas, position + 3)
        if erro != OK:
            return erro
        erro = FalseSwipeHorde(p_Teclas, position + 3, pp=30)                    
        if erro != OK:
            return erro
        confirmacao = POKEMON_NAO_CAPTURADO
        while confirmacao == POKEMON_NAO_CAPTURADO:
            erro = LancarPokebola(p_Teclas, qntdPokebolas=50)
            if erro != OK:
                return erro
            confirmacao = VerificarPokemonCapturado(manter_pokemon=True)
        ClickTecladoVirtual(t_ESC)
        RegisterShiny(FOUND_SHINY_FILE)

    return OK
    
main()