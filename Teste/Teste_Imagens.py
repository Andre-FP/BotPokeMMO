from keras.preprocessing import image
from tensorflow.keras.applications import VGG16
from tensorflow.keras.applications.vgg16 import preprocess_input
import numpy as np

model = VGG16(weights="imagenet", include_top=False)

model.summary()

