from app.utils import image_utils
import os 
import numpy as np

def test_filetoimage_array():
    
    file_path = 'tests/test_assets/Allure 3 Piece Sofa and Armchair Set.jpg'
    file_path = os.path.join(os.getcwd(), file_path)

    image_array = image_utils.filetoimage_array(file_path, (150,150))
    print(type(image_array))
    assert isinstance(image_array, np.ndarray)
    assert image_array.shape == (150,150,3)

def test_expand_array_dims():
    arr = np.zeros((10,10,3))
    arr = image_utils.expand_array_dims(arr)

    assert arr.shape == (1,10,10,3)

def test_rescale():
    arr = np.ones((10,10,3))
    arr = image_utils.rescale(arr, scale=20)

    max = arr.max()

    assert max == 20
