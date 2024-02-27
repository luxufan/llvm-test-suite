#!/usr/bin/env python3

import json
from compare import read
import pandas as pd
import argparse
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

def main():
    parser = argparse.ArgumentParser(prog="plot.py")
    parser.add_argument("-m", "--metric", action="append", dest="metrics", default=[])
    parser.add_argument("-b", "--base", dest="base")
    parser.add_argument("file",
                        help="File to plot")
    config = parser.parse_args()
    data = read(config.file)
    base = config.base

    # Extract metrics
    metrics = config.metrics
    for metric in metrics + [base]:
        if metric not in data.columns:
            sys.stderr.write("Unknown metric '%s'\n" % metric)

    metrics_column = data[metrics]
    base_column = data[base]
    result_column = metrics_column.div(base_column, axis=0)
    result_column = result_column.mul(100)
    plt.rcParams.update({'font.size': 32})
    plot = result_column.plot.bar(rot=0, figsize=(46, 30))
    plot.yaxis.set_major_formatter(mtick.PercentFormatter())
    plot.set_xlabel("Applications")
    plot.set_ylabel("Percentage out of " + base)
    plt.savefig(metrics[0].replace(".", "_"))

if __name__ == "__main__":
    main()
