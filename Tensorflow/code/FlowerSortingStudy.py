import tensorflow as tf

# 데이터셋 불러오기
train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    directory = "./asset/flower",
    image_size = (250, 250),
    batch_size = 32,
    subset = "training",
    validation_split = 0.2,
    seed = 2371
)

valid_ds = tf.keras.preprocessing.image_dataset_from_directory(
    directory = "./asset/flower",
    image_size = (250, 250),
    batch_size = 32,
    subset = "validation",
    validation_split = 0.2,
    seed = 2371
)

# 전처리 함수
def 전처리함수(i, 정답):
    i = tf.cast(i / 255.0, tf.float32)  # 정규화
    return i, 정답

train_ds = train_ds.map(전처리함수)
valid_ds = valid_ds.map(전처리함수)

# 모델 정의
input = tf.keras.layers.Input(shape=[250, 250, 3])
conv1 = tf.keras.layers.Conv2D(32, (3, 3), padding='same', activation='relu')(input)
pooling1 = tf.keras.layers.MaxPooling2D((2, 2))(conv1)
conv2 = tf.keras.layers.Conv2D(32, (3, 3), padding='same', activation='relu')(pooling1)
pooling2 = tf.keras.layers.MaxPooling2D((2, 2))(conv2)
conv3 = tf.keras.layers.Conv2D(32, (3, 3), padding='same', activation='relu')(pooling2)
pooling3 = tf.keras.layers.MaxPooling2D((2, 2))(conv3)

# Resize 후 채널을 맞추기 위해 Conv2D 사용
resize = tf.keras.layers.Resizing(250, 250)(pooling3)
resize = tf.keras.layers.Conv2D(3, (1, 1), padding='same')(resize)  # 채널 맞추기

# Concatenate 레이어
concat = tf.keras.layers.Concatenate()([resize, input])

# Flatten 후 Dense 레이어
flatten1 = tf.keras.layers.Flatten()(concat)
dense1 = tf.keras.layers.Dense(128, activation="relu", name="dense1")(flatten1)

# 출력 레이어
output = tf.keras.layers.Dense(5, activation="softmax")(dense1)

# 모델 컴파일 및 학습
model = tf.keras.Model(input, output)
model.summary()

model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["acc"])
model.fit(train_ds, validation_data=valid_ds, epochs=10)