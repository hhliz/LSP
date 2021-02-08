#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Liz M. Huancapaza Hilasaca
# Copyright (c) 2020
# E-mail: lizhh@usp.br

import matplotlib.pyplot as plt
import matplotlib

from vx.com.py.projection.LSPU import *
from vx.com.py.projection.TSNEM import *

from vx.com.px.dataset.dataio import DataMatrix, ProximityMatrix


def plot(X2, y, fileo):
    cmap = plt.cm.get_cmap('rainbow')
    norm = matplotlib.colors.Normalize(vmin=0,vmax=10)
    colors = [matplotlib.colors.rgb2hex( cmap(norm(ij))[:3] ) for ij in range(10)]
    fig, ax = plt.subplots(figsize=(5, 5))
    xmin, xmax = float("inf"), float("-inf")
    ymin, ymax = float("inf"), float("-inf")
    for i in range(len(y)):
        ax.scatter( X2[i][0], X2[i][1],
                    c=colors[int(y[i])], s=7,
                    alpha=0.85, linewidth=0.0001,
                    marker="o")
        if X2[i][0]<xmin:
            xmin = X2[i][0]
        if X2[i][0]>xmax:
            xmax = X2[i][0]
        if X2[i][1]<ymin:
            ymin = X2[i][1]
        if X2[i][1]>xmax:
            ymax = X2[i][1]

    # ax.set_xlim(xmin, xmax)
    # ax.set_ylim(ymin, ymax)
    
    fig = ax.get_figure()
    fig.savefig("out.pdf", format="pdf", bbox_inches='tight')
    plt.close("all")


if __name__ == "__main__":

    # Open dataset 
    DF = DataMatrix("../datasets/Core-1000-150.csv")
    target = "Category";
    # Feature selection using column index
    X = DF.selectcolumns_index([ i for i in range(0, 150)])
    y, _, _ = DF.getcolumn(target)

    # Proximity fot LSP
    #projprox = "DCosine"
    projprox = "Euclidean"

    # Dissimilarity for TSNE
    dissx = "cosine" if projprox=="DCosine" else "euclidean"

    # Make projection with LSP
    X2 = LSPU(  X=X,
                smpprj=TSNEM(proxtype=dissx),
                proxtype=ProximityMatrix.POT[projprox],
                smptype="clusteringmedoids").execute()
    
    # Plot results
    print(X2)
    plot(X2, y, "o.pdf")

    del DF
    del X
    del X2
