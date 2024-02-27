#!/usr/bin/env python3

import json
from compare import read
import pandas as pd
import argparse
import matplotlib.pyplot as plt

def main():
    parser = argparse.ArgumentParser(prog="plot.py")
    parser.add_argument("-m", "--metric", action="append", dest="metrics", default=[])
    parser.add_argument("file",
                        help="File to plot")
    config = parser.parse_args()
    file = config.file
    data = read(file)

    # Extract metrics
    metrics = config.metrics
    for metric in metrics:
        if metric not in data.columns:
            sys.stderr.write("Unknown metric '%s'\n" % metric)

    metrics_column = data[metrics]
    plt.rcParams.update({'font.size': 32})
    plot = metrics_column.plot.bar(rot=0, figsize=(46, 30))
    plt.savefig(metrics[0].replace(".", "_"))
    plot = metrics_column.plot.bar(rot=0, figsize=(46, 30))

if __name__ == "__main__":
    main()
