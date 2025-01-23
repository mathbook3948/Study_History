import tensorflow as tf
import pandas as pd
from pandas import DataFrame
import numpy as np
from sklearn.model_selection import train_test_split


#PassengerId,HomePlanet,CryoSleep,Cabin,Destination,Age,VIP,RoomService,FoodCourt,ShoppingMall,Spa,VRDeck,Name,Transported
'''
PassengerId: 승객 고유 식별 번호
HomePlanet: 승객의 출발/고향 행성
CryoSleep: 동면 상태 여부
Cabin: 객실 번호/위치
Destination: 목적지 행성
Age: 승객의 나이
VIP: VIP 승객 여부
RoomService: 룸서비스 이용 관련 데이터
FoodCourt: 푸드코트 이용 관련 데이터
ShoppingMall: 쇼핑몰 이용 관련 데이터
Spa: 스파 이용 관련 데이터
VRDeck: VR 데크 이용 관련 데이터
Name: 승객 이름
Transported: 운송 완료 여부
'''
csv_data = pd.read_csv("spaceship-titanic/train.csv")
print(csv_data.head())

def homeplanet(homeplanet : DataFrame) :
    homeplanet_dict = {x: i for i, x in enumerate(homeplanet.unique())}
    homeplanet_dict[np.nan] = 3
    print(homeplanet_dict)
    return homeplanet.map(lambda x : homeplanet_dict[x])

def deck(deck : DataFrame) :
    deck_dict = {x : i for i, x in enumerate(deck.unique())}
    print(deck_dict)
    deck_dict[np.nan] = len(deck_dict)
    return deck.map(lambda x : deck_dict[x])

def destination(destination : DataFrame) :
    destination_dict = {x : i for i, x in enumerate(destination.unique())}
    print(destination_dict)
    destination_dict[np.nan] = len(destination_dict)
    return destination.map(lambda x : destination_dict[x])

#HomePlanet
csv_data["HomePlanet"] = homeplanet(csv_data["HomePlanet"])

#CryoSleep
csv_data["CryoSleep"] = csv_data["CryoSleep"].map(lambda x : 1 if bool(x) else 0)

#Destination
csv_data["Destination"] = destination(csv_data["Destination"])
print(csv_data)

# ====================================================이 뒤는 Claude

# Age - 정규화
csv_data["Age"] = csv_data["Age"].fillna(csv_data["Age"].mean())  # 결측값은 평균값으로
csv_data["Age"] = csv_data["Age"] / csv_data["Age"].max()  # 최대값으로 나누어 정규화

# VIP - 이진값으로 변환
csv_data["VIP"] = csv_data["VIP"].map(lambda x: 1 if bool(x) else 0)

# 소비 관련 컬럼들 (RoomService, FoodCourt, ShoppingMall, Spa, VRDeck)
spend_columns = ["RoomService", "FoodCourt", "ShoppingMall", "Spa", "VRDeck"]
for column in spend_columns:
    # 결측값은 평균값으로
    csv_data[column] = csv_data[column].fillna(csv_data[column].mean())
    # 최대값으로 나누어 정규화
    csv_data[column] = csv_data[column] / csv_data[column].max()

# Name 컬럼은 필요없다면 삭제
csv_data = csv_data.drop("Name", axis=1)

# PassengerId - 필요없다면 삭제
csv_data = csv_data.drop("PassengerId", axis=1)

# Transported - 이진값으로 변환 (타겟 변수)
csv_data["Transported"] = csv_data["Transported"].map(lambda x: 1 if x else 0)

# Cabin
csv_data = csv_data.dropna(subset=['Cabin']).reset_index(drop=True)  # reset_index 추가
cabin = csv_data["Cabin"].tolist()
cabin = [i.split("/") for i in cabin]

cabin_df = pd.DataFrame(cabin, columns=['Deck', 'Num', 'Side'])
cabin_df["Deck"] = deck(cabin_df["Deck"])
cabin_df["Num"] = cabin_df["Num"].astype("float64")
maxNum = cabin_df["Num"].max()
cabin_df["Num"] = cabin_df["Num"].map(lambda x : x / maxNum)
# P : 0, S : 1
cabin_df["Side"] = cabin_df["Side"].map(lambda x : 0 if x == "P" else 1)

# Cabin 컬럼들을 원본 데이터프레임에 추가
csv_data["Deck"] = cabin_df["Deck"]
csv_data["Cabin_Num"] = cabin_df["Num"]
csv_data["Cabin_Side"] = cabin_df["Side"]
csv_data = csv_data.drop("Cabin", axis=1)  # 원본 Cabin 컬럼 삭제

print("전처리 완료된 데이터 shape:", csv_data.shape)
print("\n각 컬럼의 데이터 타입:")
print(csv_data.dtypes)
print("\n결측치 확인:")
print(csv_data.isnull().sum())

csv_data = csv_data.astype("float64")

x = csv_data.drop("Transported", axis=1)
y = csv_data["Transported"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=456)

x_train = tf.convert_to_tensor(x_train, dtype=tf.float64)
y_train = tf.convert_to_tensor(y_train, dtype=tf.float64)
x_test = tf.convert_to_tensor(x_test, dtype=tf.float64)
y_test = tf.convert_to_tensor(y_test, dtype=tf.float64)

def create_dataset(x, y, batch_size=32, shuffle=True, buffer_size=1000):
    dataset = tf.data.Dataset.from_tensor_slices((x, y))
    if shuffle:
        dataset = dataset.shuffle(buffer_size)
    dataset = dataset.batch(batch_size).prefetch(tf.data.AUTOTUNE)
    return dataset

BATCH_SIZE = 32
train_dataset = create_dataset(x_train, y_train, BATCH_SIZE)
test_dataset = create_dataset(x_test, y_test, BATCH_SIZE, shuffle=True)

print(x_train.shape)

input = tf.keras.layers.Input(shape=[13])
x = tf.keras.layers.Dense(32, activation='relu')(input)
x = tf.keras.layers.Dense(64, activation='relu')(x)
x = tf.keras.layers.Dropout(0.3)(x)
x = tf.keras.layers.Concatenate()([x, input])
x = tf.keras.layers.Dense(128, activation='relu')(x)
x = tf.keras.layers.Dropout(0.3)(x)
x = tf.keras.layers.Concatenate()([x, input])
x = tf.keras.layers.Dense(64, activation='relu')(x)
x = tf.keras.layers.Dense(32, activation='relu')(x)

output = tf.keras.layers.Dense(1, activation='sigmoid')(x)

model = tf.keras.Model(inputs=input, outputs=output)

model.summary()

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["acc"])

model.fit(train_dataset, validation_data=test_dataset, epochs=40)

model.evaluate(x_test, y_test)

model.save("model.h5")
