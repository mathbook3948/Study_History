import numpy as np
import tensorflow as tf
import random
from collections import deque

# 환경 클래스 정의
class GridWorld:
    def __init__(self):
        self.grid_size = 4
        self.state = 0  # 시작 위치 (왼쪽 상단)
        self.goal = 15  # 목표 위치 (오른쪽 하단)

    def reset(self):
        self.state = 0
        return self.state

    def step(self, action):
        # 행동: 0(상), 1(우), 2(하), 3(좌)
        x = self.state % self.grid_size
        y = self.state // self.grid_size

        if action == 0:  # 상
            y = max(0, y - 1)
        elif action == 1:  # 우
            x = min(self.grid_size - 1, x + 1)
        elif action == 2:  # 하
            y = min(self.grid_size - 1, y + 1)
        elif action == 3:  # 좌
            x = max(0, x - 1)

        self.state = y * self.grid_size + x

        # 보상 계산
        if self.state == self.goal:
            reward = 1.0
            done = True
        else:
            reward = -0.1
            done = False

        return self.state, reward, done

# Q-Network 모델 정의
class QNetwork(tf.keras.Model):
    def __init__(self, state_size, action_size):
        super(QNetwork, self).__init__()
        self.dense1 = tf.keras.layers.Dense(24, activation='relu')
        self.dense2 = tf.keras.layers.Dense(24, activation='relu')
        self.dense3 = tf.keras.layers.Dense(action_size)

    def call(self, x):
        x = self.dense1(x)
        x = self.dense2(x)
        return self.dense3(x)

# 학습 파라미터 설정
state_size = 16  # 4x4 그리드
action_size = 4  # 상,우,하,좌
episodes = 1000
memory_size = 2000
batch_size = 32
gamma = 0.95    # 할인율
epsilon = 1.0   # 탐험율
epsilon_min = 0.01
epsilon_decay = 0.995

# 모델과 환경 생성
env = GridWorld()
model = QNetwork(state_size, action_size)
optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
memory = deque(maxlen=memory_size)

# 학습 루프
for episode in range(episodes):
    state = env.reset()
    state = tf.one_hot(state, state_size).numpy()
    total_reward = 0

    while True:
        # 무작위 모험을 하거나 보상을 예측
        if random.random() < epsilon:
            action = random.randrange(action_size)
        else:
            q_values = model(tf.expand_dims(state, 0))
            action = np.argmax(q_values[0])

        # 행동을 실제로 실행
        next_state, reward, done = env.step(action)
        next_state = tf.one_hot(next_state, state_size).numpy()
        total_reward += reward

        # 경험 저장
        memory.append((state, action, reward, next_state, done))

        # 배치 학습
        if len(memory) >= batch_size:
            batch = random.sample(memory, batch_size)
            states = tf.convert_to_tensor([x[0] for x in batch])
            actions = tf.convert_to_tensor([x[1] for x in batch])
            rewards = tf.convert_to_tensor([x[2] for x in batch])
            next_states = tf.convert_to_tensor([x[3] for x in batch])
            dones = tf.convert_to_tensor([x[4] for x in batch])

            with tf.GradientTape() as tape:
                q_values = model(states)
                next_q_values = model(next_states)

                # Q-value 계산
                target_q_values = q_values.numpy()
                max_next_q_values = np.max(next_q_values.numpy(), axis=1)

                for i in range(batch_size):
                    target_q_values[i][actions[i]] = rewards[i]
                    if not dones[i]:
                        target_q_values[i][actions[i]] += gamma * max_next_q_values[i]

                # 손실 계산
                loss = tf.reduce_mean(
                    tf.square(target_q_values - q_values)
                )

            # 경사하강법을 이용한 loss 계산
            grads = tape.gradient(loss, model.trainable_variables)
            optimizer.apply_gradients(zip(grads, model.trainable_variables))

        if done:
            break

        state = next_state

    # 엡실론 감소
    if epsilon > epsilon_min:
        epsilon *= epsilon_decay

    # 학습 진행상황 출력
    if (episode + 1) % 10 == 0:
        print(f"Episode: {episode + 1}, Total Reward: {total_reward}, Epsilon: {epsilon:.3f}")