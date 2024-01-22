import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from utils.utils import Utils as ut
from typing import List
import random
from utils.linear_algebra import vector_sum, Vector

#https://covid19.uthm.edu.my/wp-content/uploads/2020/04/Data-Science-from-Scratch-First-Principles-with-Python-by-Joel-Grus-z-lib.org_.epub_.pdf
def logistic(x: float) -> float:
    return 1.0 / (1 + np.exp(-x))

def logistic_d(x: float) -> float:
    y = logistic(x)
    return y * (1 - y)

def  _negative_log_likelihood(x, y, beta) -> float:
    if y == 'Gryffindor':
        return -np.log(logistic(np.dot(x, beta)))
    else:
        return -np.log(1 - logistic(np.dot(x, beta)))

def negative_log_likelihood(xs,
                            ys,
                            beta) -> float:
    return sum(_negative_log_likelihood(x, y, beta)
    for x, y in zip(xs, ys))

def _negative_log_partial_j(x: Vector, y: float, beta: Vector, j: int):
    -(y - logistic(np.dot(x, beta))) * x[j]

def _negative_log_gradient(x: Vector, y: float, beta: Vector):
    return [_negative_log_partial_j(x, y, beta, j) for j in range(len(beta))]

# def J(df):
#     n = df.shape[0]
#     print(n)

if __name__ == '__main__':
    s2 = 'Astronomy'
    s1 = 'Flying'
    df = pd.read_csv('./dataset/dataset_train.csv')
    df_num = ut.keep_num_values(df)
    df_num = df_num.drop('Index', axis=1)
    df_num['Hogwarts House'] = df['Hogwarts House']
    df_test = df_num[['Hogwarts House', s1, s2]]
    df_test = pd.concat([df_test[df_test['Hogwarts House'] == 'Gryffindor'], df_test[df_test['Hogwarts House'] == 'Hufflepuff']], ignore_index=True)
    for subj in [('Hufflepuff', 'yellow'), ('Gryffindor', 'red')]:
        plt.scatter(df_test[df_test['Hogwarts House'] == subj[0]][s1], df_test[df_test['Hogwarts House'] == subj[0]][s2], alpha=0.5, label=subj[0], color=subj[1])
    plt.xlabel(s1)
    plt.ylabel(s2)
    plt.legend()
    plt.title(f'Scatter of {s1} and {s2}')
    print(df_test)
    xs = [[1.0] + row[1:] for row in df_test.values.tolist()]
    ys = [row[0] for row in df_test.values.tolist()]
    beta = [random.random() for _ in range(3)]
    # print(negative_log_likelihood(xs, ys, beta))
    print(np.dot(xs[0], beta))
    plt.show()

    