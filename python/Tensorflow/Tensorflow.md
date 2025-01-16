# Tensorflow 란?
- 구글에서 만든 딥러닝 프로그램을 쉽게 구현할 수 있도록 기능을 제공하는 라이브러리'
# Tensorflow 메인
- 일반적으로 `import tensorflow as tf`로 짧게 바꿔서 불러온다
## 전처리
- 먼저 데이터 사이에 빈 값이나 `null` 이 있는지 확인하고 제거하거나 평균값 등을 넣어준다(`.fillna()`, `.dropna()` 등을 사용할 수 있다)
- 데이터 준비가 끝나면, numpy 배열로 데이터를 준비시킨다.
### tf.keras.preprocessing
#### `.image_dataset_from_directory()`
- 폴더에 저장된 이미지 파일을 데이터셋으로 로드할 수 있게 해주는 함수
- 경로에 폴더별로 이미지를 나눠주면 자동으로 라벨링 해준다
```python
#매개변수
directory = "" # 데이터셋으로 만들기 원하는 사진의 폴더의 경로
image_size = (x, y) # 사진의 크기를 정한다. 크거나 작아도 알아서 조절 해준다
barch_size = batch_size # 한번에 처리할 이미지의 갯수를 정함
subset = "" # training과 validation을 넣을 수 있으며, 데이터를 훈련용과 검증용으로 나누기 위해 사용한다. 보통 seed, validation_split 매개변수를 같게 설정한다
validation_split = 0 ~ 1 # 0에서 1 사이의 값을 넣을 수 있으며, validation 데이터의 비율을 결정한다
seed = seed # 데이터를 나눌 시드를 정한다
```
## 모델의 신경망
### 기본 레이어
- `tf.keras.layers.Dense(노드갯수, activation=)` : 기본적인 계산을 수행하는 노드들을 가지고 있는 레이어이다.
- `tf.keras.layers.Flatten()` : 다차원 입력을 1차원으로 평면화하는 레이어
- `tf.keras.layers.Reshape()` : `Flatten` 레이어와 반대로 차원을 높이는 레이어이다. 이전 레이어와 총 노드의 수는 같아야 한다
- `tf.keras.layers.Concatenate()` : 여러 tensor들을 하나로 합치는 레이어
- `tf.keras.layers.Input(shape=)` : 모델의 입력 레이어를 정의. Functional 모델에서 사용한다
- `tf.keras.layers.Dropout(rate)` : 과적합 방지를 위해 학습 중 일정 비율의 데이터를 무작위로 비활성화(제거)하는 레이어
### CNN(Convolutional Neural Network) 레이어
- `tf.keras.layers.Conv2D()` : 2D CNN 레이어. 이미지 처리에 사용한다
```
#매개변수
filters : 출력 채널의 수
kernel_size : 커널의 크기. (height, width) 튜플 또는 단일 정수(예: (3,3) 또는 3 (3x3 커널))
[padding = "same/valid"] : 입력과 출력의 크기가 같도록 패딩을 더해준다. 커널을 적용하면 크기가 작아질 수 밖에 없는데, 작아진 만큼 padding을 추가해준다
activation : 이미지의 rgb는 0~255 이여서 음수가 나오지 않게 설정하는 relu를 많이 사용한다
```
- `tf.keras.layers.MaxPooling2D((x,y))` : 지정한 크기에서 가장 큰 값들을 중앙으로 모은다 (x, y : 2, 2일 경우 2,2 x 4개. 즉, 4, 4 -> 2,2를 진행한다)
### 데이터 증강 레이어(사진)
- `tf.keras.layers.RandomFlip(mode='horizontal')`: 이미지를 좌우 또는 상하로 뒤집습니다. mode는 'horizontal', 'vertical'을 사용할 수 있다.
- `tf.keras.layers.RandomRotation(factor=0.2)`: 이미지를 지정된 각도 범위 내에서 무작위로 회전시킵니다. factor 0.2는 ±20% 회전을 의미한다.
- `tf.keras.layers.RandomZoom(height_factor=0.2)`: 이미지를 무작위로 확대/축소합니다. 0.2는 ±20% 크기 변화를 의미한다.
- `tf.keras.layers.RandomTranslation(height_factor=0.2, width_factor=0.2)`: 이미지를 가로/세로로 이동시킨다.
- `tf.keras.layers.RandomBrightness(factor=0.2)`: 이미지의 밝기를 무작위로 조정한다.
- `tf.keras.layers.RandomContrast(factor=0.2)`: 이미지의 대비를 무작위로 조정한다.
- `tf.keras.layers.RandomCrop(height, width)`: 이미지를 지정된 크기로 무작위로 가린다.
- `tf.keras.layers.GaussianNoise(stddev=0.1)`: 가우시안 노이즈를 추가한다.
- `tf.keras.layers.RandomSaturation(factor=0.2)`: 이미지의 채도를 무작위로 조정한다
- `tf.keras.layers.RandomHue(factor=0.2)`: 이미지의 색조를 무작위로 조정한다.

### 모델 유형
#### Sequential 모델
- 층(Layer)을 순차적으로 쌓아 구성하는 선형 구조의 신경망 모델
- 입력층부터 출력층까지 순서대로 연결되어 데이터가 순차적으로 흐르는 단순한 구조
- 주로 간단한 구조의 신경망을 구현할 때 사용됨
```python
#예시
model = Sequential([
   Dense(64, activation='relu', input_shape=(784,)),
   Dense(32, activation='relu'),
   Dense(10, activation='softmax')
])
```
#### Functional 모델
- 층들을 함수처럼 처리하여 더 복잡하고 유연한 신경망 구조를 구현할 수 있는 모델
- 다중 입력/출력, 층 공유, 분기/합류 등 복잡한 신경망 구조 설계 가능
```python
#예시
inputs = Input(shape=(784,))
x = Dense(64, activation='relu')(inputs)
x = Dense(32, activation='relu')(x)
outputs = Dense(10, activation='softmax')(x)
model = Model(inputs=inputs, outputs=outputs)
```

## 모델 학습
### Compile
```python
model.compile(optimizer=, loss=, metrics=)
```
- optimizer : Learning Rate Optimizer
- loss : Loss Function
- metrics : 모델의 성능을 측정하는 값
```
'accuracy'
'mae'
```
### Fit(학습)
```python
model.fit(x데이터(학습데이터), y데이터(실제 데이터), epochs=반복횟수)
```
- x데이터와 y데이터가 하나로 전처리(튜플)되어 있는 경우는 그 데이터 하나만 넣어도 된다
### 모델을 이용한 예측하기
```python
model.predict(test_data)
```
- 훈련 데이터와 같은 데이터 형식을 넣어주어야 하며, numpy 배열 형식의 데이터가 필요하다
- 
<!--======================================================밑은 정리중-->

# Tensorflow 메인
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
##### 모델
##### 전이 학습
```python
inception_model = InceptionV3(input_shape = (150, 150, 3), include_top = False, weights = None)
inception_model.load_weights("./asset/model/inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5")
# 예시처럼 기존 모델과 가중치를 불러온다.
```
- `.load_weights(path)` : path(경로)에서 가중치 파일(.h5등)을 불러온다
- `.get_layer(layer_name)` : 해당 모델에 있는 레이어중 일치하는 이름의 레이어를 가져온다. 이후 새로운 레이어를 추가하면 기존 레이어는 사라진다

