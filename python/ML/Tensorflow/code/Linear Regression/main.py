from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt

def model(x, a, b):
    return x * a + b

def mse(y_true, y_pred):
    return (np.array([y_true[i] - y_pred[i] for i in range(len(y_true))]) ** 2).mean()

def get_gradients(x, y_true, y_pred, a, b, learning_rate):
    dw = np.mean(2 * (y_pred - y_true) * x)
    db = np.mean(2 * (y_pred - y_true))

    new_a = a - learning_rate * dw
    new_b = b - learning_rate * db

    return new_a, new_b

#======================================================
iris = load_iris()

# 꽃받침 길이(X)와 꽃잎 길이(y) 선택
x = iris.data[:, 0].reshape(-1, 1).flatten()
y = iris.data[:, 2]

a = 0
b = 0
lr = 0.01

for i in range(100): # 100epoch
    print(f"epoch : {i + 1}")
    y_pred = model(x, a, b)
    loss = mse(y, y_pred)
    a, b = get_gradients(x, y, y_pred,a, b, lr)


plt.scatter(x, y, color='blue', label='True Data')
plt.plot(x, model(x, a, b), color='red', label='Regression Line')
plt.xlabel('Flow (Sepal Length)')
plt.ylabel('Petal Length')
plt.title('Iris Data Linear Regression')
plt.legend()
plt.show()