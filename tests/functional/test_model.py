from app.models import model
import os 

def test_get_image_class():
  file_path = 'tests/test_assets/Allure 3 Piece Sofa and Armchair Set.jpg'
  file_path = os.path.join(os.getcwd(), file_path)
  labels = ['Bed', 'Chair', 'Sofa']
  image_class = model.get_image_class(file_path, labels)

  #test if function works not classification
  assert  image_class in labels