import tensorflow as tf
import numpy as np
import pandas as pd
from pandas import DataFrame

csv_data = pd.read_csv("spaceship-titanic/test.csv")
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

# PassengerId 저장
origin_num = csv_data["PassengerId"].copy()

#HomePlanet
csv_data["HomePlanet"] = homeplanet(csv_data["HomePlanet"])

#CryoSleep
csv_data["CryoSleep"] = csv_data["CryoSleep"].map(lambda x : 1 if bool(x) else 0)

#Destination
csv_data["Destination"] = destination(csv_data["Destination"])

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

# Name 컬럼은 삭제
csv_data = csv_data.drop("Name", axis=1)

# PassengerId 삭제
csv_data = csv_data.drop("PassengerId", axis=1)

# Cabin 처리 - 결측치를 특별한 값으로 대체
csv_data['Cabin'] = csv_data['Cabin'].fillna('Z/0/Z')  # 결측치를 특별한 값으로 대체
cabin = csv_data["Cabin"].str.split('/', expand=True)
cabin.columns = ['Deck', 'Num', 'Side']

# Deck 처리
cabin["Deck"] = deck(cabin["Deck"])

# Num 처리
cabin["Num"] = pd.to_numeric(cabin["Num"], errors='coerce')
cabin["Num"] = cabin["Num"] / cabin["Num"].max()  # 정규화

# Side 처리 (P:0, S:1, Z:2)
cabin["Side"] = cabin["Side"].map({'P': 0, 'S': 1, 'Z': 2})

# Cabin 컬럼들을 원본 데이터프레임에 추가
csv_data["Deck"] = cabin["Deck"]
csv_data["Cabin_Num"] = cabin["Num"]
csv_data["Cabin_Side"] = cabin["Side"]
csv_data = csv_data.drop("Cabin", axis=1)  # 원본 Cabin 컬럼 삭제

print("전처리 완료된 데이터 shape:", csv_data.shape)
print("\n각 컬럼의 데이터 타입:")
print(csv_data.dtypes)
print("\n결측치 확인:")
print(csv_data.isnull().sum())

# 모든 컬럼을 float64로 변환
csv_data = csv_data.astype("float64")

# 결측치가 있다면 0으로 채우기
csv_data = csv_data.fillna(0)

# 텐서로 변환
x = tf.convert_to_tensor(csv_data, dtype=tf.float64)

# 모델 로드
model = tf.keras.models.load_model("model.h5")

# 예측
predictions = model.predict(x)

# 예측 결과를 True 또는 False로 변환
predictions_boolean = predictions > 0.5

# 제출 파일 생성
submission = pd.DataFrame({
    'PassengerId': origin_num,
    'Transported': predictions_boolean.flatten()
})

submission.to_csv('submission.csv', index=False)