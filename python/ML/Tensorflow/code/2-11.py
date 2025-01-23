import tensorflow as tf 
import numpy as np
from tensorflow.keras.utils import plot_model
import ssl # 오류 때문에 사용

# SSL 인증서 검증 비활성화(오류 때문에)
ssl._create_default_https_context = ssl._create_unverified_context

(trainX, trainY), (testX, testY) = tf.keras.datasets.fashion_mnist.load_data()

trainX = trainX / 255.0
testX = testX / 255.0

trainX = trainX.reshape( (trainX.shape[0], 28,28,1) )
testX = testX.reshape( (testX.shape[0], 28,28,1) )

# model = tf.keras.Sequential([
#     tf.keras.layers.Flatten(),
#     tf.keras.layers.Dense(128, activation='relu'),
#     tf.keras.layers.Dense(10, activation='softmax'),
# ])

input = tf.keras.layers.Input(shape= [28, 28])
flatten = tf.keras.layers.Flatten()(input)
dense1 = tf.keras.layers.Dense(28 * 28, activation = 'relu')(flatten)
reshape = tf.keras.layers.Reshape((28, 28))(dense1)
concat = tf.keras.layers.Concatenate()([input, reshape])
flatten2 = tf.keras.layers.Flatten()(concat)
output = tf.keras.layers.Dense(10, activation = 'softmax')(flatten2)
model = tf.keras.Model(input, output)

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['acc'])


input_shape=(28,28,1)
model.build(input_shape)
plot_model(model, to_file='model.png', show_shapes=True, show_layer_names=True)

model.fit(trainX, trainY, validation_data=(testX, testY), epochs=3)