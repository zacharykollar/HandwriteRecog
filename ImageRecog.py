import tensorflow as tf
import keras as k
from keras.layers.core import Dense, Activation
from keras.datasets import mnist
from keras.utils import np_utils
import numpy as np

(x_train, y_train), (x_test, y_test) = mnist.load_data()
X_train = x_train.reshape(60000, 784)
X_test = x_test.reshape(10000, 784)
Y_train = np_utils.to_categorical(y_train, 10)
Y_test = np_utils.to_categorical(y_test, 10)
class ImageRecognition:
    def __init__(self):
        self.model = k.Sequential()
        self.model.add(Dense(512, input_shape=(784,)))
        self.model.add(Activation('relu'))
        self.model.add(Dense(256))
        self.model.add(Activation('relu'))
        self.model.add(Dense(128))
        self.model.add(Activation('relu'))
        self.model.add(Dense(10))
        self.model.add(Activation('softmax'))
        self.model.compile(loss="categorical_crossentropy",metrics=['accuracy'],optimizer='adam')
        self.model.fit(X_train, Y_train, batch_size=256, epochs=16, verbose=2, validation_data=(X_test, Y_test))
        
    def check(self, bitmap):
        return self.model(bitmap)

        
a = ImageRecognition()

