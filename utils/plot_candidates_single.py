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
    candidates = stats[["dyncastopt.NumLeafNodes", "dyncastopt.NumTwoCandidates", "dyncastopt.NumThreeCandidates", "dyncastopt.NumMoreThanThreeCandidates", "dyncastopt.NumRangeCheck"]]
    non_optimized = stats[["dyncastopt.NumNonFixedInLTO", "dyncastopt.NumPrivateBase", "dyncastopt.NumNoHint", "dyncastopt.NumNoAddressPoints"]]

    nan_index = np.isnan(candidates)
    candidates[nan_index] = 0
    nan_index = np.isnan(candidates)
    candidates[nan_index] = 0

    candidates = candidates.sum(axis=0)
    print(candidates)
    non_optimized = non_optimized.sum(axis=0)
    print(non_optimized)

    num_non_optimized = non_optimized.sum(axis=0)
    candidates.loc['dyncastopt.NumNonOptimized'] = num_non_optimized
    print(candidates)

    plt.rcParams.update({'font.size': 30})
    fig, ax = plt.subplots(figsize=(40, 60))

    rmprefix = lambda s: s[len('dyncastopt.Num'):]

    labels = [rmprefix(i) for i in candidates.index]

    ax.pie(candidates, labels=labels)

    plt.show()
    plt.savefig("candidates")

if __name__ == "__main__":
    main()
