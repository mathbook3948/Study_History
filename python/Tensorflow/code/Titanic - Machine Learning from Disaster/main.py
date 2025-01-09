import math

import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split

#PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
#승객번호,생존여부(0=사망1=생존),좌석등급(1=1등2=2등3=3등),이름,성별,나이,동승한가족수(형제자매배우자),동승한가족수(부모자녀),티켓번호,운임,객실번호,탑승항(C=셰르부르Q=퀸즈타운S=사우샘프턴)
train = pd.read_csv("./titanic/train.csv")
train['Age'] = train['Age'].fillna(train['Age'].mean())
maxAge = train['Age'].max()
train["Age"] = train['Age'].map(lambda x : x / maxAge)
train["Age"] = train["Age"].map(lambda x : round(x, 3))
train["Sex"] = train["Sex"].map({"male" : 0, "female" : 1})

x = train[["Pclass", "Sex", "Age", "SibSp", "Parch"]].values
y = train["Survived"]

x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.2, random_state=456)

x_train = x_train.astype('float32')
x_val = x_val.astype('float32')
y_train = y_train.astype('float32')
y_val = y_val.astype('float32')

x_train = tf.reshape(x_train, (-1, 1, 5))
x_val = tf.reshape(x_val, (-1, 1, 5))

x_train = tf.convert_to_tensor(x_train, dtype=tf.float32)
y_train = tf.convert_to_tensor(y_train, dtype=tf.float32)
x_val = tf.convert_to_tensor(x_val, dtype=tf.float32)
y_val = tf.convert_to_tensor(y_val, dtype=tf.float32)

input = tf.keras.layers.Input(shape=[1, 5])

# 초기 특성 추출
dense1 = tf.keras.layers.Dense(32, activation="relu", name="dense1")(input)
dense2 = tf.keras.layers.Dense(64, activation="relu", name="dense2")(dense1)
dense3 = tf.keras.layers.Dense(128, activation="relu", name="dense3")(dense2)

# 첫 번째 스킵 커넥션 - axis=2로 수정 (특성 차원에서 연결)
concat = tf.keras.layers.Concatenate(axis=2)([dense3, input])
flatten = tf.keras.layers.Flatten()(concat)
dropout1 = tf.keras.layers.Dropout(0.4)(flatten)

# 중간 처리
dense4 = tf.keras.layers.Dense(256, activation="relu", name="dense4")(dropout1)
dense5 = tf.keras.layers.Dense(128, activation="relu", name="dense5")(dense4)
dense6 = tf.keras.layers.Dense(64, activation="relu", name="dense6")(dense5)

# 마지막 층
dense7 = tf.keras.layers.Dense(32, activation="relu", name="dense7")(dense6)
output = tf.keras.layers.Dense(1, activation="sigmoid")(dense7)

model = tf.keras.Model(input, output)

model.summary()
model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["acc"])

model.fit(x_train, y_train, validation_data=(x_val, y_val), epochs=60)

train = pd.read_csv("./titanic/test.csv")
train['Age'] = train['Age'].fillna(train['Age'].mean())
maxAge = train['Age'].max()
train["Age"] = train['Age'].map(lambda x : x / maxAge)
train["Age"] = train["Age"].map(lambda x : round(x, 3))
train["Sex"] = train["Sex"].map({"male" : 0, "female" : 1})

x = train[["Pclass", "Sex", "Age", "SibSp", "Parch"]].values
x = x.astype('float32')
x = tf.reshape(x, (-1, 1, 5))
x = tf.convert_to_tensor(x, dtype=tf.float32)

predictions = model.predict(x)

# 예측 결과를 0 또는 1로 변환 (0.5를 임계값으로 사용)
predictions_binary = (predictions > 0.5).astype(int)

# 제출 파일 생성
submission = pd.DataFrame({
    'PassengerId': train['PassengerId'],
    'Survived': predictions_binary.flatten()
})

submission.to_csv('submission.csv', index=False)