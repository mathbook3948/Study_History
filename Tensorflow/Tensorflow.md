# Tensorflow 란?
- 구글에서 만든 딥러닝 프로그램을 쉽게 구현할 수 있도록 기능을 제공하는 라이브러리'
# Tensorflow를 하기 전에 기초
## 머신러닝 이란?
- 단순히 뭔가 수학적인 계산을 통해 실제 결과와 예측한 결과의 오차를 찾는 행위를 컴퓨터에게 시키는 것이다.
## 학습 방법의 종류
### Supervised Learning(지도학습)
- 데이터에 정답이 있고, 정답을 맞추거나 정답일 확률을 구하는 모델을 만들 때 사용
### Unsupervised Learning(비지도 학습)
- 데이터에 정답이 없고 알아서 비슷한것 끼리 분류를 하는 모델을 만들 때 사용
### Reinforcement Learning(강화 학습)
- 특정 행동을 할때마다 보상을 주고, 이 보상을 최대화 하는 방식으로 행동하는 모델을 만들 때 사용
### Transfer Learning(전이 학습)
- 기존에 있던 성능 좋은 모델을 가져와서 가중치, 원하는 레이어 등을 뽑아와서 더 성능이 좋은 모델을 만드는 방법
## 용어 및 개념
### 가중치(W)
- 어떤 데이터가 결과에 미치는 영향력
### 편향(Bias) 과 분산(Variance)
- 예측 모델의 복잡성과 일반화 능력 사이의 균형을 설명하는 개념이다. 
- 편향은 모델의 예측이 얼마나 학습한 데이터에 떨어져 있는지(차이가 나는지)를 나타낸다
- 분산은 모델의 예측이 얼마나 데이터의 변화에 민감한지(실제 데이터하고 얼마나 일치하는지)를 나타낸다
#### 편향이 낮고 분산이 높은 경우
- 학습 데이터를 향해 모델의 결과가 분산되어 있어서 새로운 데이터를 만났을 때 과적합 될 수 있다.
#### 편향이 높고 분산이 낮은 경우
- 모든 학습 데이터의 중간 정도로 모델의 결과가 모여 있어서 데이터의 복잡한 구조를 제대로 반영하지 못할 수 있다.
### 활성화 함수(Activation_function)
- 데이터를 의도적으로 변형시키서 복잡한 예측을 가능하게 해주는 함수.
- 활성화 함수가 없을 경우 선형적인 예측만 가능하다(아무리 복잡한 구조여도 식을 정리하고 치환한다면 1차함수 모양으로 나온다)
### 손실 함수
- 오차들을 계산을 통해 평균을 내는 역할을 하는 함수
### 경사하강법
![Pasted image 20241108224009](https://github.com/user-attachments/assets/f7cc6100-b1de-4d19-979b-faef5995b599)
-  이 그래프는 가로가 가중치, 세로가 오차를 뜻한다.
- 가중치를 변경할 때 마다 오차가 변하는데 조금씩 가중치를 변경해서 가장 오차가 작은(y값이 가장 작은) 오차를 찾아야 한다. 이때, 높은 곳에서 경사를 타고 내려오듯이 점점 내려오면 되는 것 아닌가? 즉, 조금씩 가중치를 조절해 경사를 타고 가장 낮은 오차를 찾는것이 경사 하강법이다
#### 방법
1. 초기 가중치를 랜덤으로 설정한다.
2. 가중치를 바탕으로 오차를 계산한다. 
3. 경사하강법을 이용하여 새로운 가중치를 업데이트한다.
4. 더 이상 학습(오차를 줄어들게 하는 것)이 이루어지지 않을 때까지 반복한다.
- 새로운 가중치를 업데이트 하는 법은 기존 가중치에서 기존 가중치의 변화가 오차에 얼마나 큰 영향을 미치는가를 빼서 구한다(접선의 기울기, 편미분 을 뺀다). 
$$
w = w - 기울기
$$
#### 문제점
- 위의 그래프에서 왼쪽의 가장 높은 부분에서 오른쪽으로 내려왔다고 가정하면 어느정도 가중치를 크게 만들다 보면 오차가 다시 증가하는 부분이 생긴다. 이러면 경사하강법은 여기서 끝난것이다.
- 우리가 원하는 결과는 위의 결과보다 더 나은 그래프에서 약간 오른쪽에 위치한 부분을 원한다. 그래서 가중치를 업데이트 할 때 기울기에 일정한 수를 곱해서 언덕을 넘어버릴 수 있게 해야 한다. 이 곱해지는 수를 Learning Rate라고 한다.
- 하지만 고정된 수의 경우에는 복잡한 문제에서 학습이 안일어나는 문제가 있을 수 있으므로 가변적인 값을 곱해주어야 한다. 
##### Learning Rate Optimizer
- Learning Rate를 가변적으로 상황에 맞게 변경해 주는 알고리즘을 뜻한다. 
### 과적합(Overfitting)
- 반복적으로 같거나 비슷한 데이터만 훈련시키면 그 데이터에 익숙해져서 답을 외워버리는 현상을 말한다.
### 데이터 전처리
- 데이터 중간에 값이 없는 등 학습에 영향을 주는 요소들을 제거, 또는 학습이 더 잘 이루어지도록 데이터를 미리 처리 해두는 것을 말한다.
### 파라미터 튜닝
- 모델의 성능을 최적화 하기 위하여 Learning Rate, epochs, 등 조절 가능한 값을 조절 하는 것이다. 또한, 확률을 예측하는 모델의 경우 학습데이터를 0~1로 조절(적절한 값을 나누는 등)하는 방법이 있다

### CNN(Convolutional Neural Network)
- 이미지 같은 것을 예측하거나 할 때 2차원 이상의 데이터를 Flatten 레이어로 1차원으로 만들어야 하는 경우가 생긴다.
- 이미지를 일자로 나열한다면 규칙이 깨져서 유연한 모델을 만들기 힘들어진다
#### 해결책
1. 이미지의 중요한 정보를 추려서 복사본을 만든다. 각 이미지는 원본 이미지의 특성을 강조하는 성격을 지니고 있다.
2. 이미지 정보를 중앙으로 모으는 Pooling 레이어를 거친다
3. 중앙으로 모인 정보를 바탕으로 Flatten 레이어를 거친다.

##### 1. 이미지의 복사본 생성
```python
tf.keras.layers.Conv2D(복사본갯수, (kernal_x, kernal_y), [padding = "same"], activation = 'relu') 
# padding : kernal을 적용하면 크기가 작아질 수 밖에 없는데, 작아진 만큼 padding을 추가해주는 설정을 할 수 있다.
# activation = 'relu' : 이미지의 rgb는 0~255 이여서 음수가 나오지 않게 설정한다
```
##### 2. 이미지 정보를 중앙으로 모으는 Pooling 레이어
```python
tf.keras.layers.MaxPooling2D((x,y))  #가장 큰 값을 중앙으로 모음
# x, y : 2, 2일 경우 2,2 x 4개. 즉, 4, 4 -> 2,2를 진행한다
```
# 함수, 알고리즘들
## Learning Rate Optimizer
### Momentum
- 가중치가 변하는 값을 분석하여 가속도를 붙여준다
- 예를 들어 한 경사가 높아서 가중치가 급격하게 변할 경우 그 가속도를 인식하고 Learning Rate에 반영한다. 
### AdaGrad
- 자주 변하는 가중치는 작게, 자주 변하지 않는 가중치는 경사하강법의 문제점에 빠졌다고 판단하여 크게 변화시켜 준다
### RMSProp
//TODO
### Adam
- 가장 자주 쓰인다(왜그런지 //TODO)
## Loss Function(손실 함수)
### binary_crossentropy
//TODO
## Activation Function(활성화 함수)
### Sigmoid(시그모이드)
- 0~1 사이로 값을 만들어준다. (0, 0.5)에서 만나며, 이후 x가 증가할 때 1에 가까워지고, x가 감소할 때 0에 가까워진다.
- 0과 1 사이로 추려지기에 확률 문제에 적합하다.
### ReLU(Rectified Linear Unit, 경사 함수) 
- 음수는 0으로 처리하고 x가 0일때부터는 기울기가 1인 일차함수로 표현된다.


<!-- ------------------------------------------------- -->


# Tensorflow 메인
- 일반적으로 `import tensorflow as tf`로 짧게 바꿔서 불러온다
## tensor 자료형
- 숫자, 리스트(숫자) 등의 데이터를 담는 곳이다.
- 자료의 차원(리스트 안에 리스트 안에 리스트)이 높아져도 계산을 쉽게 할 수 있다(자동을 해줌)
### 관련 함수
#### tf
- `.constant(data, [dtype=])` : 데이터(숫자)를 받아 tensor 자료형으로 바꿔서 반환한다. dtype으로 데이터 타입을 지정할 수도 있다. 값을 변경할 수 없다
- `.Variable(data, [dtype=])` : `.constant()`와 거의 비슷하지만 값을 변경할 수 있다
- `.add(t1,t2)` : 합연산을 하고 결과를 반환한다.
- `.subtract(t1,t2)` : t1에서 t2를 뺀 결과를 반환한다
- `.divide(t1,t2)` : t1에서 t2를 나눈 결과를 반환한다
- `.multiply(t1,t2)` : 곱연산을 하고 결과를 반환한다.
- `.matmul(t1, t2)` : 행렬의 곱(dot product)을 하고 결과를 반환한다
- `.zeros([..., 2차원 갯수, 1차원 0의 갯수])` : 0으로 가득찬 tensor을 만들어준다
#### 기타
- `.shape()` : tensor의 모양을 리스트 형태로 반환해준다.
- `.cast(tensor, dtype=)` : tensor 변수와 dtype을 받아 원하는 타입의 tensor로 변환할 수 있다
- `.numpy()` : tensor 변수를 numpy 배열로 변환해서 반환한다
- `.assign(data)` : 선택된 Variable 변수의 값을 data로 바꾼다.
## Keras
- Tensorflow 내에 포함된 라이브러리로, 신경망 모델을 쉽게 만들 수 있게 도와준다.
### Keras를 이용하여 모델 만들기
0. 데이터 전처리 하기
1. 모델의 신경망 레이어 만들기
2. Optimizer, 손실함수 정하기
3. 학습하기
4. 모델을 이용한 예측하기
#### 데이터 전처리 하기
- 먼저 데이터 사이에 빈 값이나 `null` 이 있는지 확인하고 제거하거나 평균값 등을 넣어준다(`.fillna()`, `.dropna()` 등을 사용할 수 있다)
- 데이터 준비가 끝나면, numpy 배열로 데이터를 준비시킨다.
##### `tf.keras.preprocessing`
###### `.image_dataset_from_directory()`
- 폴더에 저장된 이미지 파일을 데이터셋으로 로드할 수 있게 해주는 함수
- 경로에 폴더별로 이미지를 나눠주면 자동으로 라벨링 해준다
```python
#매개변수
directory = "" # 데이터셋으로 만들기 원하는 사진의 폴더의 경로
image_size = (x, y) #
barch_size = batch_size # 한번에 처리할 이미지의 갯수를 정함
subset = "" # training과 validation을 넣을 수 있으며, 데이터를 훈련용과 검증용으로 나누기 위해 사용한다. 보통 seed, validation_split 매개변수를 같게 설정한다
validation_split = 0 ~ 1 # 0에서 1 사이의 값을 넣을 수 있으며, validation 데이터의 비율을 결정한다
seed = seed # 데이터를 나눌 시드를 정한다


```
#### 모델의 신경망 레이어 만들기
- 모델의 틀을 선택하고, 레이어들을 채운다
- 첫 레이어에는 `input_shape` 속성을 주는 것이 좋다. 입력되는 데이터의 형태를 입력 받는다.
- 마지막 레이어의 노드의 갯수는 원하는 결과의 갯수와 같게 해야 한다.
##### 모델
- `.Sequential([])` : 가장 기본적인 모델. 단순히 순서대로 레이어가 배열된다
```python
input = tf.keras.layers.Input(shape= [28, 28])
flatten1 = tf.keras.layers.Flatten()(input)
dense1 = tf.keras.layers.Dense(28 * 28, activation = 'relu')(flatten1)
reshape = tf.keras.layers.Reshape((28, 28))(dense1)
concat = tf.keras.layers.Concatenate()([input, reshape])
flatten2 = tf.keras.layers.Flatten()(concat)
output = tf.keras.layers.Dense(10, activation = 'softmax')(flatten2)
model = tf.keras.Model(input, output)
```
- Functional API : 각 레이어들을 변수로 나눠서 연결 해주는 방식의 모델. `tf.keras.Model()`의 매개변수에 입력 레이어  , 반환 레이어를 명시만 해줘도 된다
##### 강화 학습
```python
inception_model = InceptionV3(input_shape = (150, 150, 3), include_top = False, weights = None)
inception_model.load_weights("./asset/model/inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5")
# 예시처럼 기존 모델과 가중치를 불러온다.
```
- `.load_weights(path)` : path(경로)에서 가중치 파일(.h5등)을 불러온다
- `.get_layer(layer_name)` : 해당 모델에 있는 레이어중 일치하는 이름의 레이어를 가져온다. 이후 새로운 레이어를 추가하면 기존 레이어는 사라진다
##### 레이어 목록
- `tf.keras.layers.Dense(노드갯수, activation=)` : 기본적인 계산을 수행하는 노드들을 가지고 있는 레이어이다.
- `tf.keras.layers.Flatten()` : 
- `tf.keras.layers.Reshape()` : `Flatten` 레이어와 반대로 차원을 높이는 레이어이다. 이전 레이어와 총 노드의 수는 같아야 한다
- `tf.keras.layers.Concatenate()` :
- `tf.keras.layers.Conv2D(복사본갯수, (kernal_x, kernal_y), [padding = "same"], activation=)` : CNN에서 자세히 다룸
- `tf.keras.layers.MaxPooling2D((x,y))` : CNN에서 자세히 다룸
#### Optimizer, 손실함수 정하기
```python
model.compile(optimizer=, loss=, metrics=)
```
- Learning Rate Optimizer, Loss Function 를 적절히 찾아 넣으면 된다. 어떤 학습을 시킬지에 따라 종류를 잘 선택해야 한다
##### metrios
- 'accuracy' : 정확도를 측정한다. 

#### 학습하기
```python
model.fit(x데이터(학습데이터), y데이터(실제 데이터), epochs=반복횟수)
```
- x데이터와 y데이터가 하나로 전처리되어 있는 경우는 그 데이터 하나만 넣어도 된다

#### 모델을 이용한 예측하기
```python
model.predict(test_data)
```
- 훈련 데이터와 같은 데이터 형식을 넣어주어야 하며, numpy 배열 형식의 데이터가 필요하다
<!-- ------------------------------------------------- -->
# Pandas 메인
- 행, 열로 구조화된 데이터를 다루는 라이브러리
- Tensorflow에서는 데이터 전처리를 위해 pandas 라이브러리를 사용한다.
- 일반적으로 `import pandas as pd`로 많이 불러온다
## 함수
### pd
- `.read_csv(file_path)` : csv 파일을 읽어 dataframe 형식으로 반환한다
- `.isnull()` : `null`, 또는 빈 행을 선택한다
- `.dropna()` : 선택한 열을 drop(제거) 한다(`.isnull()`등 함수가 필요)
### 기타
- `.min()` : 해당 열의 최솟값을 반환한다
- `.max()` :  해당 열의 최댓값을 반환한다
- `.count()` : 해당 열의 행의 갯수를 반환한다
- `.fillna(value)` ㅣ: `null` 또는 빈 값을 `value`로 대체한다.
- `[column]` : 원하는 열을 선택하서 반환한다
- `.values` : 선택된 열을 numpy 배열로 반환한다(단독으로 사용되지 않고 `[column]`과 함께 주로 쓰인다)
- `.itterow()` : Java에서 foreach 문처럼 for문에서 데이터를 하나씩 가져오면서 반복한다. 행 번호, 행의 값 반환한다
## DataFrame이란?
- 표 형식의 데이터를 다루기 위한 자료형이다.
- 행과 열로 구성되어 있으며, 각 열은 서로 다른 자료형을 가질 수 있다. 
- 각 행은 인덱스를 가지며, 데이터에 빠르게 접근할 수 있다.
- csv, excel, sql 데이터 베이스 등 다양한 데이터를 쉽게 변환할 수 있다
<!-- ------------------------------------------------- -->
# Numpy 메인
- Tensorflow는 계산을 빠르고 쉽게 하기 위해 numpy 배열만 데이터로 받는다.
- 일반적으로 `import numpy as np`로 많이 불러온다
## 함수
### np
- `.array(data)` : 일반 배열을 numpy 배열로 변환한다. 