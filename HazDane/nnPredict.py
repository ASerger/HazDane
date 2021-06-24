import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

from config import ml_img_width, ml_img_height # type: ignore

img_height = ml_img_height
img_width = ml_img_width

model = tf.keras.models.load_model("nnModel")

model.summary()

img_path = 'index.jpg'
img = keras.preprocessing.image.load_img(img_path, target_size=(img_height, img_width))
img_array = keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0) # Create a batch

predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])

print(score)
print(np.argmax(score), 100 * np.max(score))
