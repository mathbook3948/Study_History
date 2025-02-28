# 개념
## 머신러닝 이란?
- 단순히 뭔가 수학적인 계산을 통해 실제 결과와 예측한 결과의 오차를 찾는 행위를 컴퓨터에게 시키는 것이다.
### 학습 방법의 종류
#### Supervised Learning(지도학습)
- 데이터에 정답이 있고, 정답을 맞추거나 정답일 확률을 구하는 모델을 만들 때 사용
#### Unsupervised Learning(비지도 학습)
- 데이터에 정답이 없고 알아서 비슷한것 끼리 분류를 하는 모델을 만들 때 사용
#### Reinforcement Learning(강화 학습)
- 특정 행동을 할때마다 보상을 주고, 이 보상을 최대화 하는 방식으로 행동하는 모델을 만들 때 사용
#### Transfer Learning(전이 학습)
- 기존에 있던 성능 좋은 모델을 가져와서 가중치, 원하는 레이어 등을 뽑아와서 더 성능이 좋은 모델을 만드는 방법

## 모델 용어
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
### 학습률
- 가중치를 한번에 얼마만큼 변경해야 하는지를 의미한다.
### 경사하강법(GD)
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
- 하지만 고정된 수의 경우에는 복잡한 문제에서 학습이 안일어나는 문제가 있을 수 있으므로 가변적인 값을 곱해주어야 한다(Learning Rate Optimizer)
### 확률적 경사하강볍(SGD)
//TODO
navigate(path)
## 기타 개념
### 데이터 전처리
- 데이터 중간에 값이 없는 등 학습에 영향을 주는 요소들을 제거, 또는 학습이 더 잘 이루어지도록 데이터를 미리 처리 해두는 것을 말한다.
### 파라미터 튜닝
- 모델의 성능을 최적화 하기 위하여 Learning Rate, epochs, 등 조절 가능한 값을 조절 하는 것이다.
### 과적합(Overfitting)
- 반복적으로 같거나 비슷한 데이터만 훈련시키면 그 데이터에 익숙해져서 답을 외워버리는 현상을 말한다.
### 순전파와 역전파
- 순전파로 오차계산 -> 역전파로 가중치 변경
#### 순전파
- 이전의 신경망에 값을 넣어 오차를 구하는 것.
#### 역전파
- 순전파에서 계산된 오차를 출력층 -> 은닉층 -> 입력층 으로 전파하며 가중치를 변경한다.
- 각 층의 가중치들이 오차에 얼마나 기여했는지 계산한다(미분 사용)
- 계산된 기여도에 따라 가중치를 수정한다

$w_{new} = w_{old} - \alpha \frac{\partial E}{\partial w}$

$\frac{\partial E}{\partial w} = \frac{\partial E}{\partial y} \cdot \frac{\partial y}{\partial z} \cdot \frac{\partial z}{\partial w}$

- $\frac{\partial E}{\partial w}$ : 가중치 w가 변할 때 오차 E가 얼마나 민감하게 변하는지의 변화율(기울기)
- $\frac{\partial E}{\partial y}$ : 출력값 y가 변할 때 오차 E가 얼마나 민감하게 변하는지의 변화율
    - 예: MSE 오차함수를 사용할 경우 (y - t), t는 실제값
- $\frac{\partial y}{\partial z}$ : 활성화 함수의 미분값. 뉴런의 입력값 z가 변할 때 출력값 y가 얼마나 민감하게 변하는지
    - 예: 시그모이드 함수의 경우 y(1-y)
- $\frac{\partial z}{\partial w}$ : 가중치 w가 변할 때 뉴런의 입력값 z가 얼마나 민감하게 변하는지
    - z = wx + b 형태에서는 입력값 x가 됨
- 출력층 -> 은닉층 이후에는 각 데이터가 오차에 얼마나 기여를 했는지(가중치)를 계산하여 오차를 내고, 반복한다

## Neural Networks(신경망)
- 인간의 뇌 구조와 기능을 모방한 컴퓨터 알고리즘
- 입력층, 은닉층, 출력층으로 구성된 인공 뉴런들의 네트워크
- 데이터로부터 패턴을 학습하여 복잡한 문제를 해결하는 모델
### 종류
#### CNN(Convolutional Neural Network) - 합성곱 신경망
- 이미지 같은 것을 예측할 때 2차원 이상의 데이터를 Flatten 레이어로 1차원으로 만들어야 하는 경우가 생긴다.
- 이미지를 일자로 나열한다면 규칙이 깨져서 유연한 모델을 만들기 힘들어진다
##### 해결책
1. 이미지의 중요한 정보(특징)를 추려서 복사본을 만든다. 각 이미지는 원본 이미지의 특성을 강조하는 성격을 지니고 있다.
2. 이미지 정보를 중앙으로 모으는 Pooling 레이어를 거친다
3. 중앙으로 모인 정보를 바탕으로 Flatten 레이어를 거친다 -> 모든 이미지의 정보가 중앙으로 집중된다
##### MobileNet
- 적은 메모리로도 성능 좋고 빠른 모델을 만들기 위한 구조
- CNN을 하는데, 각 채널에 따로 계산을 한 후, 합치는 구조
###### **핵심 구조: Depthwise Separable Convolution**
1. 일반적인 컨볼루션의 문제점
- 모든 입력 채널과 출력 채널을 한 번에 처리
- 연산량: (입력 크기) × (필터 크기) × (입력 채널 수) × (출력 채널 수)
- 예: 16×16 이미지, 3×3 필터, 3채널 입력, 256채널 출력
  → 16×16 × (3×3×3) × 256 = 매우 많은 연산량

2. MobileNet의 해결방법 (2단계로 분리)
   1) Depthwise Convolution
   - 각 입력 채널별로 따로 공간적 특징 추출
   - 연산량: (입력 크기) × (필터 크기) × (입력 채널 수)
   - 예: 16×16 × (3×3) × 3 = 훨씬 적은 연산량

   2) Pointwise Convolution (1×1 Convolution)
   - 각 채널의 특징들을 결합
   - 연산량: (입력 크기) × 1 × (입력 채널 수) × (출력 채널 수)
   - 예: 16×16 × 1 × 3 × 256 = 추가적인 연산
##### MobileNetV2
- ResNet의 장점을 흡수한 버전
- BottleNeck 구조를 사용하였다(1x1 Conv(차원 높임) -> 기존 MobileNet -> 1x1 Conv(차원 줄임))
##### ResNet
- 레이어가 깊어질수록 복잡해져서 원래 정보를 까먹는 걸 해결하기 위한 방법
###### ###### **핵심 구조: Residual Learning (잔차 학습)** 
1. 일반적인 컨볼루션의 문제점
- 더 깊은 네트워크가 오히려 성능이 떨어지는 현상 발생
- 단순히 층을 쌓는 것으로는 성능 향상의 한계
2. ResNet의 해결방법 
   1) Skip Connection (지름길 연결)
   - 입력을 출력에 바로 더해주는 연결 추가
   - 입력이 그대로 출력에 전달되어 까먹는거 방지
    2) Residual Learning
   - //TODO
---
##### BottleNeck 구조
- 입력 : 256 채널 --> 3x3 Conv를 바로 진행하면 256채널에서 모두 3x3 연산이 이루어짐(매우 무거움)
###### 해결
1. 256 → 64 채널로 줄이고
2. 64 채널에서만 3x3 연산
3. 다시 64 → 256으로 늘림
- 연산은 하지만 계산이 훨씬 줄어듦

#### RNN(Recurrent Neural Network)
- 순서가 중요한 데이터(문장 등..)을 Dense에 넣으면 순서에 대한 정보가 사라짐을 해결하기 위한 방법
- 서로 연관이 있거나 순서가 있는 데이터에 유용하다
##### 적용 예시 : Sequence to Sequence
- 문장에서 문장을 뽑아내는 방법(ex: 번역)
```
한글 문장 -> RNN -> 다차원의 복잡한 행렬(예측) -> RNN -> 영어 문장
```
- Sequence를 압축(행렬로 예측하는 놈) : Encoder
- 행렬을 Sequence로 바꿔주는 놈 : Decoder 
##### Simple RNN Layer
- 신경망에 단어를 넣을때 순서대로 하나씩 넣는 방법. 
- 예측값을 다음 레이어에 전달하여 이전의 값을 다음 예측에 사용한다
###### 문제점
- Diminishing Gradient : RNN이 복잡해질 때 뒤로 갈 수록 앞쪽의 예측값의 비중이 적어지는 것. 즉, RNN이 커질경우 input 데이터는 output 데이터에 거의 영향을 안주는 문제가 발생
##### LSTM(Long Short-Term Memory)
- 처음 데이터도 RNN 레이어 끝까지 끌고가야해서 나온 레이어
- 레이어를 통해 예측 결과물로 2개를 내놓는다.
- 장기기억 단기기억 이라고 생각하면 된다
- 이전 장기기억에 중요하지 않아 보이는거는 버리고, 중요한거는 이전 장기기억에 추가하는 식으로 작동한다
```
#forget gate
input + 이전 예측 -> sigmoid 
--> 이전 장기기억에 곱해줌
```
```
#input gate
input + 이전 예측 -> sigmoid
            *
input + 이전 예측 -> tanh
--> 이전 장기기억에 더해줌 
```
##### GRU(Gated Recurrent Unit) 
- GRU 이전 예측을 좀더 영향력을 크게 준다. 그 외에는 LSTM 비슷
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
### mean_squared_error(MSE)
- 오차를 제곱한 값의 평균을 손실값으로 정하는 함수이다.
- 오차를 제곱하여 평균을 구하기에 항상 양수가 나오고, 실제 값에서 멀어질수록 손실이 크게 증가하는 특징이 있다.
```python
def mse(y_true, y_pred):
  return (np.array([y_true[i] - y_pred[i] for i in range(len(y_true))]) ** 2).mean()
```
### binary_crossentropy
//TODO
## Activation Function(활성화 함수)
### Sigmoid(시그모이드)
- 0~1 사이로 값을 만들어준다. (0, 0.5)에서 만나며, 이후 x가 증가할 때 1에 가까워지고, x가 감소할 때 0에 가까워진다.
- 0과 1 사이로 추려지기에 확률 문제에 적합하다.
```python
def sigmoid(x):
    return 1 / (1 + math.e ** -x)
```
### ReLU(Rectified Linear Unit, 경사 함수)
- 음수는 0으로 처리하고 x가 0일때부터는 기울기가 1인 일차함수로 표현된다.

## 기초 머신러닝 알고리즘
### 선형 회귀(Linear Regression)
- 데이터 x를 넣었을 때 실제 y에 가장 가까운 선(실제 y를 가장 잘 설명하는 선)을 찾는 방법이다
```python
# 2차원 모델
def model(x, a, b):
  return x * a + b
```
### 로지스틱 회귀(Logistic Regression)
- 특정 정보를 가지고 0~1의 값(즉, 확률)으로 예측해주는 방법이다
