import tensorflow as tf
import torch

class Model:
    def __init__(self, model_path):
        self.model_path = model_path

    def readModel(self):
        self.model = tf.keras.Model.readModel(self.model_path)


if __name__ == '__main__':
    model = Model("path")
    model.fit()
