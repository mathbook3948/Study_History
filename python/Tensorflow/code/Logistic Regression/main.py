import math
import numpy as np

def sigmoid(x):
    return 1 / (1 + math.e ** -x)

def model(x, y):
    pass

def get_gradients(x, y_true, y_pred, a, b, learning_rate):
    dw = np.mean(2 * (y_pred - y_true) * x)
    db = np.mean(2 * (y_pred - y_true))

    new_a = a - learning_rate * dw
    new_b = b - learning_rate * db

    return new_a, new_b
