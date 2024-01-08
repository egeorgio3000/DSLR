import pandas as pd
import sys
import matplotlib.pyplot as plt
from utils.utils import Utils as ut


def find_lowest_std(df):
    df_num = ut.keep_num_values(df)
    df_num = df_num.drop('Index', axis=1)
    deviation = {}
    for column in df_num.columns:
        df_num[column] = ut.normalize_column(df_num[column])
        deviation[column] = ut.Std(df_num[column])
        print(f'Standard deviation of subject {column} = {deviation[column]}')
    try:
        df_num['Hogwarts House'] = df['Hogwarts House']
    except ValueError:
        print(f'{ValueError}: No Feature available in dataframe')
        sys.exit(1)
    print(f'Subject with lowest standard deviation is {min(deviation, key=deviation.get)}')
    return df_num

def histogram(df):
    for column in [col for col in df.columns if col != 'Hogwarts House']:
        plt.hist(df[df['Hogwarts House'] == 'Slytherin'][column], alpha=0.5, label='Slytherin', color='green')
        plt.hist(df[df['Hogwarts House'] == 'Gryffindor'][column], alpha=0.5, label='Gryffindor', color='red')
        plt.hist(df[df['Hogwarts House'] == 'Hufflepuff'][column], alpha=0.5, label='Hufflepuff', color='yellow')
        plt.hist(df[df['Hogwarts House'] == 'Ravenclaw'][column], alpha=0.5, label='Ravenclaw', color='blue')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.legend()
        plt.title(f'Histogram of {column}')
        plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python histogram.py <dataset>")
        sys.exit(1)
    try:
        df = pd.read_csv(sys.argv[1])
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
        sys.exit(1)
    df_num = find_lowest_std(df)
    histogram(df_num)