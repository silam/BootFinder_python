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
print ("Creating project...")
project_name = 'RWSBootAi-5'## + str(uuid.uuid4())
projectId ='4326cbad-e3ef-4e6a-870f-32394e5bf123' #'e777e3e4-2ae3-4d03-9fb3-1f5e0925d72b'# 'b5728b98-c8aa-46c2-a394-97955008482f'  #'ba98e468-4593-45b8-99cf-8bd5df00dd62' #9a4434c4-cd29-493f-9b6e-8bc25be9e6a7'
project = trainer.get_project(projectId)

#################################################
#Add tags to the project

# Make two tags in the new project
#################################################

arrInputDir  = os.listdir('F:\\AIImages\\RWSBootWithbackground\\1')
for d in arrInputDir:
    tagnum = d.split('-')[1]
    if tagnum.isnumeric() :
        continue

    # if num <= 96226: 
    #     continue

    # if d.__contains__('A') == False or d.__contains__('G') == False: 
    #     continue

    style_tag = trainer.create_tag(project.id, d)
    print(style_tag)
    style = 'F:\\AIImages\\RWSBootWithbackground\\' + d
    arrInputImageDir  = os.listdir(style)
    #print(arrInputDir)

    

    image_list = []

    for f in arrInputImageDir:
        imageName = style + '\\' + f
        print(imageName)
        with open(imageName, "rb") as image_contents:
            image_list.append(ImageFileCreateEntry(name=f, contents=image_contents.read(), tag_ids=[style_tag.id]))
    
    print('Uploading images...')
    upload_result = trainer.create_images_from_files(project.id, ImageFileCreateBatch(images=image_list))
    # if not upload_result.is_batch_successful:
    #     print("Image batch upload failed.")
    #     for image in upload_result.images:
    #         print("Image status: ", image.status)
    #     exit(-1)
    
    image_list.clear()

    #Train the project

print ("Training...")
iteration = trainer.train_project(project.id)
while (iteration.status != "Completed"):
    iteration = trainer.get_iteration(project.id, iteration.id)
    print ("Training status: " + iteration.status)
    print ("Waiting 10 seconds...")
    time.sleep(10)


# The iteration is now trained. Publish it to the project endpoint
trainer.publish_iteration(project.id, iteration.id, publish_iteration_name, prediction_resource_id)
print ("Done!")

#Test the prediction endpoint

# Now there is a trained endpoint that can be used to make a prediction
# prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
# predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)

# with open(os.path.join (base_image_location, "Test/test_image.jpg"), "rb") as image_contents:
#     results = predictor.classify_image(
#         project.id, publish_iteration_name, image_contents.read())

#     # Display the results.
#     for prediction in results.predictions:
#         print("\t" + prediction.tag_name +
#               ": {0:.2f}%".format(prediction.probability * 100))
        
#####################################################################









# hemlock_tag = trainer.create_tag(project.id, "Hemlock")
# cherry_tag = trainer.create_tag(project.id, "Japanese Cherry")


#Upload and tag images

# base_image_location = os.path.join (os.path.dirname(__file__), "C:\\dev\\ai\\cognitive-services-sample-data-files\\CustomVision\\ImageClassification\\Images")

# print("Adding images...")

# image_list = []

# for image_num in range(1, 11):
#     file_name = "hemlock_{}.jpg".format(image_num)
#     with open(os.path.join (base_image_location, "Hemlock", file_name), "rb") as image_contents:
#         image_list.append(ImageFileCreateEntry(name=file_name, contents=image_contents.read(), tag_ids=[hemlock_tag.id]))

# for image_num in range(1, 11):
#     file_name = "japanese_cherry_{}.jpg".format(image_num)
#     with open(os.path.join (base_image_location, "Japanese_Cherry", file_name), "rb") as image_contents:
#         image_list.append(ImageFileCreateEntry(name=file_name, contents=image_contents.read(), tag_ids=[cherry_tag.id]))

# upload_result = trainer.create_images_from_files(project.id, ImageFileCreateBatch(images=image_list))
# if not upload_result.is_batch_successful:
#     print("Image batch upload failed.")
#     for image in upload_result.images:
#         print("Image status: ", image.status)
#     exit(-1)

#     #Train the project

# print ("Training...")
# iteration = trainer.train_project(project.id)
# while (iteration.status != "Completed"):
#     iteration = trainer.get_iteration(project.id, iteration.id)
#     print ("Training status: " + iteration.status)
#     print ("Waiting 10 seconds...")
#     time.sleep(10)


# #Publish the current iteration


# # The iteration is now trained. Publish it to the project endpoint
# trainer.publish_iteration(project.id, iteration.id, publish_iteration_name, prediction_resource_id)
# print ("Done!")


# #Test the prediction endpoint

# # Now there is a trained endpoint that can be used to make a prediction
# prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
# predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)

# with open(os.path.join (base_image_location, "Test/test_image.jpg"), "rb") as image_contents:
#     results = predictor.classify_image(
#         project.id, publish_iteration_name, image_contents.read())

#     # Display the results.
#     for prediction in results.predictions:
#         print("\t" + prediction.tag_name +
#               ": {0:.2f}%".format(prediction.probability * 100))
        
