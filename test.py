import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
X = np.linspace(0, 10, 100).reshape(-1, 1)  # Feature
y = (3*X[:, 0] + np.random.normal(0, 1, size=len(X)) > 15).astype(int)  # Binary labels


def logistic_regression(a, iteration):
    theta = [0, 0]
    n = X.shape[0]
    # for k in range(iteration):
    i = 0
    sum1: float = 0
    sum2: float = 0
    for i in range(n):
        print(1 - (1 + np.exp(-(theta[0] + theta[1] * X[i][0]))))
        if y[i] == 1:
            sum1 += np.exp(-(theta[0] + theta[1] * X[i][0])) / (1 + np.exp(-(theta[0] + theta[1] * X[i][0])))
            sum2 += X[i][0] * np.exp(-(theta[0] + theta[1] * X[i][0])) / (1 + np.exp(-(theta[0] + theta[1] * X[i][0])))
        else:
            sum1 += np.exp(-(theta[0] + theta[1] * X[i][0])) / (1 - (1 + np.exp(-(theta[0] + theta[1] * X[i][0]))))
            sum2 += X[i][0] * np.exp(-(theta[0] + theta[1] * X[i][0])) / (1 - (1 + np.exp(-(theta[0] + theta[1] * X[i][0]))))
        theta[0] -= (a / n) * sum1
        theta[1] -= (a / n) * sum2
        print(theta)
        
def logistic(x: float) -> float:
    return 1.0 / (1 + np.exp(-x))
def logistic_d(x: float) -> float:
    y = logistic(x)
    return y * (1 - y)

if __name__ == "__main__":
    logistic_regression(0.1, 50)
    # plt.scatter(X, y)
    x = np.linspace(-10, 10, 100)
    plt.plot(x, logistic(x), label="logistic function")
    plt.show()