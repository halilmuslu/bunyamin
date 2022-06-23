import tensorflow as tf
from tensorflow.keras.applications import vgg19, resnet50, inception_v3, vgg19

class CustomModel:
    def __init__(self, model_name):
        self.model_name = model_name

    def vgg16(self):
        pass


if __name__ == "__main__":
    custom_model = CustomModel("vgg16")
    CustomModel.vgg16()
