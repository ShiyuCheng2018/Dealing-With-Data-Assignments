import numpy as np


def sums(ndarray):

    return ndarray.sum(axis=1), ndarray.sum(axis=0), ndarray.sum()


def fvr(ndarray, order="C"):

    flatten = np.array([])
    if order.upper() == "C":
        for i in range(len(ndarray)):
            flatten = np.concatenate((flatten, ndarray[i]))

    elif order.upper() == "F":
        for i in range(len(ndarray[0])):
            flatten = np.concatenate((flatten, ndarray[:, i]))

    return flatten


def znm(ndarray, row=True):

    if row:
        for i in range(len(ndarray)):
            max_num = np.amax(ndarray[i])
            for each in range(len(ndarray[i])):
                if ndarray[i][each] != max_num:
                    ndarray[i][each] = 0
    else:
        for i in range(len(ndarray)):
            max_num = np.amax(ndarray[:, i])
            for each in range(len(ndarray[:, i])):
                if ndarray[:, i][each] != max_num:
                    ndarray[:, i][each] = 0

    return ndarray



print(znm(np.array([[1, 99, 3],
                     [4, 11, 6],
                     [7, 8, 9]]), row=False))


