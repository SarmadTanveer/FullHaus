from flask import Flask, request
from main import app 
from app.utils import image_utils
import numpy as np

@app.route("/api/v1/classify", methods=["Post"])
def classify_image():
  try:
    print(request.files['image'])

    if '' in request.files: 
      return({
      "message": "Error please provide an image or check file key"
      },400)
  
    if "image" not in request.files:
      return ({
      "message": "Please ensure file key is 'image'"
      },400)

    ext = request.files['image'].filename.split('.')[-1]
    if ext not in app.config['AllowedExt']:
      return({
        "message": "File extension not allowed"
      },400)

  except Exception as e: 
    #the catch all

    print(e)
    return({
        "message": "something went wrong"
    }, 500) 

  image_array =  image_utils.filetoimage_array(request.files['image'], size=(150,150))
  print(image_array.shape)
  image_array = image_utils.rescale(image_array, scale=1./255)
  print(image_array)
  return({
    "category": "Bed"
  }, 200) 

