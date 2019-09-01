# Hw1 tester, DRAFT!

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
       
    def test_dups_lol(self):
        self.assertFalse(dups_lol([]))
        self.assertFalse(dups_lol([[1,2]]))
        self.assertFalse(dups_lol([[1],[2]]))
        self.assertFalse(dups_lol([['python', 'fun'],['study', 'meh']]))
        self.assertFalse(dups_lol([[1,3,4],[2,7,6],[9,8,5]]))
        self.assertFalse(dups_lol([[1,2],[3,4],[5,6]]))
        self.assertTrue(dups_lol([[1,1]]))
        self.assertTrue(dups_lol([[1],[1]]))
        self.assertTrue(dups_lol([['python', 'fun'],['study', 'fun']]))
        self.assertTrue(dups_lol([[1,3,4],[2,7,6],[9,8,1]]))
        self.assertTrue(dups_lol([[1,2],[3,1],[5,6]]))
        
    def test_dups_dict(self):
        self.assertFalse(dups_dict({}))
        self.assertFalse(dups_dict({'dog':[1,2]}))
        self.assertFalse(dups_dict({'dog':[1],'cats':[2]}))
        self.assertFalse(dups_dict({'yay':['python', 'fun'],'nay':['study', 'meh']}))
        self.assertFalse(dups_dict({'vals1':[1,3,4],'vals2':[2,7,6],'vals3':[9,8,5]}))
        self.assertFalse(dups_dict({'vals1':[1,2],'vals2':[3,4],'vals3':[5,6]}))
        self.assertTrue(dups_dict({'dogs':[1,1]}))
        self.assertTrue(dups_dict({'dogs':[1],'cats':[1]}))
        self.assertTrue(dups_dict({'yay':['python', 'fun'],'nay':['study', 'fun']}))
        self.assertTrue(dups_dict({'vals1':[1,3,4],'vals2':[2,7,6],'vals3':[9,8,1]}))
        self.assertTrue(dups_dict({'vals1':[1,2],'vals2':[3,1],'vals3':[5,6]}))

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
        xself.assertEqual((3,4,4,3),corners([[3,4],[3,4]]))

    def test_count_lets(self):
        self.assertEqual([99,3,"a",1,"x"], count_lets("xaaa"))
        self.assertEqual([3, 'a', 0, 'b', 0, 'c', 0, 'd', 0, 'e', 0, 'f', 0, 'g', 0, 'h', 0, 'i', 0, 'j', 0, 'k', 0, 'l', 0, 'm', 0, 'n', 0, 'o', 0, 'p', 0, 'q', 0, 'r', 0, 's', 0, 't', 0, 'u', 0, 'v', 0, 'w', 0, 'x', 0, 'y', 0, 'z'], count_lets("aaa",True))
        self.assertEqual(
            [3, 'a', 3, 'd', 5, 'e', 3, 'h', 2, 'i', 1, 'l', 1, 'm', 2, 'n', 3, 'o', 2, 'p', 2, 'r', 5, 's', 6, 't', 2, 'u', 1, 'v', 2, 'w', 2, 'y'],
            count_lets("ISTA 131 Hw1, Due: Thursday 9/5/2019 at 23:59:59 MST, Python Review + Nested Loops"))

    def test_print_nzp(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            r1 = """
+-----+
|z p z|
|n z n|
|p n p|
+-----+
"""[1:]
            print_nzp([[0,4,0],
                       [-3,0,-4],
                       [5,-2,3]])
            self.assertEqual(r1, buf.getvalue())

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
