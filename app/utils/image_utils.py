from PIL import Image
from tensorflow.keras.utils import img_to_array
import numpy as np


def filetoimage_array(uploaded_file, size=(150,150)):
  image = Image.open(uploaded_file)
  image = image.resize(size)
  image_array = img_to_array(image)

  return image_array  

def rescale(image_array, scale = 1./255):
  image_array /= 255.0
  return image_array

def expand_array_dims(image_array): 
  return np.expand_dims(image_array, axis=0)
