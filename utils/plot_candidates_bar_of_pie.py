#!/usr/bin/env python3

import json
from compare import read
import pandas as pd
import numpy as np
import argparse
import matplotlib.pyplot as plt

from matplotlib.patches import ConnectionPatch

def main():
    parser = argparse.ArgumentParser(prog="plot_addresspoints_candidates.py")
    parser.add_argument("file", help="statistics file")
    config = parser.parse_args()
    stats = read(config.file)
    candidates = stats[["dyncastopt.NumLeafNodes", "dyncastopt.NumTwoCandidates", "dyncastopt.NumThreeCandidates", "dyncastopt.NumMoreThanThreeCandidates", "dyncastopt.NumRangeCheck"]]
    non_optimized = stats[["dyncastopt.NumNonFixedInLTO", "dyncastopt.NumPrivateBase", "dyncastopt.NumNoHint", "dyncastopt.NumNoAddressPoints"]]

    # Transform nan to 0
    nan_index = np.isnan(candidates)
    candidates[nan_index] = 0
    nan_index = np.isnan(candidates)
    candidates[nan_index] = 0

    # Exchange two columns
    exchange_columns = ['dyncastopt.NumThreeCandidates', 'dyncastopt.NumRangeCheck']
    candidates = candidates.reindex(columns=exchange_columns)

    # Do summation
    candidates = candidates.sum(axis=0)
    non_optimized = non_optimized.sum(axis=0)
    num_non_optimized = non_optimized.sum(axis=0)
    candidates.loc['dyncastopt.NumNonOptimized'] = num_non_optimized
    non_optimized = non_optimized.rename(index={'dyncastopt.NumNonFixedInLTO': 'dyncastopt.NumVirtualInherit'})
    num_all_dyncast = candidates.sum(axis=0)

    # print(non_optimized)
    print(candidates)

    # make figure and assign axis objects
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(60, 34))
    fig.subplots_adjust(wspace=0)
    plt.rcParams.update({'font.size': 23})

    # pie chart parameters
    overall_ratios = candidates / num_all_dyncast
    rmprefix = lambda s: s[len('dyncastopt.Num'):]

    labels = [rmprefix(i) for i in candidates.index]
    explode = [0, 0, 0, 0, 0, 0.1]
    # rotate so that first wedge is split by the x-axis
    angle = -180 * overall_ratios[5]
    wedges, *_ = ax1.pie(overall_ratios, autopct='%1.1f%%', startangle=angle,
                         labels=labels, explode=explode)

    # bar chart parameters
    age_ratios = non_optimized / num_non_optimized
    age_labels = [rmprefix(i) for i in non_optimized.index]
    bottom = 1
    width = .2

    # Adding from the top matches the legend.
    for j, (height, label) in enumerate(reversed([*zip(age_ratios, age_labels)])):
        bottom -= height
        bc = ax2.bar(0, height, width, bottom=bottom, color='C0', label=label,
                     alpha=0.1 + 0.25 * j)
        ax2.bar_label(bc, labels=[f"{height:.0%}"], label_type='center')

        ax2.set_title('Age of approvers')
        ax2.legend()
        ax2.axis('off')
        ax2.set_xlim(- 2.5 * width, 2.5 * width)

        # use ConnectionPatch to draw lines between the two plots
        theta1, theta2 = wedges[5].theta1, wedges[5].theta2
        center, r = wedges[0].center, wedges[0].r
        bar_height = sum(age_ratios)

        # draw top connecting line
        x = r * np.cos(np.pi / 180 * theta2) + center[0]
        y = r * np.sin(np.pi / 180 * theta2) + center[1]
        con = ConnectionPatch(xyA=(-width / 2, bar_height), coordsA=ax2.transData,
                              xyB=(x, y), coordsB=ax1.transData)
        con.set_color([0, 0, 0])
        con.set_linewidth(4)
        ax2.add_artist(con)

        # draw bottom connecting line
        x = r * np.cos(np.pi / 180 * theta1) + center[0]
        y = r * np.sin(np.pi / 180 * theta1) + center[1]
        con = ConnectionPatch(xyA=(-width / 2, 0), coordsA=ax2.transData,
                              xyB=(x, y), coordsB=ax1.transData)
        con.set_color([0, 0, 0])
        ax2.add_artist(con)
        con.set_linewidth(4)

        plt.show()
        plt.savefig("candidates")

if __name__ == "__main__":
    main()
