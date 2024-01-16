import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
X = np.random.rand(100, 2)  # 100 samples with 2 features
y = (X[:, 0] + X[:, 1] > 1).astype(int)
print(f"X: {X}\ny: {y}")
plt.scatter(X[:, 0] + X[:, 1], y)
plt.show()

def logistic_regression(iteration):
    theta = [0, 0]