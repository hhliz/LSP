# install python
sudo apt install cmake
sudo apt install python3
sudo apt install python3-venv
sudo apt install python3-pip
pip3 install virtualenv

rm -r ./python38
mkdir ./python38
python3 -m venv ./python38
source ./python38/bin/activate

# install packages
# pip3 install -r requirementspgff.txt
pip3 install wheel
pip3 install numpy
pip3 install scikit-sparse
pip3 install matplotlib
pip3 install sklearn
pip3 install pandas
pip3 install cython
pip3 install umap-learn
pip3 install MulticoreTSNE

#compile task 1
cd ./src/vx/com/px/dataset/
sh Makefile.sh
