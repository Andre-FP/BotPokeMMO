import sys
sys.path.append('..')
import pyautogui
import time

def rectangle(coordenada):
    left = coordenada[0]
    top = coordenada[1]
    right = coordenada[0] + coordenada[2]
    bottom = coordenada[1] + coordenada[3]
    return (left, top, right, bottom)

def CadastrarOutraImagem(images_path, coordenada):
    if len(images_path) >= 3:
        return sys.exit("Imagens já cadastradas")
    if len(images_path) == 0:
        return sys.exit("images_path não pode ser vazio")

    cadastrar_nova = True
    for image_path in images_path:
        coordenadaImagem = pyautogui.locateOnScreen(image_path)    
        if coordenadaImagem != None:
            cadastrar_nova = False

    if cadastrar_nova:
        im = pyautogui.screenshot()
        im = im.crop(rectangle(coordenada))        
        new_image_path = get_next_image_path(images_path)
        im.save(new_image_path)
        return new_image_path
    return False

def get_next_image_path(images_path):
    if len(images_path) >= 3:
        return sys.exit("Imagens já cadastradas")
    
    next_number = 1
    image_number = 0
    for image_path in images_path:
        if image_path != None:
            try:                
                image_number = int(image_path[-5])
            except:
                image_number = 1
            if image_number >= next_number:
                next_number = image_number + 1

    next_image_path = f'{image_path[0:-5]}{next_number}.png'
    return next_image_path

def main():
    images = ["../imagens/Magikarp1.png"]
    coordenada = (816, 515, 20, 33)
    limite = len(images)
    print("Aguarde 5 segundos...")
    i=-1
    while limite < 3:
        i = i*(-1)
        pyautogui.moveRel(i*500, 0, duration=2)
        #pyautogui.moveRel(-i*500, 0, duration=2)
        time.sleep(5)
        new_image = CadastrarOutraImagem(images, coordenada)
        if new_image:
            images.append(new_image)
            limite += 1
            print("Imagem", limite, "cadastrada!")

    print("Todas as imagens cadastradas")
    while True:        
        pyautogui.moveRel(500, 0, duration=2)
        pyautogui.moveRel(-500, 0, duration=2)

if __name__ == "__main__":
    main()
        