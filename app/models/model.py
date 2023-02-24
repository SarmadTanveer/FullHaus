from tensorflow.keras.models import load_model
from app.utils import image_utils
import numpy as np
import os


def get_model(model_name = "modelv2"):
  cwd = os.getcwd()
  models_dir = os.path.join(cwd,'app/models')
  model_location = os.path.join(models_dir, model_name)
  model = load_model(model_location)
  return model 

def prepare_image(fileObject):
  image_array = image_utils.filetoimage_array(fileObject, size=(150,150))
  #not required for model v2
  #image_array = image_utils.rescale(image_array)
  image_array = image_utils.expand_array_dims(image_array)
  return image_array


def get_image_class(fileObject, labels):   
  image_array = prepare_image(fileObject)
  model = get_model("modelv1")
  predictions = model.predict(image_array)
  image_class = labels[np.argmax(predictions)]
  return image_class 


  
    