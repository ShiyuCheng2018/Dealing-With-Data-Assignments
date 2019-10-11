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
    copy_ndarray = ndarray.copy()
    sign = False

    if row:
        for i in range(len(copy_ndarray)):
            max_num = np.amax(copy_ndarray[i])
            for each in range(len(copy_ndarray[i])):

                if copy_ndarray[i][each] != max_num:
                    copy_ndarray[i][each] = 0
                else:
                    if sign:
                        copy_ndarray[i][each] = 0
                    else:
                        sign = True
            sign = False

    else:
        for i in range(len(copy_ndarray[0])):
            max_num = np.amax(copy_ndarray[:, i])
            for each in range(len(copy_ndarray[:, i])):
                if copy_ndarray[:, i][each] != max_num:
                    copy_ndarray[:, i][each] = 0
                else:
                    if sign:
                        copy_ndarray[:, i][each] = 0
                    else:
                        sign = True
            sign = False

    return copy_ndarray

# version 1.0
def make_board(s):
    board = np.empty((9, 9), dtype="int8")
    for r in range(9):
        for c in range(9):
            while not ('0' <= s[0] <= '9'):
                s = s[1:]
            board[r, c] = s[0]
            s = s[1:]

    return board


def check_sdk(board):
    nums = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    bad_rows = []
    bad_columns = []
    bad_squares = []
    string = f"Bad row(s):"

    for row in range(9):
        if not np.array_equal(np.sort(board[row]), nums):
            bad_rows.append(row + 1)
            string += f" {row + 1}"

    string += "\nBad column(s):"
    for col in range(9):
        if not np.array_equal(np.sort(board[:, col]), nums):
            bad_columns.append(col + 1)
            string += f" {col + 1}"

    string += "\nBad square(s):"
    for row in [0, 3, 6]:
        for col in [3, 6, 9]:
            if not np.array_equal(np.sort(fvr(board[row:row + 3, col - 3:col])), nums):
                bad_squares.append((row + 1, col - 2))
                string += f" {(row + 1, col - 2)}"

    if bad_squares == [] and bad_columns == [] and bad_rows == []:
        print("OK!")
    else:
        print(string)


ndarray_1 = np.array([[1, 2, 0, 1, 0, 2, 0, 1, 1],
                      [0, 1, 1, 1, 0, 2, 2, 2, 1],
                      [0, 2, 2, 0, 2, 2, 2, 0, 1],
                      [1, 0, 0, 2, 1, 2, 2, 2, 2],
                      [1, 1, 2, 1, 1, 2, 1, 0, 2],
                      [2, 1, 0, 2, 0, 0, 0, 0, 1]])

ndarray_2 = np.array([[2, 1, 2, 2, 1, 1, 2, 1, 1, 0],
                      [2, 2, 1, 2, 0, 0, 0, 1, 0, 1],
                      [2, 2, 2, 1, 0, 2, 2, 0, 2, 1],
                      [2, 1, 2, 0, 1, 2, 0, 1, 2, 1],
                      [0, 0, 2, 2, 2, 1, 1, 0, 2, 0]])


def concentrate(ndarray, num):
    for row in range(0, len(ndarray) + 1 - num, num):
        for col in range(num, len(ndarray[0]) + 1, num):
            sub_matrix = ndarray[row:row + num, col - num:col]
            sum_sub = np.sum(sub_matrix)
            ndarray[row:row + num, col - num:col] = np.zeros((num, num))
            sub_matrix[num // 2][num // 2] = sum_sub

    return ndarray


def q1():
    return '''
        reshape(row, col) takes two reference to represent rows and cols. 
        The times result of row and col have to equal to the range(num)'s passing argument.
        So, in this example, np.array(range(12)).reshape(3, 4) will be work since 3*4 = 12.

    '''


def q2():
    return '''
        >>>np.array(range(10)).cumsum()
        >>>a
        array([ 0,  1,  3,  6, 10, 15, 21, 28, 36, 45])
    
    '''


def q3():
    return '''
        //making a 5*5 matrix that elements between 100 and 125, which assigns to variable a.
        >>>a=np.arange(100,125).reshape(5,5) 
        >>>a
        array([[100, 101, 102, 103, 104],
        [105, 106, 107, 108, 109],
        [110, 111, 112, 113, 114],
        [115, 116, 117, 118, 119],
        [120, 121, 122, 123, 124]])

        >>>a += 5 //every element in matrix a plus 5
        >>>a
        array([[105, 106, 107, 108, 109],
        [110, 111, 112, 113, 114],
        [115, 116, 117, 118, 119],
        [120, 121, 122, 123, 124],
        [125, 126, 127, 128, 129]])

        >>>print(a[-3:,1:]) //slice the matrix with -3 row (the second row) till the last row, and the second col till end
        [[116 117 118 119]
        [121 122 123 124]
        [126 127 128 129]]


        a[:,a.shape[1]//2] = a.sum() # assume a has an odd number of columns
        
    '''


def q4():
    return '''
        how to make all elements are 0 matrix with specific rows and cols?
        np.zeros((row, col))np.zeros((4, 5))
        
        >>>array([[0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.]])
        
        
    '''


def estimated_hours():
    return 7


def observation():
    return '''
        observation 1: https://docs.scipy.org/doc/numpy-1.10.1/user/basics.rec.html. This document page gave me great examples
                       of structured arrays in numpy, and how to manipulate dtypes

        observation 2: The length of this assignment is very fair and really helped me to review Python class. Numpy is a very
                        interesting framework, it is perfectly working in order to manipulate numpy.array 
                        
        observation 3: https://docs.scipy.org/doc/numpy/reference/generated/numpy.arange.html

    '''



