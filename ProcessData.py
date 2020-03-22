import cv2 as cv
import os
import glob
import  numpy as np
# from keras.datasets import mnist
# (XTrain,YTrain),(XTest,YTest) = mnist.load_data()
#
# print(XTrain.shape)
# XTrain = XTrain.reshape(XTrain.shape[0],28,28,1)
# print(XTrain.shape)
# print(YTrain.shape)
def getXTrain():
    # 79 kí tự train
    # mỗi kí tự gồm 30 ảnh. mỗi ảnh có size là 20x20
    # (2370,20,20)
    X_train = []
    for i in range(79):
        img_data = "../Dataset/English_Alphabet/"+str(i+1)
        img_path = os.path.join(img_data,"*g")
        files = glob.glob(img_path)
        for file in files:
            img = cv.imread(file,0)
            img =cv.resize(img,(20,20))
            img =  img/255
            X_train.append(img)
    X_train = np.asarray(X_train)
    X_train = X_train.reshape(X_train.shape[0], 20, 20, 1)
    return X_train

def getYTrain():
    Y =['a','b', 'c', 'd', 'e' ,'f' ,'g' ,'h', 'i', 'j' ,'k' ,'l' ,'m' ,'n' ,'o', 'p', 'q','r' ,'s' ,'t', 'u', 'v' ,'w', 'x', 'y' ,'z',
        'A' ,'B', 'C' ,'D' ,'E' ,'F' ,'G' ,'H', 'I', 'J', 'K' ,'L' ,'M' ,'N', 'O', 'P' ,'Q' ,'R' ,'S' ,'T' ,'U', 'V', 'W', 'X' ,'Y' ,'Z',
        '1', '2' ,'3' ,'4' ,'5', '6', '7', '8', '9' ,'0',',' ,';' ,':' ,'?', '!' ,'.' ,'@' ,'#', '$', '%' ,'&', '(', ')', '{', '}' ,'[', ']'
    ]
    Y = np.array(Y)
    Y_train = []
    for i in range(79):
        y = []
        for j in range(30):
            y+=Y[i]
        Y_train+=y
    Y_train = np.array(Y_train)
    return Y_train