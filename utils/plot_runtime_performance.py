#!/usr/bin/env python3

import json
from compare import read
import pandas as pd
import numpy as np
import argparse
import matplotlib.pyplot as plt
import sys

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
    rename_map = {'blender': 'Blender', 'chrome': 'Chromium', 'povray': 'POV-Ray', 'solc':'Solidity', 'envoy-static':'Envoy', 'opt':'LLVM', '471.omnetpp':'OMNeT++', '447.dealII':'deal.II', 'd8':'V8', 'z3':'Z3'}
    rows = ['Blender', 'Chromium', 'deal.II', 'Envoy', 'LLVM', 'OMNeT++', 'POV-Ray', 'Solidity', 'V8', 'Z3']
    config = parser.parse_args()
    base_thin_data = read(config.base_thin)
    base_thin_data.rename(index=rename_map, inplace=True)
    base_thin_data = base_thin_data.reindex(rows)
    base_full_data = read(config.base_full)
    base_full_data.rename(index=rename_map, inplace=True)
    base_full_data = base_full_data.reindex(rows)

    compare_thin_data = read(config.compare_thin)
    compare_thin_data.rename(index=rename_map, inplace=True)
    compare_thin_data = compare_thin_data.reindex(rows)
    compare_full_data = read(config.compare_full)
    compare_full_data.rename(index=rename_map, inplace=True)
    compare_full_data = compare_full_data.reindex(rows)

    # Extract metrics
    metrics = config.metrics
    for metric in metrics:
        if metric not in base_thin_data.columns:
            sys.stderr.write("Unknown metric '%s'\n" % metric)

    base_thin_metrics = base_thin_data["test_time"]
    base_full_metrics = base_full_data["test_time"]
    compare_thin_metrics = compare_thin_data["test_time"]
    compare_full_metrics = compare_full_data["test_time"]
    thin_improvement = ((base_thin_metrics - compare_thin_metrics) / base_thin_metrics) * 100
    full_improvement = ((base_full_metrics - compare_full_metrics) / base_full_metrics) * 100

    improvement = pd.DataFrame()
    improvement.insert(0, "ThinLTO", thin_improvement, allow_duplicates=True)
    improvement.insert(1, "LTO", full_improvement)
    improvement = improvement.round(2)
    #improvement = improvement.drop(["chrome"])

    print(improvement)

    width = 0.30
    multiplier = 0
    plt.rcParams.update({'font.size': 15})

    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(12, 6), height_ratios=[1,1])
    fig.subplots_adjust(hspace=0.085)
    fig.subplots_adjust(bottom=0.15)

    ax1.spines['bottom'].set_visible(False)
    ax2.spines['top'].set_visible(False)
    ax1.xaxis.tick_top()
    ax1.tick_params(labeltop=False)
    ax2.xaxis.tick_bottom()

    colors = {'LTO': 'xkcd:azure', 'ThinLTO': 'tab:orange'}
    edgecolors = {'LTO': 'black', 'ThinLTO': 'black'}
    x = np.arange(len(improvement.index))
    #kwargs = dict(linewidth=0.02, visible=True)
    for col in improvement.columns:
        offset = width * multiplier
        rects = ax1.bar(x + offset, improvement[col], width, clip_on=False, color=colors[col], label=col, edgecolor='black', linewidth=2, align='edge')
        ax2.bar(x + offset, improvement[col], width, label=col, color=colors[col], edgecolor='black', linewidth=2, align='edge')
        #ax1.bar_label(rects, padding = 3)
        multiplier += 1

    fontsize = 20
    ax1.set_ylim(10, 90)
    ax2.set_ylim(-1, 4)
    ax2.set_ylabel('Performance Improvement', labelpad=10, fontsize=fontsize, y=1.0)
    #ax2.set_xlabel("benchmarks", fontsize=fontsize)
    ax2.set_xticks(x + width, improvement.index, fontsize=fontsize)
    ax1.set_title('Run-time Performance', fontsize=fontsize)

    # set y labels
    vals = ax2.get_yticks()
    ax2.set_yticklabels(['{0}%'.format(round(x)) for x in vals], fontsize=18)
    vals = ax1.get_yticks()
    ax1.set_yticklabels(['{0}%'.format(round(x)) for x in vals], fontsize=18)

    ax2.tick_params(axis='x', labelrotation=18)

    ax1.legend(loc="upper right", ncols=2, fontsize=17)
    #plot = base_improvement.plot.bar(rot=0, figsize=(46, 30))
    d = .5
    leg = plt.legend()
    kwargs = dict(marker=[(-1, -d), (1, d)], markersize=18.5,
              linestyle="none", color='k', mec='k', mew=2, clip_on=False)
    ax1.plot([0, 1], [0, 0], transform=ax1.transAxes, **kwargs)
    ax1.plot([0, 0.468], [0, 0], transform=ax1.transAxes, **kwargs)
    ax1.plot([0, 0.184], [0, 0], transform=ax1.transAxes, **kwargs)
    ax1.plot([0, 0.44], [0, 0], transform=ax1.transAxes, **kwargs)
    ax1.plot([0, 0.155], [0, 0], transform=ax1.transAxes, **kwargs)
    ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)
    ax2.plot([0.468, 1], [1, 1], transform=ax2.transAxes, **kwargs)
    ax2.plot([0.184, 1], [1, 1], transform=ax2.transAxes, **kwargs)
    ax2.plot([0.44, 1], [1, 1], transform=ax2.transAxes, **kwargs)
    ax2.plot([0.155, 1], [1, 1], transform=ax2.transAxes, **kwargs)
    ax2.get_legend().remove()
    plt.show()
    plt.savefig("runtime.pdf")

if __name__ == "__main__":
    main()
