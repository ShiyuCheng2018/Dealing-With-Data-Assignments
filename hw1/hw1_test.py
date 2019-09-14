# Hw1 unit tests, version 1.0

from hw1 import *
import unittest
from contextlib import redirect_stdout
import io

class TestFns(unittest.TestCase):
    def setUp(self):
        self.m0 = [[]]
        self.m1 = [[0]] # diagonal, triangular
        self.m2 = [[1]] # diagonal, triangular
        self.m3 = [[1, 0], 
                   [0, 1]] # diagonal, triangular
        self.m4 = [[0, 0], 
                   [0, 0]] # diagonal, triangular
        self.m5 = [[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 9]] # neither
        self.m6 = [[1, 2, 3], 
                   [0, 5, 6], 
                   [0, 0, 9]] # upper tri
        self.m7 = [[1, 0, 0], 
                   [4, 5, 0], 
                   [7, 8, 9]] # lower tri
        self.m8 = [[1, 0, 0], 
                   [4, 5, 0], 
                   [-7, -8, -9]] # lower tri
        self.m9 = [[1, 0, 0], 
                   [5, 5, 0], 
                   [-7, -8, -9]] # lower tri
        self.m10 = [[1, 1, 0], 
                    [0, 5, 0], 
                    [0, 0, -9]] # upper tri
        self.m11 = [[1, 0], 
                    [0, 1], 
                    [0, 0]] # diagonal
        self.m12 = [[1, 0, 0], 
                    [0, 1, 0]] # diagonal
        self.m13 = [[1, 0], 
                    [0, 1], 
                    [0, 8]] # neither
        self.m14 = [[1, 0, 0], 
                    [0, 1, 8]] # neither
        self.m15 = [[1], 
                    [0], 
                    [3]] # neither
        self.m16 = [[1, 0, 3]] # neither               
        self.m17 = [[-45, -12, -13], 
                    [-14, -15, -16], 
                    [-17, -18, -9]] # neither
        self.m18 = [[-45, -12, -13], 
                    [-14, -15, -16], 
                    [-17, -18, -9]] # neither
        self.m19 = [[1, 1, 0], 
                    [-1, 5, 0], 
                    [0, 0, -9]] # neither
        self.m20 = [[1, 2, 3], 
                    [1, 5, 6], 
                    [0, -1, 9]] # not upper tri
        self.m21 = [[1, 0], 
                    [0, 1], 
                    [0, 0], 
                    [0, 8]] # neither
        self.m22 = [[1, 0, 0, 0], 
                    [0, 1, 0, 8]] # neither
        self.m23 = [[1, 0], 
                    [0, 1], 
                    [0, 0], 
                    [0, 0]] # diagonal
        self.m24 = [[1, 0, 0, 0], 
                    [0, 1, 0, 0]] # diagonal
        self.m25 = [[1, 0, 0, 0], 
                    [0, 1, 8, 0]] # neither
        self.m26 = [[9, 8], 
                    [0, 0]]
        self.m27 = [[9], 
                    [0]]
        self.m28 = [[9, 8]]
        
    def test_middle(self):
        self.assertEqual(5, middle([3,5,7]))
        self.assertEqual("b", middle(" a b c- ".split()))

    def test_around(self):
        self.assertEqual((3,4,5), around(4))
        self.assertEqual((2,4,6), around(4,2))
        self.assertEqual((-5,0,5), around(0,interval=5))

    def test_second_biggest(self):
        self.assertEqual(4, second_biggest([1,2,3,4,5]))
        self.assertEqual(40, second_biggest([32,  3, 26,  5,  5, 32, 17, 40, 34, 42]))
        self.assertEqual(34, second_biggest([32,  3, 26,  5,  5, 32, 17, 40, 34, -42]))
        self.assertEqual(71, second_biggest([ 29,  71,  52, -17,  99,   9,   4]))
        self.assertEqual(4, second_biggest([5, 4, 3, 2, 1]))
        self.assertEqual(5, second_biggest([5, 4, 3, 2, 1, 2, 3, 4, 5, 6]))
        self.assertEqual(6, second_biggest([7, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6]))
        self.assertEqual(12, second_biggest([12, 12, 12]))
        self.assertEqual(12, second_biggest([12, 12, 12]))
        self.assertEqual(-4751433543177166420, second_biggest([-9172997208545430121, -6261421986659827751, -6776445639395506310, -7611105336578200572, -7090165692420484881, -8176708890984671245, -5838559672576929164, -8497913531347285206, -5135315061876505912, -6141249917775242390, -5816574962527138022, -7841515860727383988, -6813440665901309647, -8561784316437323150, -5080440722645407900, -7831566073062440929, -6594994920204194183, -4647440541814192807, -4751433543177166420, -4794507894426376645]))
        self.assertEqual(15714414278, second_biggest([16316105278, 5157598875, -10148355512, -14796614125, 12671699739, 14936087251, -17122891517, -14796614125, 12671699739, 14936087251, -17122891517, -8289644049, -13330661612, -5746216341, 6415201071, 6604275455, 11000183874, 5496966180, 6585805730, 15714414278, 5205878922, 8189210683, 13878332564, -15911926276]))
    
    def test_get_column(self):
        self.assertEqual([3,4,7],get_column([[3,5],[4,2],[7,1]],0))
        self.assertEqual([3,4,7],get_column([[3,5],[4,2],[7,1]],0,False))
        self.assertEqual([20,1,2,5],get_column([[3,5],[4,2],[7,1],[10,20]],1,True))
        self.assertEqual([1,0],get_column(self.m14,-2,reverse=True))

    def test_is_diagonal(self):
        self.assertTrue(is_diagonal(self.m1))
        self.assertTrue(is_diagonal(self.m2))
        self.assertTrue(is_diagonal(self.m3))
        self.assertTrue(is_diagonal(self.m4))
        self.assertFalse(is_diagonal(self.m5))
        self.assertFalse(is_diagonal(self.m6))
        self.assertFalse(is_diagonal(self.m7))
        self.assertTrue(is_diagonal(self.m11))
        self.assertTrue(is_diagonal(self.m12))
        self.assertFalse(is_diagonal(self.m13))
        self.assertFalse(is_diagonal(self.m14))
        self.assertFalse(is_diagonal(self.m19))
        self.assertFalse(is_diagonal(self.m21))
        self.assertFalse(is_diagonal(self.m22))
        self.assertFalse(is_diagonal(self.m25))
        self.assertTrue(is_diagonal(self.m23))
        self.assertTrue(is_diagonal(self.m24))
        
    def test_is_upper_triangular(self):
        self.assertTrue(is_upper_triangular(self.m1))
        self.assertTrue(is_upper_triangular(self.m2))
        self.assertTrue(is_upper_triangular(self.m3))
        self.assertTrue(is_upper_triangular(self.m4))
        self.assertFalse(is_upper_triangular(self.m5))
        self.assertTrue(is_upper_triangular(self.m6))
        self.assertFalse(is_upper_triangular(self.m7))
        self.assertTrue(is_upper_triangular(self.m10))
        self.assertFalse(is_upper_triangular(self.m20))
        
    def test_contains(self):
        self.assertTrue(contains(self.m1, 0))
        self.assertFalse(contains(self.m1, 1))
        self.assertFalse(contains(self.m0, 0))
        self.assertFalse(contains(self.m0, 1))
        self.assertTrue(contains(self.m7, 0))
        self.assertTrue(contains(self.m7, 5))
        self.assertTrue(contains(self.m7, 9))
        self.assertTrue(contains(self.m7, 8))
        self.assertFalse(contains(self.m7, -1.3))
        self.assertTrue(contains(self.m13, 8))
        self.assertTrue(contains(self.m14, 8))
        self.assertTrue(contains(self.m21, 8))
        self.assertTrue(contains(self.m22, 8))
        self.assertTrue(contains(self.m25, 8))
       
    def test_biggest(self):
        self.assertEqual(0, biggest(self.m1))
        self.assertEqual(1, biggest(self.m3))
        self.assertEqual(9, biggest(self.m7))
        self.assertEqual(5, biggest(self.m8))
        self.assertEqual(3, biggest(self.m15))
        self.assertEqual(3, biggest(self.m16))
        self.assertEqual(-9, biggest(self.m17))
        self.assertEqual(self.m18, self.m17)
        
    def test_indices_biggest(self):
        self.assertEqual([(0,0)], indices_biggest(self.m1))
        self.assertEqual([(0,0)], indices_biggest(self.m2))
        self.assertEqual([(0,0),(1,1)], indices_biggest(self.m3))
        self.assertEqual([(2,2)], indices_biggest(self.m5))
        self.assertEqual([(1,1)], indices_biggest(self.m8))
        self.assertEqual([(2,1)], indices_biggest(self.m13))
        m1 = [[1, 1, 1],
              [0, 1, 0],
              [1, 0, 0]]
        self.assertEqual([(0,0),(0,1),(0,2),(1,1),(2,0)], indices_biggest(m1))

        m2 = [[3, 2, 0, 1, 2],
              [2, 3, 1, 0, 2],
              [3, 2, 0, 2, 2]]
        self.assertEqual([(0,0),(1,1),(2,0)], indices_biggest(m2))
        
    def test_indices_divisible_by_3(self):
        self.assertEqual([], indices_divisible_by_3(self.m0))
        self.assertEqual([0], indices_divisible_by_3(self.m1))
        self.assertEqual([1], indices_divisible_by_3(self.m2))
        self.assertEqual([1], indices_divisible_by_3(self.m3))
        self.assertEqual([0], indices_divisible_by_3(self.m4))
        self.assertEqual([1, 6, 8], indices_divisible_by_3(self.m5))
        self.assertEqual([1, 6, 0], indices_divisible_by_3(self.m6))
        
    def test_sort_int_string(self):
        self.assertEqual("-17 4 42", sort_int_string("42 4 -17"))
        self.assertEqual("-3 -1", sort_int_string("-1 -3"))
        self.assertEqual("-17 4 42", sort_int_string("\t42   4 -17  \n"))
        self.assertEqual("3 3 3 4 4 4 5 5 5", sort_int_string("5 5 5 4 4 4 3 3 3"))
        self.assertEqual("", sort_int_string(""))
        self.assertEqual("", sort_int_string("\t"))
        self.assertEqual("1", sort_int_string("1"))
       
    def test_create_matrix(self):
        self.assertEqual([[1, 2, 3], [40, 3, 1], [3, 1, 3]], create_matrix("1 2 3/ 40 3 1/ 3  1  3"))
        self.assertEqual(self.m18, create_matrix("-45 -12 -13/-14 -15 -16    /   -17 -18 -9           "))
        self.assertEqual(self.m19, create_matrix("1 1 0/-1 5 0/0 0 -9"))
        self.assertEqual(self.m21, create_matrix("1 0/0 1/       0 0/0 8"))
        self.assertEqual(self.m22, create_matrix("1 0 0 0/0 1 0 8"))
        self.assertEqual([[10],[20]], create_matrix("10/20"))
        self.assertEqual([[723094823904823820482304280]], create_matrix("723094823904823820482304280"))
        self.assertEqual([[72309482390,4823820482304280]], create_matrix("72309482390 4823820482304280"))

    def test_corners(self):
        self.assertEqual((10, 5, 4, 8),corners([[10,3,5],[3,1,7],[8,9,4]]))
        self.assertEqual((7,7,7,7),corners([[7]]))
        self.assertEqual((3,4,4,3),corners([[3,4]]))
        self.assertEqual((3,4,4,3),corners([[3,4],[3,4]]))

    def test_print_nzp(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            r = """
+---+
|z p|
|n z|
|p n|
+---+
"""[1:]


            print_nzp([[0,4],
                       [-3,0],
                       [5,-2]])
            self.assertEqual(r, buf.getvalue())
            
        with io.StringIO() as buf, redirect_stdout(buf):
            r = """
+-----+
|z p z|
|n z n|
|p n p|
+-----+
"""[1:]
            print_nzp([[0,4,0],
                       [-3,0,-4],
                       [5,-2,3]])
            self.assertEqual(r, buf.getvalue())
            
        with io.StringIO() as buf, redirect_stdout(buf):
            r = """
+-----+
|n n n|
+-----+
"""[1:]
            print_nzp([[-100,-4,-20],
                       ])
            self.assertEqual(r, buf.getvalue())

        with io.StringIO() as buf, redirect_stdout(buf):
            r = """
+---------------+
|n n p p n p p n|
|p n n n z n n z|
|n p p p n p p z|
|n n n p n n n z|
|p p p p n n p n|
|p n n z p p n p|
|z p n n p p p n|
|p n n n n n n p|
|n n p p p n p n|
|p p z p p p p n|
|z n n p n p p n|
|n n n p n n n p|
+---------------+
"""[1:]
            print_nzp([[-5, -5,  1,  1, -4,  3,  4, -3],
                       [ 2, -2, -5, -2,  0, -3, -5,  0],
                       [-1,  2,  4,  4, -2,  3,  4,  0],
                       [-3, -1, -2,  3, -3, -2, -2,  0],
                       [ 1,  4,  1,  4, -5, -1,  1, -3],
                       [ 4, -2, -3,  0,  4,  1, -3,  1],
                       [ 0,  4, -2, -1,  1,  1,  3, -5],
                       [ 4, -1, -3, -1, -2, -1, -3,  3],
                       [-1, -1,  1,  1,  3, -5,  2, -1],
                       [ 1,  2,  0,  1,  2,  3,  4, -2],
                       [ 0, -4, -3,  3, -2,  1,  1, -1],
                       [-4, -2, -1,  2, -4, -1, -2,  3]]
                       )
            self.assertEqual(r, buf.getvalue())


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestFns)
    print("type(suite)",type(suite))
    results = unittest.TextTestRunner().run(suite)
    print("type(results)",type(results))
    print(results)
    print('Correctness score = ', str((results.testsRun - len(results.errors) - len(results.failures)) / results.testsRun * 100) + '%')
    for fault in results.errors + results.failures:
        test_name = str(fault[0]).split()[0]
        print(test_name)

    try:
        print("Hours: ",estimated_hours())
    except:
        print("No hours...")
    try:
        print("Observations: ",observations())
    except:
        print("No observations...")
