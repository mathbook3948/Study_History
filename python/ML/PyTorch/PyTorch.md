# PyTorch 왜씀?
- 기본 Python 문법과 비슷하여 쉽게 배울 수 있다.
## PyTorch 메인
### 데이터 작업
- 기본적으로 `torch.utils.data.DataLoader`, `torch.utils.data.Dataset`가 있다
- Dataset은 샘플과 정답(label)을 저장하고, DataLoader은 Dataset을 iterable한 객체로 감싼다
#### Dataset
- 원하는 데이터를 학습 가능하게 가공하려면 Dataset 객체를 상속받는 객체를 만들어야 한다.
```python
from torch.utils.data import Dataset

class CustomDataset(Dataset):
    def __init__(self, data, labels):
        self.data = data # ex pd.DataFrame
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        # 1. 데이터 로드
        # 2. 전처리
        # 4. 반환
        return sample, label # x, y 반환
```
- 3가지 메서드를 필수로 구현해야 한다.
- `__init__` : 데이터를 초기화
- `__len__` : 데이터셋의 총 샘플 수를 반환
- `__getitem__` : 주어진 데이터를 반환(x, y 모두 torch.Tensor 타입)

### 모델 만들기
- `nn.Module`을 상속받는 클래스를 생성하여 정의한다.
- `__init__`에서 신경망의 계층을 정의하고, `forward` 함수에서 데이터를 어떻게 전달할지 지정한다.
### `nn.Sequential()`
- 순차적인 신경망 컨테이너를 정의한다
- 모든것이 순차적으로 진행되기에 `forward`를 정의할 필요가 없다.
```python
class BasicSequential(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(784, 512),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(512, 256),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(256, 10)
        )
    
    def forward(self, x):
        return self.model(x)
```
### Functional
- 복잡한 모델을 구현할 떄 사용한다
- `forward`함수에 어떻게 모델이 구성되는지 정의해야 한다
```python
class BasicFunctional(nn.Module):
    def __init__(self):
        super().__init__()
        # 학습 가능한 레이어 정의
        self.fc1 = nn.Linear(784, 512)
        self.fc2 = nn.Linear(512, 256)
        self.fc3 = nn.Linear(256, 10)
    
    def forward(self, x):
        # Functional API를 사용하여 연산 정의
        x = F.relu(self.fc1(x))
        x = F.dropout(x, p=0.2, training=self.training)
        x = F.relu(self.fc2(x))
        x = F.dropout(x, p=0.2, training=self.training)
        x = self.fc3(x)
        return x
```
### 레이어 목록
#### 활성화 함수(`torch.nn.functional`)
- `.relu(x)`
- `.sigmoid(x)`
- `.tanh(x)`
- `.leaky_relu(x)`
- `.elu(x)`
- `.softmax(x, dim=)` : dim을 필수로 지정해야 한다
```
[[1, 2, 3],
 [4, 5, 6]]

# dim이 0일 경우
# 각 행의 합이 1이 되도록 계산한다
[[0.018, 0.119, 0.268],
 [0.982, 0.881, 0.732]]
 
# dim이 1일 경우
# 각 열의 합이 1이 되도록 계산한다
[[0.090, 0.245, 0.665],
 [0.090, 0.245, 0.665]]
```
#### 손실 함수(`torch.nn.functional`)
##### 회귀
- `.mse_loss(pred, true)`
- `.l1_loss(pred, true)`
- `.smooth_l1_loss(pred, true)`
##### 분류
- `.cross_entropy(pred, true)`
- `.nll_loss(pred, true)`
- `.binary_cross_entropy(pred, true)`
#### 정규화 함수(`torch.nn.functional`)
- `.batch_norm(x)`
- `.layer_norm(x)`
- `.dropout()` : p -> 비활성화(제거)할 비율 
- `.dropout2d(x, p=)` : p -> 비활성화(제거)할 채널의 비율
#### CNN(`torch.nn.functional`)
- `.conv2d()`
```python
.conv2d(x, weight,
    in_channels,          # 들어오는 채널 수
    out_channels,         # 출력 채널 수
    kernel_size,          # 커널 크기
    stride=1,             # 스트라이드 크기
    padding=0,            # 패딩 크기
)
stride: 필터가 이동하는 간격. (2,2)이면 가로세로 2칸씩 이동
padding: 입력 데이터 외곽에 추가하는 0값. padding=1이면 한 줄씩 추가
```
##### 풀링
- `.max_pool2d()`
```python
.max_pool2d(x,
    kernel_size=2,        # 커널 크기
    stride=None,          # 윈도우 이동 간격 (None이면 kernel_size와 동일)
    padding=0,            # 패딩 크기
    ceil_mode=False       # True:올림, False:내림으로 출력 크기 계산
)
```
- `.avg_pool2d()`
```python
.avg_pool2d(x,
    kernel_size=2,
    stride=None,
    padding=0,
    ceil_mode=False,
    count_include_pad=True
)
```