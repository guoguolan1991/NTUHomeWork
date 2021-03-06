# coding:utf8

import numpy as np


def get_data_set(filename):

    '''
    
    :param filename: 
    :return: X, Y
    '''

    data_set = open(filename, "r")
    data_set = data_set.readlines()
    num = len(data_set)

    X = np.zeros((num, 5))
    Y = np.zeros((num, 1))

    for i in range(num):
        data = data_set[i].strip().split()
        X[i, 0] = 1.0
        X[i, 1] = np.float(data[0])
        X[i, 2] = np.float(data[1])
        X[i, 3] = np.float(data[2])
        X[i, 4] = np.float(data[3])
        Y[i, 0] = np.int(data[4])

    return X, Y

