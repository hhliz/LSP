FROM ubuntu:20.04

MAINTAINER Liz M. Huancapaza "lihh@usp.br"
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y python3-pip python3-dev gcc build-essential cmake python3 python3-venv  python3-scipy libsuitesparse-dev \
    && rm -rf /var/lib/apt/lists/* 

COPY . /app/lsp

WORKDIR /app/lsp
RUN pip3 install -r requirements.txt

# RUN pip3 install wheel
# RUN pip3 install numpy
# RUN pip3 install scikit-sparse
# RUN pip3 install matplotlib
# RUN pip3 install sklearn
# RUN pip3 install pandas
# RUN pip3 install cython
# RUN pip3 install umap-learn
# RUN pip3 install MulticoreTSNE

WORKDIR /app/lsp
CMD [ "bash", "rundocker.sh" ]
