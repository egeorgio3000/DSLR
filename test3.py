
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from utils.utils import Utils as ut


def logistic(x: float) -> float:
    return 1.0 / (1 + np.exp(-x))

def logistic_d(x: float) -> float:
    y = logistic(x)
    return y * (1 - y)

def partial_gradient_descent(theta, x, y, j):
        return - (y - logistic(np.dot(x, theta))) * x[j]

def J(X, y, theta):
    m = len(y)
    sum = 0
    for i in range(m):
        if y[i] == 1:
            sum -= (1 / m) * np.log(logistic(np.dot(X[i], theta)))
        else:
            sum -= (1 / m) * np.log(logistic(np.dot(X[i], theta)))
    return(sum)

def gradient_descent(X, y, theta, learning_rate, iter):
    m = len(y)
    for _ in range(iter):
        cost = J(X, y, theta)
        h = logistic(np.dot(X, theta))
        gradient = np.dot(X.T, (h - y)) / m
        theta -= learning_rate * gradient
        if J(X, y, theta) > cost:
            return theta
    raise Exception("Not enough iteration")
        
          


if __name__ == '__main__':
    s2 = 'Astronomy'
    s1 = 'Flying'
    df = pd.read_csv('./dataset/dataset_train.csv')
    df_num = ut.keep_num_values(df)
    df_num = df_num.drop('Index', axis=1)
    df_num['Hogwarts House'] = df['Hogwarts House']
    df_test = df_num[['Hogwarts House', s1, s2]]
    df_test = pd.concat([df_test[df_test['Hogwarts House'] == 'Gryffindor'], df_test[df_test['Hogwarts House'] == 'Hufflepuff']], ignore_index=True)

    for column in df_test.columns:
        if column != 'Hogwarts House':
            df_test[column] = ut.normalize_column(df_test[column])

    for subj in [('Hufflepuff', 'yellow'), ('Gryffindor', 'red')]:
        plt.scatter(df_test[df_test['Hogwarts House'] == subj[0]][s1], df_test[df_test['Hogwarts House'] == subj[0]][s2], alpha=0.5, label=subj[0], color=subj[1])
    plt.xlabel(s1)
    plt.ylabel(s2)
    plt.legend()
    plt.title(f'Scatter of {s1} and {s2}')
    df_test = df_test.dropna()

    X = df_test[['Flying', 'Astronomy']].values
    X = np.c_[np.ones((X.shape[0], 1)), X]
    theta = np.zeros(X.shape[1])
    y = df_test['Hogwarts House'].map({'Gryffindor': 0, 'Hufflepuff': 1}).values
    try:
        theta = gradient_descent(X, y, theta, 0.05, 200)
    except Exception as e:
        print("Error: ", e)
    print(theta, df_test)
    plt.show()