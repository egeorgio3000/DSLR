import pandas as pd
import sys
from utils.utils import Utils as ut

def describe(df):
    df = ut.keep_num_values(df)
    summary_stats = pd.DataFrame({
        'Count': df.apply(ut.Count),
        'Mean': df.apply(ut.Mean),
        'Std': df.apply(ut.Std),
        'Min': df.apply(ut.Min),
        '25%': df.apply(lambda x: ut.Quartile(x)[0]),
        '50%': df.apply(ut.Mediane),
        '75%': df.apply(lambda x: ut.Quartile(x)[1]),
        'Max': df.apply(ut.Max)
    })
    summary_stats = summary_stats.T
    summary_stats = summary_stats.drop('Index', axis=1)
    return summary_stats

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python describe.py <dataset>")
        sys.exit(1)
    try:
        df = pd.read_csv(sys.argv[1])
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
        sys.exit(1)
    summary_stats = describe(df)
    summary_stats.to_csv('describe.csv')
    print(summary_stats)
    