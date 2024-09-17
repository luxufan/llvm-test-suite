#!/usr/bin/env python3
import json
from compare import read
import pandas as pd
import numpy as np
import argparse
import matplotlib.pyplot as plt

def main():
    parser = argparse.ArgumentParser(prog="plot_addresspoints_candidates.py")
    parser.add_argument("file", help="statistics file")
    config = parser.parse_args()
    stats = read(config.file)
    fig, axes = plt.subplots(3, 3)
    fig.set_figheight(40)
    fig.set_figwidth(60)
    candidates = stats[["dyncastopt.NumLeafNodes", "dyncastopt.NumTwoCandidates", "dyncastopt.NumThreeCandidates", "dyncastopt.NumMoreThanThreeCandidates", "dyncastopt.NumRangeCheck"]]
    nan_index = np.isnan(candidates)
    candidates[nan_index] = 0

    print(len(axes))
    axes_list = []
    for x in axes:
        for ax in x:
            axes_list.append(ax)

    rmprefix = lambda s: s[len('dyncastopt.Num'):]
    for i in range(len(axes_list)):
        labels = []
        print(candidates.index[i])
        row = candidates.loc[candidates.index[i]]
        print(row)
        ii = 0
        for n in row:
            if n == 0:
                labels.append('')
            else:
                labels.append(rmprefix(candidates.columns[ii]))
            ii += 1
        axes_list[i].pie(row, labels=labels)

    plt.show()
    plt.savefig("candidates")

if __name__ == "__main__":
    main()
