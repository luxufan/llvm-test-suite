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
    fig.set_figheight(8)
    fig.set_figwidth(16)
    fig.subplots_adjust(hspace=0.25, wspace=0.15)
    col_names = ["dyncastopt.NumHasLeafNodes", "dyncastopt.NumHasTwoCandidates", "dyncastopt.NumHasThreeCandidates", "dyncastopt.NumHasFourCandidates", "dyncastopt.NumHasFiveCandidates", "dyncastopt.NumHasSixCandidates", "dyncastopt.NumHasSevenCandidates", "dyncastopt.NumHasMoreThanSevenCandidates"]
    colors = {"LeafNodes": "blue", "TwoCandidates":'red', 'ThreeCandidates':'green', 'FourCandidates':'orange', 'FiveCandidates':'grey', 'SixCandidates':'blue', 'SevenCandidates':'yellow', 'MoreThanSevenCandidates':'pink'}
    candidates = stats[col_names]
    nan_index = np.isnan(candidates)
    candidates[nan_index] = 0
    print(candidates)

    print(len(axes))
    axes_list = []
    for x in axes:
        for ax in x:
            axes_list.append(ax)

    width = 0.5

    rmprefix = lambda s: s[len('dyncastopt.NumHas'):]
    for i in range(len(axes_list)):
        labels = []
        #title = candidates.index[i]
        #print(candidates.index[i])
        row = candidates.loc[candidates.index[i]]
        testsuite = candidates.index[i]
        row = row.sort_values(ascending=False)
        ii = 0
        color = []
        data = []
        for n in row:
            if n == 0:
                continue
            else:
                name = rmprefix(candidates.columns[ii])
                color.append(colors[name])
                #print(name)
                if name == 'LeafNodes':
                    labels.append('1')
                elif name == 'TwoCandidates':
                    labels.append('2')
                elif name == 'ThreeCandidates':
                    labels.append('3')
                elif name == 'FourCandidates':
                    labels.append('4')
                elif name == 'FiveCandidates':
                    labels.append('5')
                elif name == 'SixCandidates':
                    labels.append('6')
                elif name == 'SevenCandidates':
                    labels.append('7')
                elif name == 'MoreThanSevenCandidates':
                    labels.append('>7')
                else:
                    labels.append(name[:-len('Candidates')])
                data.append(n)
            ii += 1
        axes_list[i].bar(labels, data, width, color=color)
        axes_list[i].set_xlim(-1, 8)
        axes_list[i].set_xlabel(testsuite)

    plt.show()
    plt.savefig("candidates.pdf")

if __name__ == "__main__":
    main()
