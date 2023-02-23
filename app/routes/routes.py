from flask import Flask, request
from main import app 
from app.models.model import get_image_class

@app.route("/api/v1/classify", methods=["Post"])
def classify_image():
  try:

    if '' in request.files: 
      return({
      "message": "Please provide an image or check file key"
      },400)
  
    if "image" not in request.files:
      return ({
      "message": "Please ensure file key is 'image'"
      },400)

    print(request.files['image'])

    if request.files['image'].filename is '' or request.files['image'].filename is ' ': 
      return({
        "message": "Missing image file"
      },400)

    ext = request.files['image'].filename.split('.')[-1]
    if ext not in app.config['AllowedExt']:
      return({
        "message": "File extension not allowed"
      },400)

    category = get_image_class(request.files['image'], labels=['Bed', 'Chair', 'Sofa'])

  except Exception as e: 
    #the catch all
    print(e)
    return({
        "message": "something went wrong"
    }, 500) 

  

  

  return({
    "category": category
  }, 200) 

