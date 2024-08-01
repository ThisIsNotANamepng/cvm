# CVM Testing

This repo is for testing the [CVM Algorithm](https://arxiv.org/abs/2301.10191) at scale. 

`createDataset.py` creates a `dataset.txt` which contains x number of non-unique numbers, and y number of unique numbers. `main.py` then handles estimating the unique numbers with the CVM algorithm. The results of various tests are recorded in this file below

It uses https://pypi.org/project/cvm-count/ for the implementation, none of that code is mine and all credit goes to [jinh_tech](https://github.com/jinh-tech/cvm_python)

The library has been tested with a set of 150k items with a 2% accuracy, record with that sort of tone

TODO:
    - Look at initializing library

## Results

### Test 1

3 x 1000000000 non-unique, 10000000 unique

Round 1:
