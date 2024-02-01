import rembg
import numpy as np 
from PIL import Image
from tensorflow.keras.preprocessing import image
from keras.applications.vgg16 import VGG16
from sklearn.metrics.pairwise import cosine_similarity

vgg16 = VGG16(weights="imagenet", include_top=False, 
              pooling='max', input_shape=(320, 320, 3))

for model_layer in vgg16.layers:
  model_layer.trainable = False
# print the summary of the model's architecture.
# vgg16.summary()

def load_image(image_path):
    """
        -----------------------------------------------------
        Process the image provided. 
        - Resize the image 
        -----------------------------------------------------
        return resized image
    """

    input_image = Image.open(image_path)
    input_image = input_image.resize((320, 320))
    input_image = rembg.remove(input_image)
    input_image = input_image.convert("RGB")
    # resized_image = input_image.resize((224, 224))
    
    return input_image
    # return resized_image

def get_image_embeddings(object_image : image):
    
    """
      -----------------------------------------------------
      convert image into 3d array and add additional dimension for model input
      -----------------------------------------------------
      return embeddings of the given image
    """

    image_array = np.expand_dims(image.img_to_array(object_image), axis = 0)
    image_embedding = vgg16.predict(image_array)

    return image_embedding

def get_similarity_score(first_image : str, second_image : str):
    """
        -----------------------------------------------------
        Takes image array and computes its embedding using VGG16 model.
        -----------------------------------------------------
        return embedding of the image
        
    """

    first_image = load_image(first_image)
    second_image = load_image(second_image)

    first_image_vector = get_image_embeddings(first_image)
    second_image_vector = get_image_embeddings(second_image)
    
    similarity_score = cosine_similarity(first_image_vector, second_image_vector).reshape(1,)

    return similarity_score, first_image, second_image
