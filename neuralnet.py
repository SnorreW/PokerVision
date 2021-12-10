import numpy as np
from PIL import ImageGrab
import os
import cv2
from PIL import Image
import Cards
import tensorflow as tf
import emnist
from keras.utils import np_utils
'''
x_train2, y_train2 = emnist.extract_training_samples('letters')
x_test2, y_test2 = emnist.extract_test_samples('letters')


J = []
Q = []
K = []
A = []

for i in range(len(x_train2)):
    if y_train2[i] == 10:
        J.append(x_train2[i])
    elif y_train2[i] == 17:
        Q.append(x_train2[i])
    elif y_train2[i] == 11:
        K.append(x_train2[i])
    elif y_train2[i] == 1:
        A.append(x_train2[i])



#data
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

###############tens#######################
zeros = []
ones = []
twos = []
threes = []
fours = []
fives = []
sixs = []
sevens = []
eights = []
nines = []

for i in range(len(x_train)):
    if y_train[i] == 0:
        zeros.append(x_train[i])
    elif y_train[i] == 1:
        ones.append(x_train[i])
    elif y_train[i] == 2:
        twos.append(x_train[i])
    elif y_train[i] == 3:
        threes.append(x_train[i])
    elif y_train[i] == 4:
        fours.append(x_train[i])
    elif y_train[i] == 5:
        fives.append(x_train[i])
    elif y_train[i] == 6:
        sixs.append(x_train[i])
    elif y_train[i] == 7:
        sevens.append(x_train[i])
    elif y_train[i] == 8:
        eights.append(x_train[i])
    elif y_train[i] == 9:
        nines.append(x_train[i])

tens = []
k = 0
while 5923 > k:
    tens.append(cv2.resize(np.concatenate((ones[k], zeros[k]), axis=1), (28, 28)))
    k += 1
#print(x_train[0].shape)

#######################################
twosLabel = [2] * len(twos)
threesLabel = [3] * len(threes)
foursLabel = [4] * len(fours)
fivesLabel = [5] * len(fives)
sixsLabel = [6] * len(sixs)
sevensLabel = [7] * len(sevens)
eightsLabel = [8] * len(eights)
ninesLabel = [9] * len(nines)
tensLabel = [10] * len(tens)
JLabel = [11] * len(J)
QLabel = [12] * len(Q)
KLabel = [13] * len(K)
ALabel = [14] * len(A)

y_train = twosLabel + threesLabel + foursLabel + fivesLabel + sixsLabel + sevensLabel + eightsLabel + ninesLabel + tensLabel + JLabel + QLabel + KLabel + ALabel
x_train = twos + threes + fours + fives + sixs + sevens + eights + nines + tens + J + Q + K + A
########test#############

JT = []
QT = []
KT = []
AT = []

for i in range(len(x_test2)):
    if y_test2[i] == 10:
        JT.append(x_test2[i])
    elif y_test2[i] == 17:
        QT.append(x_test2[i])
    elif y_test2[i] == 11:
        KT.append(x_test2[i])
    elif y_test2[i] == 1:
        AT.append(x_test2[i])


###############tens#######################
zerosT = []
onesT = []
twosT = []
threesT = []
foursT = []
fivesT = []
sixsT = []
sevensT = []
eightsT = []
ninesT = []

for i in range(len(x_test)):
    if y_test[i] == 0:
        zerosT.append(x_test[i])
    elif y_test[i] == 1:
        onesT.append(x_test[i])
    elif y_test[i] == 2:
        twosT.append(x_test[i])
    elif y_test[i] == 3:
        threesT.append(x_test[i])
    elif y_test[i] == 4:
        foursT.append(x_test[i])
    elif y_test[i] == 5:
        fivesT.append(x_test[i])
    elif y_test[i] == 6:
        sixsT.append(x_test[i])
    elif y_test[i] == 7:
        sevensT.append(x_test[i])
    elif y_test[i] == 8:
        eightsT.append(x_test[i])
    elif y_test[i] == 9:
        ninesT.append(x_test[i])

tensT = []
k = 0

while 980 > k:
    tensT.append(cv2.resize(np.concatenate((onesT[k], zerosT[k]), axis=1), (28, 28)))
    k += 1
#print(x_train[0].shape)
twosLabelT = [2] * len(twosT)
threesLabelT = [3] * len(threesT)
foursLabelT = [4] * len(foursT)
fivesLabelT = [5] * len(fivesT)
sixsLabelT = [6] * len(sixsT)
sevensLabelT = [7] * len(sevensT)
eightsLabelT = [8] * len(eightsT)
ninesLabelT = [9] * len(ninesT)
tensLabelT = [10] * len(tensT)
JLabelT = [11] * len(JT)
QLabelT = [12] * len(QT)
KLabelT = [13] * len(KT)
ALabelT = [14] * len(AT)

y_test = twosLabelT + threesLabelT + foursLabelT + fivesLabelT + sixsLabelT + sevensLabelT + eightsLabelT + ninesLabelT + tensLabelT #+ JLabelT + QLabelT + KLabelT + ALabelT
x_test = twosT + threesT + foursT + fivesT + sixsT + sevensT + eightsT + ninesT + tensT #+ JT + QT + KT + AT
#######################################
twosLabel = [2] * len(twos)
threesLabel = [3] * len(threes)
foursLabel = [4] * len(fours)
fivesLabel = [5] * len(fives)
sixsLabel = [6] * len(sixs)
sevensLabel = [7] * len(sevens)
eightsLabel = [8] * len(eights)
ninesLabel = [9] * len(nines)
tensLabel = [10] * len(tens)
JLabel = [11] * len(J)
QLabel = [12] * len(Q)
KLabel = [13] * len(K)
ALabel = [14] * len(A)

y_train = twosLabel + threesLabel + foursLabel + fivesLabel + sixsLabel + sevensLabel + eightsLabel + ninesLabel + tensLabel #+ JLabel + QLabel + KLabel + ALabel
x_train = twos + threes + fours + fives + sixs + sevens + eights + nines + tens #+ J + Q + K + A
'''
####################
#mnist = tf.keras.datasets.mnist
#(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = []
for i in os.listdir('data'):
    pic = cv2.imread('data/{}'.format(i))
    x_train.append(pic)

print(x_train[3].shape)
print(x_train[10].shape)
cv2.imshow("test", x_train[3])
cv2.waitKey(0)
cv2.destroyAllWindows()

x_train = np.array(x_train)

y_train = ['2','3','4','5','6','7','8','9','10','A','J','K','Q']
x_train = tf.keras.utils.normalize(x_train, axis=1)
#x_test = tf.keras.utils.normalize(x_test, axis=1)

#print(y_train[0].shape)
print(x_train[10].shape)
cv2.imshow("test", x_train[4])
cv2.waitKey(0)
cv2.destroyAllWindows()
#model
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
model.add(tf.keras.layers.Dense(128, activation='relu'))
model.add(tf.keras.layers.Dense(128, activation='relu'))
model.add(tf.keras.layers.Dense(10, activation='softmax'))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics = ['accuracy'])
#train
model.fit(x_train, y_train, epochs=3)

#loss, accuracy = model.evaluate(x_test, y_test)
#print(accuracy)
#print(loss)

model.save('digits.model')