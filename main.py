## Importing libraries
import math
import numpy as np
import matplotlib.pyplot as plt
from drawing_canvas import MyApp

# from tensorflow import keras

## Obtaining and normalizing the data
# data = keras.datasets.mnist
# (train_data, train_labels), (test_data, test_labels) = data.load_data()
#
# train_data = train_data / 255.0
# test_data = test_data / 255.0
#
# for train in range(len(train_data)):
#     for row in range(28):
#         for x in range(28):
#             if train_data[train][row][x] >= 0.5:
#                 train_data[train][row][x] = 1
#             else:
#                 train_data[train][row][x] = 0
#
# for train in range(len(test_data)):
#     for row in range(28):
#         for x in range(28):
#             if test_data[train][row][x] >= 0.5:
#                 test_data[train][row][x] = 1
#             else:
#                 test_data[train][row][x] = 0

## Creating, compiling, and fitting the model
# model = keras.Sequential([
#     keras.layers.Flatten(input_shape=(28, 28)),
#     keras.layers.Dense(128, activation='relu'),
#     keras.layers.Dense(16, activation='relu'),
#     keras.layers.Dense(10, activation='softmax')
# ])
#
# model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
#
# model.fit(train_data, train_labels, epochs=30)

## Saving the model
# model.save('digit_recognition_model')

## Getting the model
# model = keras.models.load_model('digit_recognition_model')

## Testing the model
# class_names = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#
# prediction = model.predict(test_data)
# for i in range(5):
#     plt.grid(False)
#     plt.imshow(test_data[i], cmap=plt.cm.binary)
#     plt.xlabel('Actual value: ' + class_names[test_labels[i]])
#     plt.title('Prediction: ' + class_names[np.argmax(prediction[i])])
#     plt.show()

## Predicting a single image
# prediction = model.predict([[test_data[7]]])
# print('Prediction: ', class_names[np.argmax(prediction)])

## Running the app
if __name__ == '__main__':
    MyApp().run()