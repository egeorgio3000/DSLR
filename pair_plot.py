import pandas as pd
import sys
import matplotlib.pyplot as plt
from utils.utils import Utils as ut
import argparse

def histogram(ax, column):
    ax.hist(df[df['Hogwarts House'] == 'Slytherin'][column], alpha=0.5, color='green')
    ax.hist(df[df['Hogwarts House'] == 'Gryffindor'][column], alpha=0.5, color='red')
    ax.hist(df[df['Hogwarts House'] == 'Hufflepuff'][column], alpha=0.5, color='yellow')
    ax.hist(df[df['Hogwarts House'] == 'Ravenclaw'][column], alpha=0.5, color='blue')

def pair_plot(df):
    df_num = ut.keep_num_values(df)
    df_num = df_num.drop('Index', axis=1)
    # print("df_num:\n", df_num)
    for column in df_num.columns:
        df_num[column] = ut.normalize_column(df_num[column])
    # print("df_num normalized:\n", df_num)
    fig, axs = plt.subplots(df_num.shape[1], df_num.shape[1], figsize=(6, 2))
    print(type(axs), type(axs[0]))
    for column1 in df_num.columns:
        for column2 in df_num.columns:
            if column1 == column2:
                histogram(axs[int(df_num.columns.get_loc(column1))], column1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python histogram.py <dataset>")
        sys.exit(1)
    try:
        df = pd.read_csv(sys.argv[1])
    except Exception as e:
        print(e)
        sys.exit(1)
    pair_plot(df)
