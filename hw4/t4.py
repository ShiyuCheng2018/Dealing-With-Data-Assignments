# Version: 1.0

from a4 import *

import unittest, io
from contextlib import redirect_stdout

#
# These Sudoku boards are at the top-level for easy access when doing manual testing like
# this: 'python -i t4.py'
#

b1 ="""
       5 3 4 | 6 7 8 | 9 1 2 
       6 7 2 | 1 9 5 | 3 4 8
       1 9 8 | 3 4 2 | 5 6 7 
       - - - + - - - + - - - 
       8 5 9 | 7 6 1 | 4 2 3 
       4 2 6 | 8 5 3 | 7 9 1 
       7 1 3 | 9 2 4 | 8 5 6 
       - - - + - - - + - - -                   
       9 6 1 | 5 3 7 | 2 8 4
       2 8 7 | 4 1 9 | 6 3 5
       3 4 5 | 2 8 6 | 1 7 9"""

b2 ="""
       5 3 4 | 6 7 8 | 9 1 2 
       6 7 2 | 1 9 5 | 3 4 8
       1 9 8 | 3 4 2 | 5 6 7 
       - - - + - - - + - - - 
       8 5 9 | 7 6 1 | 4 2 3 
       4 2 6 | 8 5 3 | 7 9 1 
       7 1 3 | 9 2 4 | 8 5 6 
       - - - + - - - + - - -                   
       8 6 1 | 5 3 7 | 2 8 4
       2 8 7 | 4 1 9 | 6 3 5
       3 4 5 | 2 8 6 | 1 7 9"""

b3 ="""
       5 3 4 | 6 7 8 | 9 1 2 
       6 7 2 | 1 9 5 | 3 4 8
       1 9 8 | 3 4 2 | 5 6 7 
       - - - + - - - + - - - 
       8 5 9 | 7 6 1 | 4 2 3 
       4 2 6 | 8 5 3 | 7 9 1 
       7 1 3 | 9 2 4 | 8 5 6 
       - - - + - - - + - - -                   
       9 6 1 | 9 4 3 | 3 8 4
       2 8 7 | 1 2 2 | 6 3 5
       3 4 5 | 2 1 2 | 1 7 9"""

class TestFns(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None

    def test_sums(self):
        a = np.array([[8, 3, 6, 7, 4],
                      [9, 8, 3, 5, 1],
                      [8, 7, 3, 1, 1]])

        s = sums(a)
        self.assertEqual(tuple, type(s))
        rsum, csum, asum = s
        self.assertEqual(np.ndarray, type(rsum))
        self.assertEqual(np.ndarray, type(csum))
        
        self.assertEqual([28, 26, 20], list(rsum.tolist()))
        self.assertEqual([25, 18, 12, 13,  6], list(csum.tolist()))
        self.assertEqual(74, asum)
        
        a =  np.array([[ 8, 17, 11,  9,  7, 22, 29,  1],
                       [44, 17, 43, 38, 15,  8,  6, 16],
                       [26, 25, 27, 23, 49,  6, 37, 44],
                       [ 4, 20, 36, 32, 39, 20, 15,  2],
                       [ 8, 10, 46, 28, 32, 28, 39,  4],
                       [29, 42, 48, 13,  9, 44, 47, 40],
                       [42, 33,  7, 11, 45, 24,  3, 13]])


        s = sums(a)
        self.assertEqual(tuple, type(s))
        rsum, csum, asum = s
        self.assertEqual(np.ndarray, type(rsum))
        self.assertEqual(np.ndarray, type(csum))
        
        self.assertEqual([104, 187, 237, 168, 195, 272, 178], list(rsum.tolist()))
        self.assertEqual([161, 164, 218, 154, 196, 152, 176, 120], list(csum.tolist()))
        self.assertEqual(1341, asum)

        a =  np.array([[23],
                       [33],
                       [13],
                       [37],
                       [ 2],
                       [42],
                       [18],
                       [44],
                       [ 1],
                       [28]])

        s = sums(a)
        self.assertEqual(tuple, type(s))
        rsum, csum, asum = s
        self.assertEqual(np.ndarray, type(rsum))
        self.assertEqual(np.ndarray, type(csum))
        
        self.assertEqual([23, 33, 13, 37,  2, 42, 18, 44,  1, 28], list(rsum.tolist()))
        self.assertEqual([241], list(csum.tolist()))
        self.assertEqual(241, asum)

    def test_fvr(self):
        a = np.array([[8, 3, 6, 7, 4],
                      [9, 8, 3, 5, 1],
                      [8, 7, 3, 1, 1]])
        self.assertEqual(list(a.flatten()), list(fvr(a)))
        self.assertEqual(list(a.T.flatten()), list(fvr(a.T)))
        self.assertEqual(list(a[:,2:].T.flatten()), list(fvr(a[:,2:].T)))
        
        self.assertEqual(list(a.flatten(order='F')), list(fvr(a, order='F')))
        self.assertEqual(list(a.T.flatten(order='F')), list(fvr(a.T,order='F')))
        self.assertEqual(list(a[:,2:].T.flatten(order='F')), list(fvr(a[:,2:].T,order='F')))
        self.assertEqual(list(a[:,2:].T.flatten('c')), list(fvr(a[:,2:].T,order='c')))
        self.assertEqual(list(a[:,2:].T.flatten('f')), list(fvr(a[:,2:].T,order='f')))

    def test_znm(self):
        a = np.array(range(35)).reshape(5,7)
        a0 = a.copy()
        self.assertEqual(
            np.array([[ 0,  0,  0,  0,  0,  0,  6],
               [ 0,  0,  0,  0,  0,  0, 13],
               [ 0,  0,  0,  0,  0,  0, 20],
               [ 0,  0,  0,  0,  0,  0, 27],
               [ 0,  0,  0,  0,  0,  0, 34]]).tolist(), znm(a).tolist())

        self.assertEqual(
            np.array([[ 0,  0,  0,  0,  0,  0,  0],
               [ 0,  0,  0,  0,  0,  0,  0],
               [ 0,  0,  0,  0,  0,  0,  0],
               [ 0,  0,  0,  0,  0,  0,  0],
               [28, 29, 30, 31, 32, 33, 34]]).tolist(), znm(a,False).tolist())

        self.assertTrue(np.array_equal(a0,a), "Oops! Looks like znm changed its argument!  znm should produce a new array but not change the original.")

        a = np.array([[7, 2, 1], [5, 2, 3]])
        a0 = a.copy()
        self.assertEqual(np.array([[7, 0, 0], [5, 0, 0]]).tolist(), znm(a).tolist())
        self.assertTrue(np.array_equal(a0,a), "Oops! Looks like znm changed its argument!  znm should produce a new array but not change the original.")

        a = np.full((6,6),-1)
        a0 = a.copy()
        self.assertEqual(
         np.array([[-1,  0,  0,  0,  0,  0],
                   [-1,  0,  0,  0,  0,  0],
                   [-1,  0,  0,  0,  0,  0],
                   [-1,  0,  0,  0,  0,  0],
                   [-1,  0,  0,  0,  0,  0],
                   [-1,  0,  0,  0,  0,  0]]).tolist(), znm(a).tolist())

        self.assertEqual(
         np.array([[-1, -1, -1, -1, -1, -1],
                   [ 0,  0,  0,  0,  0,  0],
                   [ 0,  0,  0,  0,  0,  0],
                   [ 0,  0,  0,  0,  0,  0],
                   [ 0,  0,  0,  0,  0,  0],
                   [ 0,  0,  0,  0,  0,  0]]).tolist(), znm(a,False).tolist())


    def test_check_sdk(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            r = """
OK!
"""[1:]
            check_sdk(make_board(b1))
            self.assertEqual(r, buf.getvalue())
            
        with io.StringIO() as buf, redirect_stdout(buf):
            r = """
Bad row(s): 7
Bad column(s): 1
Bad square(s): (7, 1)
"""[1:]
            check_sdk(make_board(b2))
            self.assertEqual(r, buf.getvalue())
            
        with io.StringIO() as buf, redirect_stdout(buf):
            r = """
Bad row(s): 7 8 9
Bad column(s): 4 5 6 7
Bad square(s): (7, 4) (7, 7)
"""[1:]
            check_sdk(make_board(b3))
            self.assertEqual(r, buf.getvalue())

    def test_concentrate(self):
        self.maxDiff = None
        c1 = np.array([[1, 2, 0, 1, 0, 2, 0, 1, 1],
                       [0, 1, 1, 1, 0, 2, 2, 2, 1],
                       [0, 2, 2, 0, 2, 2, 2, 0, 1],
                       [1, 0, 0, 2, 1, 2, 2, 2, 2],
                       [1, 1, 2, 1, 1, 2, 1, 0, 2],
                       [2, 1, 0, 2, 0, 0, 0, 0, 1]])
        
        self.assertEqual(
          np.array([[ 0,  0,  0,  0,  0,  0,  0,  0,  0],
                   [ 0,  9,  0,  0, 10,  0,  0, 10,  0],
                   [ 0,  0,  0,  0,  0,  0,  0,  0,  0],
                   [ 0,  0,  0,  0,  0,  0,  0,  0,  0],
                   [ 0,  8,  0,  0, 11,  0,  0, 10,  0],
                   [ 0,  0,  0,  0,  0,  0,  0,  0,  0]]).tolist(),
                   concentrate(c1,3).tolist())

        c2 = np.array([[2, 1, 2, 2, 1, 1, 2, 1, 1, 0],
                   [2, 2, 1, 2, 0, 0, 0, 1, 0, 1],
                   [2, 2, 2, 1, 0, 2, 2, 0, 2, 1],
                   [2, 1, 2, 0, 1, 2, 0, 1, 2, 1],
                   [0, 0, 2, 2, 2, 1, 1, 0, 2, 0]])
                   
        self.assertEqual(
             np.array([[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                       [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                       [ 0,  0, 34,  0,  0,  0,  0, 24,  0,  0],
                       [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                       [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0]]).tolist(),
                       concentrate(c2,5).tolist())

        c3 = np.array([[ -43,   15,   79,   66,    0,  -81,   -4,  -81,   35,  -96,   -4,   20,   91,  -57,  -40,   84,   -9,  -25],
                       [  43,   99,   52,   49,  -13,  -97,   21,   83,   51,  -10,   99,   93,  -55,  -86,   51,  -10,   96,  -55],
                       [  41,  -18,    2,  -68,   -8,  -60,   96,  -96,  -81,   79,   17,   -7,  -91,    2,   29,  -81,  -54,   45],
                       [ -14,   57,    0,   14,   30,   89,  -40,   95,  -42,  -77,   99,  -96,  -21,   80,   81,   97,   88,   55],
                       [ -10,   43,   45,   91,  -31,   60,  -86,  -12,  -22,   83,  -13,  -27,   61,  -87,  -25,  -56,   85,    7],
                       [  -6,   63,  -36,  -96,   35,   91,   43,    2,    2,   95,   40,   89,   88,  -63,  -61,  -47,  -41,  -77],
                       [   4,   66,  -52,   13,  -67,   87,  -37,  -98,   37,  -69,  -81,   30,   86,  -13,  -98,   35,   39,    2],
                       [ -89,  -92,   42,  -97,  -68,  -34,   64,   75,   -7,   91,  -84,   63,  -80,    4,   -5,   45,   34,  -49],
                       [ -77,   77,   16,  -55,  -80,  -21,   77,   78,  -31,   90,  -29,   86,   97,  -10,   55,  -10,  -19,  -62],
                       [ -50,  -20,   43,  -16,  -75,  -77,  -76,   86,  -44,   96,  -47,   75,   49,  -99,   26,   46,   75,  -88],
                       [  26,   -3,    3,   10,   88,   60,  -16,  -75,   -4,   61,   91,  -70,  -49,   81,    2,   75,  -80,  -52],
                       [  35,   40,   79,    6,  -88,   29,  -60,  -38,  -31,  -11,  -86,   43,    4,   15,  -32,  -52,  -96,  -51],
                       [ -25,  -15,   39,  -90,   24,  -55,  -92,  -72,   10,  -63,  -55,   76,   90,   43,   -5,   -1,  -79,   24],
                       [  42,  -23,   46,  -65,   57,   29,    3,  -85,  -71,   25,   91,   36,  -77,  -97,   76,   35,   69,   89],
                       [  50,  -60,  -88,   62,  -93,   -2,  -91,  -74,  -12,   17,   -5,  -17,  -54,  -77,   47,  -53,   95,   96],
                       [  90,  -58,  -14,   77,   92, -100,   13,  -33,  -78,   38,   45,   60,   43,  -69, -100,  -51,  -31,   82],
                       [ -16,   88,  -42,  -59,   67,   67,  -35,   89,  -87,  -80,   88,   -3,   75,  -14,  -16,  -27,   59,  -41],
                       [ -98,  -10,   58,   33,   66,  -37,   67,   -8,  -87,  -59,   52,   75,   23,    9,   11,    9,  -52,   -8],
                       [  78,  -28,   30,  -78,  -67,   31,  -10,   -4,   96,   32,  -49,   15,   91,  -97,  -48,   81,   23,  -45],
                       [ -66,   -8,   75,  -40,   40,  -64,    4,   60,   78,   56,   12,  -72,   63,   70,   52,   19,  -69,   18],
                       [  54,  -92,  -99,   70,  -71,  -87,  -52,   64,  -65,  -67,  -30,   83,   15,   71,  -49,  -92,    8,  -64],
                       [ -98,   81,  -41,  -56,   90,   40,   43,  -65,  -96,  -62,  -39,  -93,  -13,   -4,  -78,   75,  -29,  -39],
                       [  50,  -65,   74,   25,   94,   67,  -30,   10,  -64,  -40,  -95,   61,   -8,   47,  -69,   70,   78,    7],
                       [ -39,  -31,   17,   42,   23,  -67,   19,   63,   53,  -55,  -58,  -72,   75,  -49,   89,   -9,   83,  -25],
                       [ -35,   -7,   49,   57,   50,  -10,   -8,  -27,  -58,   31,   16,  -49,   29,  -65,   87,   18,   45,  -79],
                       [  45,   -3,    1,  -11,  -56,   95,  -35,  -99,   34,  -11,  -62,  -55,  -89,   54,   61,   58,  -57,  -60],
                       [ -91,  -47,  -14,   52,  -61,  -91,   -5,  -89,   95,   87,   29,  -38,   20,  -27,   35,  -81,   36,  -75],
                       [  20,   40,  -88,    0,  -96,   39,  -33,  -94,  -20,   89,   70,   41,   94,  -15,  -82,   53,  -86,  -54],
                       [ -33,   49,    6,  -60,   11,  -42,   98,   30,  -60,   45,  -78, -100,  -31,   35,  -84,   62,  -78,   26],
                       [ -33,  -20,  -58,  -11,   47,   95,   32,  -88,   -7,  -45,   71,   35,   35,   44,   30,  -19,  -99,   95],
                       [ -60,  -84,  -13,  -68,  -37,   23,  -48,  -16,   74,  -74,   -6,  -64,  -58,  -23,  -14,   34,   86,   50],
                       [ -74,  -59,  -93,  -10,  -64,   31,   54,   72,  -42,   50,   85,   57,  -30,   28,   75,  -85,   20,   93],
                       [   4,  -27,   99,  -83,  -49,  -67,  -38,  -36,  -96,   99,    4,  -95,   97,  -48,  -40,  -72,  -38,   84],
                       [  60,  -38,   34,   38,  -54,  -72,   79,    3,   41,  -24,   69,  -90,  -52,  -38,  -61,  -90,  -33,  -19],
                       [ -80,   84,  -52,  -76,   52,    1,    5,  -57,   18,   16,  -33,  -25,  -41,  -45,  -42,  -33,  -28,   -1],
                       [  79,   95,   75,   23,  -87,  -72,   91,  -48,   87,   -9,   69,    6,  -36,   54,   -9,   48,   89,  -16]])

        self.assertEqual(
             np.array([[   0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
                       [   0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
                       [   0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
                       [   0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
                       [   0,    0,    0,    0,  178,    0,    0,    0,    0,    0,    0,    0,    0,  531,    0,    0,    0,    0],
                       [   0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
                       [   0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
                       [   0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
                       [   0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
                       [   0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
                       [   0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
                       [   0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
                       [   0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
                       [   0,    0,    0,    0, -774,    0,    0,    0,    0,    0,    0,    0,    0,  370,    0,    0,    0,    0],
                       [   0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
                       [   0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
                       [   0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
                       [   0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
                       [   0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
                       [   0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
                       [   0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
                       [   0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
                       [   0,    0,    0,    0, -281,    0,    0,    0,    0,    0,    0,    0,    0, -367,    0,    0,    0,    0],
                       [   0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
                       [   0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
                       [   0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
                       [   0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
                       [   0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
                       [   0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
                       [   0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
                       [   0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
                       [   0,    0,    0,    0, -754,    0,    0,    0,    0,    0,    0,    0,    0, -105,    0,    0,    0,    0],
                       [   0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
                       [   0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
                       [   0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
                       [   0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0]]).tolist(),
                       concentrate(c3,9).tolist())
