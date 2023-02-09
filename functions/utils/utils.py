from functions.utils.erros import *

def StringTuplaParaTupla(string):
    '''
    Converte uma string da forma "(a, b)" ou "(a, b, c)", onde a, b e c têm que ser números naturais, para tupla.
    Essa função foi feita para ser usada para pixel e cores do pixel, mas pode ser usada para o que for necessário,
    se possível.

    Args:
        string(str):
            string no formato "(a, b)"
    
    Returns:
        tupla
        TUPLA_INVALIDA
        STRING_VAZIA
    '''
    if len(string) == 0:
        return STRING_VAZIA
    if string[0] != '(':
        return TUPLA_INVALIDA
    if string[-1] == '\n':  
        string = string[0:-1]  # tira o '\n' se a string tiver
    if string[-1] != ')':
        return TUPLA_INVALIDA

    tamanhoString = len(string)
    isTupla = False
    fimString = False
    coordenada = ["", "", ""]
    caracteresValidos = "0123456789,() "
    virgula = 0
    abreParenteses = 0

    for caracter in range(tamanhoString):

        # Verifica se o caracter é inválido.
        caracterValido = False
        for termo in caracteresValidos:
            if string[caracter] == termo:
                caracterValido = True
        if caracterValido == False:
            return TUPLA_INVALIDA
        
        if string[caracter] != ' ':

            # Se achar o ')', tem que ser o fim da string.
            if string[caracter] == ')':
                if caracter + 1 != tamanhoString:
                    return TUPLA_INVALIDA
                fimString = True

            if not fimString:
                if string[caracter] == ',':
                    if not isTupla:
                        return TUPLA_INVALIDA
                    virgula += 1
                    if virgula > 2:
                        return TUPLA_INVALIDA                
                
                elif string[caracter] == '(':
                    isTupla = True
                    abreParenteses += 1
                    if abreParenteses > 1:
                        return TUPLA_INVALIDA  
                
                elif isTupla:
                    coordenada[virgula] += string[caracter]              
    # end for
    x = 0
    y = 1
    z = 2
    if coordenada[x] == "" or coordenada[y] == "":
        return TUPLA_INVALIDA
    if coordenada[z] == "" and virgula == 2:
        return TUPLA_INVALIDA
    if not fimString:
        return TUPLA_INVALIDA

    if virgula == 2:
        pixel = (int(coordenada[x]), int(coordenada[y]), int(coordenada[z]))
    else:
        pixel = (int(coordenada[x]), int(coordenada[y]))
    print(pixel)
    return pixel
