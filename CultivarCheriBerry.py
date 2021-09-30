from Scripts import BotCultivarBerry, OK
import os 
import time

def main():

    print("\n\tOlá ! Esse é o script para cultivar as berries !\n\n")

    print ("Requisitos:")
    print ("\tSuper repel x2")
    print ("\tRepel x1")
    print ("\tSementes picantes suficientes para todos os slots.\n")

    ### Perguntando o modo desejado de execução ###

    repetir = True
    while repetir:
        repetir = False
        print ("O que você deseja fazer?")
        print ("Opção 1: Plantar e regar as berries.")
        print ("Opção 2: Regar as berries.")
        print ("Opção 3: Colher as berries.")
        print ("Opção 4: Colher e plantar as berries.")
        
        opcao = input("Digite o número da opção: ")
        
        if opcao == "1":
            escolha = "plantar"
        elif opcao == "2":
            escolha = "regar"
        elif opcao == "3":
            escolha = "colher"
        elif opcao == "4":
            escolha =  "colherEPlantar"
        else: 
            print ("Opcão inválida. Digite novamente\n\n")
            repetir = True

    
    ### Perguntando se o jogo está aberto ###
    
    print ("\n\nO jogo está aberto?")
    
    resposta = input("Digite \"N\" para NÃO e qualquer outra coisa para SIM: ")
    
    if resposta == "N" or resposta == "n":
        jogo = "fechado"
    else: 
        jogo = "aberto"

    print ("O jogo está", jogo, end="\n\n")
    
    print ("Preparando o programa, espere um momento...") 
    print ("OBS: Aperte Ctrl + C quando quiser parar o programa.\n")
    time.sleep(3)
    print ("Executando...")

    ### Executando o bot ###
    
    erro = BotCultivarBerry(modo=escolha, jogo=jogo)
    if erro != OK:
        print ("Erro #", erro, sep="")

    os.system("PAUSE")
    return erro

if __name__ == "__main__":
    main()