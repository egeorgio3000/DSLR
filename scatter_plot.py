import pandas as pd
import sys
import matplotlib.pyplot as plt
from utils.utils import Utils as ut
import argparse

def scatter_plot(df, s1, s2):
    df_num = ut.keep_num_values(df)
    df_num = df_num.drop('Index', axis=1)
    try:
        df_num['Hogwarts House'] = df['Hogwarts House']
        abs = df_num[[s1, 'Hogwarts House']]
        ord = df_num[[s2, 'Hogwarts House']]
    except ValueError:
        print(f'{ValueError}: No Feature available in dataframe')
        sys.exit(1)
    except Exception as e:
        print('Error: ', e)
        sys.exit(1)
    for subj in [('Slytherin', 'green'), ('Gryffindor', 'red'), ('Ravenclaw', 'blue'), ('Hufflepuff', 'yellow')]:
        plt.scatter(abs[abs['Hogwarts House'] == subj[0]][s1], ord[ord['Hogwarts House'] == subj[0]][s2], alpha=0.5, label=subj[0], color=subj[1])
    plt.xlabel(s1)
    plt.ylabel(s2)
    plt.legend()
    plt.title(f'Scatter of {s1} and {s2}')
    plt.show()

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=str, default='./dataset/dataset_train.csv')
    parser.add_argument('-s1', '--subject1', type=str, default='Arithmancy', help='First subject to compare')
    parser.add_argument('-s2', '--subject2', type=str, default='Astronomy', help='Second subject to compare')
    args = parser.parse_args()
    try:
        df = pd.read_csv(args.file)
    except Exception as e:
         print(e)
         sys.exit(1)
    scatter_plot(df, args.subject1, args.subject2)