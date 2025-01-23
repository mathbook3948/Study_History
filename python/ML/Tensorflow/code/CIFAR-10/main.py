import tensorflow as tf
import numpy as np

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()

x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test = tf.keras.utils.to_categorical(y_test, 10)

class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']

input = tf.keras.layers.Input(shape=[32, 32, 3])

flip = tf.keras.layers.RandomFlip(mode='horizontal')(input)
rotate = tf.keras.layers.RandomRotation(factor=0.2)(flip)
brght = tf.keras.layers.RandomBrightness(factor=0.2)(rotate)

r = tf.keras.layers.Lambda(lambda x: x[..., 0:1])(brght)
g = tf.keras.layers.Lambda(lambda x: x[..., 1:2])(brght)
b = tf.keras.layers.Lambda(lambda x: x[..., 2:3])(brght)

r_conv1 = tf.keras.layers.Conv2D(32, (1, 1), padding='same', activation='relu')(r)
r_conv2 = tf.keras.layers.Conv2D(64, (3, 3), padding='same', activation='relu')(r_conv1)
r_conv3 = tf.keras.layers.Conv2D(32, (1, 1), padding='same', activation='relu')(r_conv2)

g_conv1 = tf.keras.layers.Conv2D(32, (1, 1), padding='same', activation='relu')(g)
g_conv2 = tf.keras.layers.Conv2D(64, (3, 3), padding='same', activation='relu')(g_conv1)
g_conv3 = tf.keras.layers.Conv2D(32, (1, 1), padding='same', activation='relu')(g_conv2)

b_conv1 = tf.keras.layers.Conv2D(32, (1, 1), padding='same', activation='relu')(b)
b_conv2 = tf.keras.layers.Conv2D(64, (3, 3), padding='same', activation='relu')(b_conv1)
b_conv3 = tf.keras.layers.Conv2D(32, (1, 1), padding='same', activation='relu')(b_conv2)

concat1 = tf.keras.layers.Concatenate()([r_conv3, g_conv3, b_conv3])

conv1 = tf.keras.layers.Conv2D(32, (3, 3), padding='same', activation='relu')(concat1)
pooling1 = tf.keras.layers.MaxPooling2D((2, 2))(conv1)
conv2 = tf.keras.layers.Conv2D(32, (3, 3), padding='same', activation='relu')(pooling1)
pooling2 = tf.keras.layers.MaxPooling2D((2, 2))(conv2)
conv3 = tf.keras.layers.Conv2D(32, (3, 3), padding='same', activation='relu')(pooling2)
pooling3 = tf.keras.layers.MaxPooling2D((2, 2))(conv3)

flatten = tf.keras.layers.Flatten()(pooling3)
dense1 = tf.keras.layers.Dense(128, activation="relu")(flatten)
output = tf.keras.layers.Dense(10, activation="softmax")(dense1)

model = tf.keras.Model(input, output)
model.summary()

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["acc"])

model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=10)
