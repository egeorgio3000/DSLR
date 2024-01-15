import pandas as pd
import sys
import matplotlib.pyplot as plt
from utils.utils import Utils as ut
import argparse

def histogram(ax, column, df):
    ax.hist(df[df['Hogwarts House'] == 'Slytherin'][column], bins=20, label='Slytherin', alpha=0.5, color='green')
    ax.hist(df[df['Hogwarts House'] == 'Gryffindor'][column], bins=20, label='Gryffindor', alpha=0.5, color='red')
    ax.hist(df[df['Hogwarts House'] == 'Hufflepuff'][column], bins=20, label='Hufflepuff', alpha=0.5, color='yellow')
    ax.hist(df[df['Hogwarts House'] == 'Ravenclaw'][column], bins=20, label='Ravenclaw', alpha=0.5, color='blue')
    ax.set_xticks([])
    ax.set_yticks([])

def scatter_plot(ax, column1, column2, df):
    try:
        
        abs = pd.concat([df[column1], df['Hogwarts House']], axis=1)
        ord = pd.concat([df[column2], df['Hogwarts House']], axis=1)
    except Exception as e:
        print('Error: ', e)
        # sys.exit(1)
    for subj in [('Slytherin', 'green'), ('Gryffindor', 'red'), ('Ravenclaw', 'blue'), ('Hufflepuff', 'yellow')]:
        ax.scatter(abs[abs['Hogwarts House'] == subj[0]][column1], ord[ord['Hogwarts House'] == subj[0]][column2], alpha=0.5, label=subj[0], color=subj[1], s=1)
    ax.set_xticks([])
    ax.set_yticks([])

def pair_plot(df):
    df_num = ut.keep_num_values(df)
    df_num = df_num.drop('Index', axis=1)
    for column in df_num.columns:
        df_num[column] = ut.normalize_column(df_num[column])
    try:
        df_num['Hogwarts House'] = df['Hogwarts House']
    except ValueError:
        print(f'{ValueError}: No Feature available in dataframe')
        exit(1)
    fig, axs = plt.subplots(df_num.shape[1] - 1, df_num.shape[1] - 1, figsize=(13, 13), tight_layout=True)
    for i, column1 in enumerate([col for col in df_num.columns if col != 'Hogwarts House']):
        for j, column2 in enumerate([col for col in df_num.columns if col != 'Hogwarts House']):
            if column1 == column2:
                histogram(axs[int(df_num.columns.get_loc(column1))][int(df_num.columns.get_loc(column1))], column1, df_num)
            else:
                scatter_plot(axs[int(df_num.columns.get_loc(column1))][int(df_num.columns.get_loc(column2))], column1, column2, df_num)
            if i == df_num.shape[1] - 2:
                axs[i, j].set_xlabel(column2)
            if j == 0:
                axs[i, j].set_ylabel(column1)
    plt.legend(df['Hogwarts House'].unique(), loc='center left',
            frameon=False, bbox_to_anchor=(1, 0.5))
    plt.show()


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
