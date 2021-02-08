# LSP
This code is a new freshly implemented Least Square Projection (LSP) in Python from the original code in Java - [Paper](https://ieeexplore.ieee.org/document/4378370). LSP is projection technique based on least square approximations, LSP this characterized by be faster and accurate.

Least Square Projection (LSP) in Python was used in a system called GFF - Graphs from Features to perform visual attribute selection - [Paper](https://www.mdpi.com/1999-4893/13/11/302/htm).

## Author
Liz M. Huancapaza Hilasaca

## Running from Windows 10
### Prerequisites
Make sure the following software is installed:
* [Docker](https://docs.docker.com/docker-for-windows/install/)

### To install:
* docker build -t lspos . 
> obs.: execute only once.
### To running:
* docker run -d -it -v "$(pwd)":/app/lsp lspos
> obs.: use "docker stop id" to stop lsp aplication

> obs.: id is dinamicaly asingned, use "docker ps" to see id

## Running from Ubuntu 20.04
### Prerequisites
Make sure the following software is installed:
* [GCC](https://gcc.gnu.org/) - C/C++;
* [Python](https://www.python.org/) - Python 3.8+;

### To install:
* bash install.sh
> obs.: execute only once.
### To running:
* bash run.sh
> obs.: execute the example ./src/lsptest.py 


## How use LSP
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Liz M. Huancapaza Hilasaca
# Copyright (c) 2020
# E-mail: lizhh@usp.br

from vx.com.py.projection.LSPU import *
from vx.com.py.projection.TSNEM import *

from vx.com.px.dataset.dataio import DataMatrix, ProximityMatrix

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
```

## Sample data sets
We have included two sample data sets that can help you to get started within the framework. The data sets are:

* [MNIST](http://yann.lecun.com/exdb/mnist)
  * Content: Handwritten digits features
  * [784 features; 10,000 items](https://github.com/hhliz/LSP/blob/master/datasets/MNIST-10000-784.csv)
  * Target feature: label

* [Corel Images](https://ieeexplore.ieee.org/document/1227984)
  * Content: Extracted image features
  * [150 features; 1000 items](https://github.com/hhliz/LSP/blob/master/datasets/Core-1000-150.csv)
  * Target feature: Category

  
  
  
## LSP citation:

Paulovich, F. V.; Nonato, L. G.; Minghim, R. and Levkowitz, H. "Least Square Projection: A Fast High-Precision Multidimensional Projection Technique and Its Application to Document Mapping," in IEEE Transactions on Visualization and Computer Graphics, vol. 14, no. 3, pp. 564-575, May-June 2008, [doi: 10.1109/TVCG.2007.70443](https://ieeexplore.ieee.org/document/4378370). 


## Employed in:

Minghim, R.; Huancapaza, L.; Artur, E.; Telles, G.; Belizario, I. "Graphs from Features: Tree-Based Graph Layout for Feature Analysis," in Algorithms, 2020-13(11), 302, 18 November 2020, [https://doi.org/10.3390/a13110302](https://www.mdpi.com/1999-4893/13/11/302).
  
