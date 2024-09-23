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
    optimized = stats[["dyncastopt.NumLeafNodes", "dyncastopt.NumTwoCandidates", "dyncastopt.NumThreeCandidates", "dyncastopt.NumMoreThanThreeCandidates", "dyncastopt.NumRangeCheck"]]
    non_optimized = stats[["dyncastopt.NumNonFixedInLTO", "dyncastopt.NumPrivateBase", "dyncastopt.NumNoHint", "dyncastopt.NumNoAddressPoints"]]

    # Transform nan to 0
    nan_index = np.isnan(optimized)
    optimized[nan_index] = 0
    nan_index = np.isnan(optimized)
    optimized[nan_index] = 0

    # Do summation
    optimized = optimized.sum(axis=0)
    non_optimized = non_optimized.sum(axis=0)
    num_non_optimized = non_optimized.sum(axis=0)
    num_optimized = optimized.sum(axis=0)
    all_dyncast = pd.Series([num_optimized, num_non_optimized])
    num_all_dyncast = all_dyncast.sum(axis=0)
    print(all_dyncast)

    # exchange two rows
    exchange_columns = ['dyncastopt.NumThreeCandidates', 'dyncastopt.NumRangeCheck', 'dyncastopt.NumTwoCandidates', 'dyncastopt.NumLeafNodes', 'dyncastopt.NumMoreThanThreeCandidates']
    optimized = optimized.reindex(exchange_columns)
    print(optimized)

    # make figure and assign axis objects
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(35, 15))
    fig.subplots_adjust(wspace=0)
    plt.rcParams.update({'font.size': 20})

    # pie chart parameters
    overall_ratios = all_dyncast / num_all_dyncast
    rmprefix = lambda s: s[len('dyncastopt.Num'):]

    labels = ['optimzied', 'non-optimized']
    explode = [0, 0.1]
    # rotate so that first wedge is split by the x-axis
    angle = -180 * overall_ratios[1]
    wedges, *_ = ax2.pie(overall_ratios, autopct='%1.1f%%', startangle=angle,
                         labels=labels, explode=explode)

    # bar chart parameters
    non_optimized_ratios = non_optimized / num_non_optimized
    non_optimized_labels = [rmprefix(i) for i in non_optimized.index]
    bottom = 1
    width = .2

    # Adding from the top matches the legend.
    for j, (height, label) in enumerate(reversed([*zip(non_optimized_ratios, non_optimized_labels)])):
        bottom -= height
        bc = ax3.bar(0, height, width, bottom=bottom, color='C1', label=label,
                     alpha=0.1 + 0.25 * j)
        ax3.bar_label(bc, labels=[f"{height:.2%}"], label_type='center')

    # use ConnectionPatch to draw lines between the two plots
    theta1, theta2 = wedges[0].theta2, wedges[0].theta1
    center, r = wedges[1].center, wedges[1].r
    bar_height = sum(non_optimized_ratios)

    # draw top connecting line
    x = r * np.cos(np.pi / 180 * theta2) + center[0]
    y = r * np.sin(np.pi / 180 * theta2) + center[1]
    con = ConnectionPatch(xyA=(-width / 2, bar_height), coordsA=ax3.transData,
                          xyB=(x, y), coordsB=ax2.transData)
    con.set_color([0, 0, 0])
    con.set_linewidth(2.5)
    ax3.add_artist(con)

    # draw bottom connecting line
    x = r * np.cos(np.pi / 180 * theta1) + center[0]
    y = r * np.sin(np.pi / 180 * theta1) + center[1]
    con = ConnectionPatch(xyA=(-width / 2, 0), coordsA=ax3.transData,
                          xyB=(x, y), coordsB=ax2.transData)
    con.set_color([0, 0, 0])
    ax3.add_artist(con)
    con.set_linewidth(2.5)

    ax3.set_title('distribution of non optimized dynamic_cast')
    ax3.legend()
    ax3.axis('off')
    ax3.set_xlim(- 2.5 * width, 2.5 * width)

    optimized_ratios = optimized / num_optimized
    print(optimized_ratios)
    optimized_labels = [rmprefix(i) for i in optimized.index]

    bottom = 1
    width = .2
    for j, (height, label) in enumerate(reversed([*zip(optimized_ratios, optimized_labels)])):
        print(j)
        print(height)
        bottom -= height
        bc = ax1.bar(0.15, height, width, bottom=bottom, color='C0', label=label, alpha=0.1 + 0.20 * j)
        ax1.bar_label(bc, labels=[f"{height:.2%}"], label_type='center')

    # use ConnectionPatch to draw lines between the two plots
    theta1, theta2 = wedges[1].theta1, wedges[1].theta2
    center, r = wedges[0].center, wedges[0].r
    bar_height = sum(non_optimized_ratios)

    # draw top connecting line
    x = r * np.cos(np.pi / 180 * theta2) + center[0]
    y = r * np.sin(np.pi / 180 * theta2) + center[1]
    con = ConnectionPatch(xyA=(width + 0.05, bar_height), coordsA=ax1.transData,
                          xyB=(-0.05, r), coordsB=ax2.transData)
    con.set_color([0, 0, 0])
    con.set_linewidth(2.5)
    ax3.add_artist(con)

    # draw bottom connecting line
    x = r + center[0]
    y = r + center[1]
    con = ConnectionPatch(xyA=(width + 0.05, 0), coordsA=ax1.transData,
                          xyB=(-0.05, -r), coordsB=ax2.transData)
    con.set_color([0, 0, 0])
    ax1.add_artist(con)
    con.set_linewidth(2.5)

    ax1.set_title('distribution of optimized dynamic_cast')
    ax1.legend()
    ax1.axis('off')
    ax1.set_xlim(- 2.5 * width, 2.5 * width)

    plt.show()
    plt.savefig("candidates")

if __name__ == "__main__":
    main()
