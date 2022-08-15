import pyautogui
import time
import os

print("Aguarde 5 segundos...")
time.sleep(5)
images_path = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "imagens"))
coordinates = pyautogui.locateOnScreen(f"{images_path}/Magikarp1.png")
found = "0"
if coordinates != None:
    found = "1"
else:
    coordinates = pyautogui.locateOnScreen(f"{images_path}/Magikarp2.png")
    if coordinates != None:
        found = "2"
    else:
        coordinates = pyautogui.locateOnScreen(f"{images_path}/Magikarp3.png")
        if coordinates != None:
            found = "3"

print(found)
print(coordinates)
pyautogui.moveTo(coordinates)
