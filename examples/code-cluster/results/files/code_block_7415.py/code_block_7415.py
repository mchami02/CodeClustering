from keras import Sequential
from keras.layers import Dense

model = Sequential()
model.add(Dense(units=20, activation='relu', input_dim=X.shape[1]))
model.add(Dense(units=10, activation='relu'))
model.add(Dense(units=3, activation='softmax'))
model.compile(optimizer='rmsprop',
             loss='categorical_crossentropy',
             metrics=['accuracy'])