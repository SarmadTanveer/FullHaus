# Fullhaus Classifier
A flask API providing access to the fullhaus image classifier. 

## Prerequisites
In order to run this container you'll need the following: 
- Docker installed 
- Docker hub account
- Access to a CLI

## Usage 
### Runing the container
1. Pull latest image by running:  
`docker pull stanv1/fullhaus:latest`
2. Run the container:  
`docker run -d -p 3000:3000 stanv1/fullhaus:latest`
3. After the container is running, POST requests can be made to:  
`http://localhost:3000/api/v1/classify`

### API info
The endpoint `http://localhost:3000/api/v1/classify` expects image files sent as form data. The file is located using 'image' as the key. The endpoint only allows **.png** and **.jpg** extensions. 

A successfull request returns a 200 status code and a JSON response which contains **'category'** field. The value of this field is the classification result. 

An unsuccessful request will return a status code of 400 or 500 and a message datailing the cause of the error.

### Example 
cURL request:  
`curl -F 'image=@<Path to image file>' http://localhost:3000/api/v1/classify`

Server response:  
`{"category":"Chair"}`

## Model Info
The classifier is a custom CNN trained on the provided dataset. The architecture and training details can be found in the following notebook:  
https://colab.research.google.com/drive/1poqxgY-ZREM5YLMGg9cSc2D6eaB5pYaq?usp=sharing

Note: While the model exhibits high validation and training accuracy, this is most likely due to a small dataset. The variance in the validation set is very low. Future imporvements could include generating augmented pictures in the training set to increase variance and generalize the model. Increasing the dataset size could have a simillar effect. The model wasn't tested against a test set due to the low number of samples.    


