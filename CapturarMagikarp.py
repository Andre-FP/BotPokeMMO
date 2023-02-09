from Scripts.CapturarMagikarp import BotCapturarMagikarp, OK
import os 
import time

def main():

    print("\n\tOlá ! Esse é o script para capturar magikarp !\n\n")

    print ("  Diga o máximo de dinheiro que você quer gastar.\n")
    print ("  Tenha certeza de não digitar uma quantia maior do que")
    print ("você tem.\n")
    print ("  Se você não lembrar de quanto dinheiro você tem no jogo")
    print ("e decidir conferir, lembre-se de fechar o jogo depois.\n")
    
    entradaValida = False
    while not entradaValida:
        print ("(Não use '.' ou ',')")
        entrada = input("\nDinheiro: ")
        
        entradaValida = entrada.isdigit()
        if not entradaValida:
            print ("Número inválido. Digite novamente.\n")

    
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
    
    erro = BotCapturarMagikarp(int(entrada), jogo=jogo)
    if erro != OK:
        print ("Erro #", erro, sep="")

    os.system("PAUSE")
    return erro

if __name__ == "__main__":
    main()
