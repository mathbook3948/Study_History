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
![[Pasted image 20241108224009.png]]
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