from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, Region
from msrest.authentication import ApiKeyCredentials
import os, time, uuid




# retrieve environment variables
ENDPOINT = os.environ["VISION_TRAINING_ENDPOINT"]
training_key = os.environ["VISION_TRAINING_KEY"]
prediction_key = os.environ["VISION_PREDICTION_KEY"]
prediction_resource_id = os.environ["VISION_PREDICTION_RESOURCE_ID"]

#################################################
#Authenticate the client
#Instantiate a training and prediction client with your endpoint and keys. Create ApiKeyServiceClientCredentials objects with your keys, and use them with your endpoint to create a CustomVisionTrainingClient and CustomVisionPredictionClient object.
#################################################

credentials = ApiKeyCredentials(in_headers={"Training-key": training_key})


trainer = CustomVisionTrainingClient(ENDPOINT, credentials)

prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)

#################################################3
#Create a new Custom Vision project
#################################################

publish_iteration_name = "RWSBootClassifyModel"

credentials = ApiKeyCredentials(in_headers={"Training-key": training_key})
trainer = CustomVisionTrainingClient(ENDPOINT, credentials)

#################################################
# Create a new project
#################################################
print ("Deleting tags...")
project_name = 'RWSBootAi-5'## + str(uuid.uuid4())
projectId ='4326cbad-e3ef-4e6a-870f-32394e5bf123' #'e777e3e4-2ae3-4d03-9fb3-1f5e0925d72b'# 'b5728b98-c8aa-46c2-a394-97955008482f'  #'ba98e468-4593-45b8-99cf-8bd5df00dd62' #9a4434c4-cd29-493f-9b6e-8bc25be9e6a7'
#projectId = 'e777e3e4-2ae3-4d03-9fb3-1f5e0925d72b' #'4326cbad-e3ef-4e6a-870f-32394e5bf123'  #'e777e3e4-2ae3-4d03-9fb3-1f5e0925d72b' ##4
tags = trainer.get_tags(projectId)

for tag in tags:
    style = str(tag.name).split('-')[1]
    if  style.isdigit():
        stylenum = int(style)
        print(stylenum)
        for i in range(96317, 98054):
            if i == stylenum:
                print('Delete')
                trainer.delete_tag(projectId, tag.id)
