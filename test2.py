import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from utils.utils import Utils as ut

def logistic(x: float) -> float:
    return 1.0 / (1 + np.exp(-x))
def logistic_d(x: float) -> float:
    y = logistic(x)
    return y * (1 - y)

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
    plt.show()