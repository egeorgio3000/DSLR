import pandas as pd
import sys
import matplotlib.pyplot as plt
from utils.utils import Utils as ut
import argparse

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python histogram.py <dataset>")
        sys.exit(1)
    try:
        df = pd.read_csv(sys.argv[1])
    except Exception as e:
         print(e)
         sys.exit(1)
