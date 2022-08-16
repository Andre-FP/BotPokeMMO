import sys
sys.path.append("..")
import pyautogui
import time
from utils.Functions import *

pixel = (598, 172)
time.sleep(2)

naoFugiu = CheckPixel("hordaApareceu", tentativas=100)
print(naoFugiu)
pyautogui.moveTo(pixel, duration=1)