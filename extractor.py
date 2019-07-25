# from keras.preprocessing import image
# from keras.applications.vgg16 import VGG16, preprocess_input
# from keras.models import Model
import numpy as np
# import tensorflow as tf


class FeatureExtractor:
    def __init__(self):
        pass

    def extract(self, img):  # img sebagai parameter dari PIL.Image.open(path)
        img = img.resize((224, 224))  # VGG must take a 224x224 img as an input
        img = img.convert('HSV')  #converting into HSV
        histogram, bins = np.histogram(img,256,[0,256]) #parameter gambar,bin,range
        return histogram #histogram bentuk array