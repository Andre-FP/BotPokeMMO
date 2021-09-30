

##### Controlling the Mouse #####

# Medida de seguranca caso o mouse saia do controle
    pyautogui.FAILSAFE = True 

# Move o cursor pra posicao desejada (em pixel)
    pyautogui.moveTo(,,duration=)
    #Relativo. O ponto atual eh considerado (0,0)
    pyautogui.moveRel(,,duration=)

# Retorna a posicao atual do cursor
    pyautogui.position()

# Clica na posicao desejada. Default = posicao atual
    pyautogui.click()

# Retorna um objeto imagem representando a screenshot
    pyautogui.screenshot()

# Retorna uma tupla representando as cores RGBs do pixel (im = variavel que contem a imagem)
    im.getpixel((pixel[x], pixel[y]))

# Retorna True or False, se o pixel corresponde a cor desejada
    pyautogui.pixelMatchesColor(50, 200, (130, 135, 144))

# Localiza a imagem submetida na tela atual e retorna a posicao do pixel superior esquerdo.
# (x,y, width, height)
# Se nao for encontrada, retorna 'none'.
    pyautogui.locateOnScreen('submit.png')
    >> (643, 745, 70, 29)

# Localiza todas as posicoes onde tem uma imagem igual a submetida e retorna uma lista dessas posicoes
# [(x,y, width, height), ()]
# Se nao for encontrada, retorna 'none'.
    list(pyautogui.locateAllOnScreen('submit.png'))

# Retorna a posicao do centro da area retangular
# Argumento: ((x, y, width, height))
    pyautogui.center((643, 745, 70, 29))


##### Controlling the keyboard #####

# Escreve a string apertando os caracteres em sequencia
    pyautogui.typewrite('Hello world!')

# Pressiona cada tecla por vez, inclusive as que nao da pra botar numa string   
    pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'])

# Seguram o botao ou soltam, ou apenas clicam.
    pyautogui.keyDown('shift'); pyautogui.press('4'); pyautogui.keyUp('shift')

# keyDown keyDown, keyUp keyUp
    pyautogui.hotkey('ctrl', 'c')

