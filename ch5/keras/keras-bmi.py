from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.callbacks import EarlyStopping
import pandas as pd, numpy as np

csv = pd.read_csv('bmi.csv')
csv['weight'] /= 100
csv['height'] /= 200
X = csv[['weight', 'height']].as_matrix()

bclass = {'thin': [1, 0, 0], 'normal': [0, 1, 0], 'fat': [0, 0, 1]}
y = np.empty((20000, 3))
for i, v in enumerate(csv['label']):
    y[i] = bclass[v]

X_train, y_train = X[1:15001], y[1:15001]
X_test, y_test = X[15001:20001], y[15001:20001]

model = Sequential()
model.add(Dense(512, input_shape=(2,)))
model.add(Activation('relu'))
model.add(Dropout(0.1))

model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.1))

model.add(Dense(3))
model.add(Activation('softmax'))

model.compile(
    loss='categorical_crossentropy',
    optimizer='rmsprop',
    metrics=['accuracy']
)

hist = model.fit(
    X_train, y_train,
    batch_size=100,
    nb_epoch=20,
    validation_split=0.1,
    callbacks=[EarlyStopping(monitor='val_loss', patience=2)],
    verbose=1
)

score = model.evaluate(X_test, y_test)
print('loss=', score[0])
print('accuracy=', score[1])
