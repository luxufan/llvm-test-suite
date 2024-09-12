#!/usr/bin/env python3

import json
from compare import read
import pandas as pd
import numpy as np
import argparse
import matplotlib.pyplot as plt

def main():
    parser = argparse.ArgumentParser(prog="plot_runtime_performance.py")
    parser.add_argument("-m", "--metric", action="append", dest="metrics", default=[])
    parser.add_argument("base_thin",
                        help="Base thinlto file")
    parser.add_argument("compare_thin",
                        help="Compare thinlto file")
    parser.add_argument("base_full",
                        help="Base fulllto file")
    parser.add_argument("compare_full",
                        help="Compare fulllto file")
    config = parser.parse_args()
    base_thin_data = read(config.base_thin)
    base_full_data = read(config.base_full)

    compare_thin_data = read(config.compare_thin)
    compare_full_data = read(config.compare_full)

    # Extract metrics
    metrics = config.metrics
    for metric in metrics:
        if metric not in base_thin_data.columns:
            sys.stderr.write("Unknown metric '%s'\n" % metric)

    base_thin_metrics = base_thin_data[metrics]
    base_full_metrics = base_full_data[metrics]
    compare_thin_metrics = compare_thin_data[metrics]
    compare_full_metrics = compare_full_data[metrics]
    thin_improvement = ((base_thin_metrics - compare_thin_metrics) / base_thin_metrics) * 100
    full_improvement = ((base_full_metrics - compare_full_metrics) / base_full_metrics) * 100
    full_improvement = full_improvement.rename(columns={"exec_time" : "fulllto"})
    thin_improvement = thin_improvement.rename(columns={"exec_time" : "thinlto"})

    improvement = thin_improvement
    improvement.insert(1, "fulllto", full_improvement["fulllto"], allow_duplicates=True)
    improvement = improvement.round(2)
    improvement = improvement.drop(["chrome"])

    print(improvement)

    ## deal with envoy
    improvement.iloc[0] = - improvement.iloc[0]

    width = 0.35
    multiplier = 0
    plt.rcParams.update({'font.size': 30})
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
    fig.subplots_adjust(hspace=0.08)

    ax1.spines['bottom'].set_visible(False)
    ax2.spines['top'].set_visible(False)
    ax1.xaxis.tick_top()
    ax1.tick_params(labeltop=False)
    ax2.xaxis.tick_bottom()

    fig.set_figheight(20)
    fig.set_figwidth(30)
    x = np.arange(len(improvement.index))
    kwargs = dict(linewidth=0.02, visible=True)
    for col in improvement.columns:
        offset = width * multiplier
        rects = ax1.bar(x + offset, improvement[col], width, clip_on=False, label=col, **kwargs)
        ax2.bar(x + offset, improvement[col], width, label=col, **kwargs)
        #ax1.bar_label(rects, padding = 3)
        multiplier += 1

    ax1.set_ylim(50, 100)
    ax2.set_ylim(0, 3)
    ax2.set_ylabel('performance improvement percentage')
    ax2.set_xlabel("benchmarks")
    ax2.set_xticks(x + width/2, improvement.index)
    ax1.legend(loc="upper right", ncols=2, fontsize="xx-large")
    #plot = base_improvement.plot.bar(rot=0, figsize=(46, 30))
    d = .5
    kwargs = dict(marker=[(-1, -d), (1, d)], markersize=60,
              linestyle="none", color='k', mec='k', mew=1, clip_on=False)
    ax1.plot([0, 1], [0, 0], transform=ax1.transAxes, **kwargs)
    ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)
    plt.show()
    plt.savefig(metrics[0].replace(".", "_"))

if __name__ == "__main__":
    main()
