# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 17:48:35 2022

@author: andre
"""

import cv2
from matplotlib import pyplot as plt

image = cv2.imread("C:/Users/andre/BRICS-TB/Adamant1.png")
imagem = plt.subplot(1,1,1)
imagem.set_title("Adamant")
imagem.imshow(image, interpolation='nearest')
print(image[0][0])
plt.show()

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
imagem = plt.subplot(1,1,1)
imagem.set_title("Adamant")
imagem.imshow(
    image.reshape(18,58),
    interpolation='nearest',
    cmap='binary',
    vmin=0, vmax=255
    )

plt.show()