import numpy as np
from .ProcessData import getXTrain,getYTrain

from keras.layers import Conv2D,Dense,Flatten,MaxPooling2D
from keras.models import Sequential

X_train = getXTrain()
Y_train = getYTrain()

