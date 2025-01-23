# 개념
## 용어
### Agent
### Environment
### State
### Action
### Reward
### Policy
### Value Function
### Gamma (할인율)
- 미래의 보상을 얼마나 중요하게 볼 것인지 결정하는 값. 미래의 보상을 예측하는 것은 중요하지만, 불확실하므로 적용한다. 0~1 사이의 수를 사용하며, 일반적으로 0.9~0.99 사이의 값을 사용한다
### Epsilon
- 탐험 또는 활용을 선택하기 위한 파라미터. "탐혐률"이라 부른다
```python
random_value = random.random()  # 0과 1 사이의 무작위 값 생성

if random_value < epsilon:
    # 탐험: 완전히 무작위 행동 선택
    action = random.randrange(action_size)  # 무작위 Action
else:
    # 활용: 현재까지 학습된 정책에서 가장 좋은 행동 선택
```
### Q-value
- 특정 상태(State)에서 특정 행동(Action)을 했을 때 예상되는 미래 보상의 합
#### 벨만 방정식
```
new_Q = current_Q + 학습률 * (받은_보상 + Gamma * 다음_상태_최대_Q값 - current_Q)
```
## 이름 미정
### Epsilon-Greedy 정책
- 탐험 또는 활용을 어떻게 선택하는지에 대한 정책
- 확률에 따라 탐험 또는 활용을 선택하는데, Epsilon 값이 클수록 탐험을 선택한다
```python
def epsilon_greedy(epsilon, Q_values):
    if random.random() < epsilon:  # epsilon 확률로 무작위 행동 선택 (탐색)
        return random.choice(possible_actions)
    else:  # (1-epsilon) 확률로 최선의 행동 선택 (활용)
        return actions[np.argmax(Q_values)]
```