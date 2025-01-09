import os
import tensorflow as tf
import shutil
from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras.utils import plot_model

'''
train_path = "./asset/Kaggle_dogs_vs_cats/train"
for i in os.listdir(train_path):

    if os.path.isdir(train_path + "/" + i):
        continue
    if "cat" in i :
        shutil.copyfile('./asset/Kaggle_dogs_vs_cats/train/' + i , './asset/Kaggle_dogs_vs_cats/train/cats/' + i)
    else :
        shutil.copyfile('./asset/Kaggle_dogs_vs_cats/train/' + i , './asset/Kaggle_dogs_vs_cats/train/dogs/' + i)
'''

train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    './asset/Kaggle_dogs_vs_cats//train/',
    image_size=(150, 150),
    batch_size=64,
    subset='training',
    validation_split=0.2,
    seed=2371
)

val_ds = tf.keras.preprocessing.image_dataset_from_directory(
    './asset//Kaggle_dogs_vs_cats/train/',
    image_size=(150, 150),
    batch_size=64,
    subset='validation',
    validation_split=0.2,
    seed=2371
)


def 전처리함수(i, 정답):
    i = tf.cast(i / 255.0, tf.float32)
    return i, 정답


train_ds = train_ds.map(전처리함수)
val_ds = val_ds.map(전처리함수)

inception_model = InceptionV3(input_shape=(150, 150, 3), include_top=False,
                              weights=None)  # 구글에서 만든 InceptionV3모델 불러오기. 단, 가중치 값은 안불러옴

inception_model.load_weights(
    "./asset/model/inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5")  # 가중치 데이터를 따로 불러옴

# inception_model.summary()

for i in inception_model.layers:
    i.trainable = False  # 학습 금지 레이어를 설정

unfreeze = False
for i in inception_model.layers:
    if i.name == 'mixed6':
        unfreeze = True
    if (unfreeze):
        i.trainable = True

final_layer = inception_model.get_layer("mixed7")

print(final_layer)

myFlatten = tf.keras.layers.Flatten()(final_layer.output)
myDense = tf.keras.layers.Dense(1024, activation='relu')(myFlatten)

drop1 = tf.keras.layers.Dropout(0.2)(myDense)
myDense2 = tf.keras.layers.Dense(1, activation="sigmoid")(drop1)

model = tf.keras.Model(inception_model.input, myDense2)

model.compile(loss="binary_crossentropy", optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001), metrics=["acc"])

# model.fit(train_ds, validation_data = val_ds, epochs = 2)

plot_model(model, to_file='model.png', show_shapes=True, show_layer_names=True)