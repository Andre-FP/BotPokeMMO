import yaml
import os
import time
import pyautogui
import keyboard

CONFIG_FILE = "./parametros.yaml"
with open(CONFIG_FILE) as f:
    loaded = yaml.load(f, yaml.FullLoader)

##################### PARÂMETROS #######################
FOUND_SHINY_FILE = loaded["FOUND_SHINY_FILE"]           # Arquivo para registro de shiny
POSITIONS_HORDE_MOUSE = loaded["POSITIONS_HORDE_MOUSE"] # Lista com as posições dos nomes dos pokemons nas hordas
HORDA_MAGIKARP_FILE = loaded["HORDA_MAGIKARP_FILE"]                       # Arquivo com o centro de cada imagem do pokemon
ENCOUNTERS_FILE = loaded["ENCOUNTERS_FILE"]               # Arquivo para salvar o número de encontros de hordas
POKEMMOFILE = loaded["POKEMMOFILE"]                     # Path do executável do PokeMMO
ROOT = loaded["ROOT"]                                   # Path da pasta raíz do repositório
TECLAS = loaded["TECLAS"]                               # Dicionário com todas as funções mapeadas às teclas 
IMAGESDIR = loaded["IMAGESDIR"]                               # Dicionário com todas as funções mapeadas às teclas 
FILESDIR = loaded["FILESDIR"]                               # Dicionário com todas as funções mapeadas às teclas 

FOUND_SHINY_FILE = os.path.join(FILESDIR, FOUND_SHINY_FILE)
HORDA_MAGIKARP_FILE = os.path.join(FILESDIR, HORDA_MAGIKARP_FILE)
ENCOUNTERS_FILE = os.path.join(FILESDIR, ENCOUNTERS_FILE)

## Coordenadas para serem usado em listas (coordx[x], coordy[y])
x=0
y=1

#Teclas
t_Bike = TECLAS["Bike"]
t_Fly = TECLAS["Fly"]
t_Bolsa = TECLAS["Bolsa"]
t_Up = TECLAS["Up"]
t_Left = TECLAS["Left"]
t_Down = TECLAS["Down"]
t_Right = TECLAS["Right"]
t_Z = TECLAS["Z"]
t_X = TECLAS["X"]
t_Regar = TECLAS["Regar"]
t_ESC = TECLAS["ESC"]
t_Pescar = TECLAS["Pescar"]
t_SuperRepel = TECLAS["SuperRepel"]
t_Repel = TECLAS["Repel"]
t_SweetScent = TECLAS["SweetScent"]
t_Teleport = TECLAS["Teleport"]
##########################################################