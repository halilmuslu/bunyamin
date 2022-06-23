import tensorflow as tf
import torch
import cv2

class Model:
    def __init__(self, model_path):
        self.model_path = model_path
        self.readModel()

    def readModel(self):
        if "yolov5":
            self.model = tf.keras.Model.readModel(self.model_path)
        else:
            self.model = tf.keras.Model.getModel(self.model_path)

    def predict(self, Image):
        self.Image = Image

        model = self.read_model(self.model_path)
        self.output = model.predict(self.Image)
        return self.output

    def readImage(self):
        return self.Image


if __name__ == '__main__':
    model = Model("path")
    model.predict("image")
