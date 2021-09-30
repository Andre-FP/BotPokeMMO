import pyautogui
import os
import time
import sys
sys.path.append("..")
from utils.Functions import *

OK = 0
FALTANDO_ARGUMENTOS = 1
TUPLA_INVALIDA = "2 - TUPLA_INVALIDA"
ERRO_CRIANDO_ARQUIVO = 3
STRING_VAZIA = "3 - STRING VAZIA"

def RegistrarCorPixel(pixel, nomePixel=""):
    '''
    Registra todas as cores possíveis do pixel na posição desejada.

    Argumentos: 
                pixel -> tupla -> posição do pixel "(x, y)"
                nomePixel -> string -> nome do pixel

    Retornos:   
                OK
                FALTANDO_ARGUMENTOS
                ERRO_CRIANDO_ARQUIVO
    '''

    if nomePixel == "":
        return FALTANDO_ARGUMENTOS

    time.sleep(5)

    # Nomeando o arquivo
    nomeArquivo = FILESDIR + nomePixel + ".txt"

    # Abrindo o arquivo.
    try:
        corPixelFile = open(nomeArquivo, "r")
    
    except:
        print ("Criando o arquivo...")
        
        try:
            corPixelFile = open(nomeArquivo, "w")
        except:
            return ERRO_CRIANDO_ARQUIVO
        
        numeroDeCores = 0
        listaCores = []

    else:
        print ("Arquivo já existia.")
        
        linhaArquivo = corPixelFile.readlines()
        corPixelFile.close()
        
        listaCores = []

        if len(linhaArquivo) != 0:
            listaCoresString = linhaArquivo[0].split(';')

            for corString in listaCoresString:
                corTupla = StringTuplaParaTupla(corString)
                if corTupla == TUPLA_INVALIDA:
                    print ("Arquivo não contém tuplas válidas.")
                    return TUPLA_INVALIDA
                listaCores.append(corTupla)
                
        numeroDeCores = len(listaCores)


    if numeroDeCores >= 3:
        print ("Esse pixel já tinha sido cadastrado.")
    else:
        print ("Cadastrando as cores...")

    while numeroDeCores < 3: 

        # Pegando a cor do pixel
        im = pyautogui.screenshot()
        corAtualPixel = im.getpixel(pixel)
        print ("Cor:", corAtualPixel)

        # Analisando se já está cadastrada.
        colorIsInFile = False

        for corArquivo in listaCores:
            if corAtualPixel == corArquivo:
                colorIsInFile = True

        # Cadastrando e adicionando na lista.
        if not colorIsInFile:
            
            corPixelFile = open(nomeArquivo, "a")
            
            if numeroDeCores == 0:
                corPixelFile.write(str(corAtualPixel))
            else:
                corPixelFile.write(";" + str(corAtualPixel))
            
            corPixelFile.close()


            listaCores.append(corAtualPixel)
            numeroDeCores += 1
            print ("Cor", numeroDeCores, "cadastrada:", corAtualPixel)
            if numeroDeCores == 3:
                print ("Cores cadastradas com sucesso!")

    return OK


def main():

    print("\n\tEsse é o programa para cadastrar cores do pixel!\n\n")

    print ("  Será preciso que a tela referente a cor do pixel que você deseja cadastrar,")
    print ("esteja disponível dentre 5 segundos após iniciar o programa.\n")
    
    print ("Digite as coordenadas do pixel no formato \"(x, y)\".")
    pixelString = input("\nCoordenada: ")  

    print ("Agora crie um nome para esse pixel. Esse será o nome do arquivo gerado.")
    nomePixel = input("\nNome do pixel: ")

    if nomePixel == "" or nomePixel == " ":
        print ("Nome inválido.")
        return -1

    pixel = StringTuplaParaTupla(pixelString)
    if pixel == TUPLA_INVALIDA:
        print ("Pixel inválido.")
        return TUPLA_INVALIDA

    print ("Executando o programa...")
    


    erro = RegistrarCorPixel(pixel, nomePixel)
    if erro != OK:
        print ("Erro #", erro, " executando a função \"RegistrarCorPixel\".", sep="")
        return erro

    return OK


# x=891, y=132

main()




