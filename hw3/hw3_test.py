# Version: 1.2

import numpy as np
from hw3 import *

import unittest, io
from contextlib import redirect_stdout

class TestFns(unittest.TestCase):
    def setUp(self):
        pass # no common set-up for the moment...

    def test_jar(self):
        j = Jar(9)
        self.assertFalse(j.is_full())
        j.add(5)
        self.assertFalse(j.is_full())
        self.assertEqual("Jar(5/9)", repr(j))
        j.add(10)
        self.assertEqual("Jar(9/9)", repr(j))
        self.assertTrue(j.is_full())
        self.assertEqual("Jar(0/1000)", repr(Jar(1000)))

    def test_counter_mods(self):
        c = Counter("one")
        self.assertEqual("one", c.name())
        self.assertEqual({'clicks': 0, 'max-count': 0, 'resets': 0}, c.stats())
        for i in range(20):
            c.click()

        c.reset()
        c.click()
        c.stats()
        c2 = Counter("2")
        n = 10000
        for x in range(n):
            c2.click()
            c2.click()
            c2.reset()
            
        c2.click()
            
        self.assertEqual({'clicks': 21, 'max-count': 20, 'resets': 1}, c.stats())
        self.assertEqual({'clicks': 2*n+1, 'max-count': 2, 'resets': n}, c2.stats())
        self.assertEqual("Counter(name=one, count=1)", repr(c))
        self.assertEqual("2", c2.name())
        c2.rename("one")
        self.assertEqual("Counter(name=one, count=1)", repr(c))

    def test_cg(self):
        g0 = CounterGroup()
        a = Counter("a")
        self.assertTrue(g0.add(a))
        self.assertFalse(g0.add(a))
        
        c1 = Counter("c1")
        c1.click()
        c1.click()
        c1.click()
        c2 = Counter("c2")
        c2.click()
        c3 = Counter("c3")
        c3.click()
        c3.click()

        g1 = CounterGroup()
        self.assertEqual("|<empty>|", repr(g1))
        for c in [c1,c2,c3]:
            g1.add(c)

        self.assertEqual("|Counter(name=c1, count=3),Counter(name=c2, count=1),Counter(name=c3, count=2)|", repr(g1))
        
        g2 = CounterGroup()

        for name in "testing":
            g1.add(Counter(name))
            if name < "h":
                g2.add(Counter(name+name))

        g3 = CounterGroup()
        g3.add(Counter("|,|"))
        g3.add(Counter(",a"))
        self.assertEqual("|,a,|,||", str(g3))
        

        self.assertEqual("|c1,c2,c3,e,g,i,n,s,t|", str(g1))
        self.assertEqual("|ee,gg|", str(g2))

        for i in range(7):
            g1.click_all()
            
        self.assertEqual("|Counter(name=c1, count=10),Counter(name=c2, count=8),Counter(name=c3, count=9),Counter(name=e, count=7),Counter(name=g, count=7),Counter(name=i, count=7),Counter(name=n, count=7),Counter(name=s, count=7),Counter(name=t, count=7)|", repr(g1))

        g4 = CounterGroup()
        c = Counter("z")
        c.click()
        g4.add(c)
        g4.add(Counter("a"))
        g4.add(Counter("A"))
        self.assertEqual("([Counter(name=A, count=0), Counter(name=a, count=0)], [Counter(name=z, count=1)])",repr(g4.znz()))
        
                                       
    def test_matrix_mods(self):
        m = Matrix([[1, 2, 3], [7, 5, 2]])
        self.assertEqual(6, len(m))
        self.assertTrue(5 in m)
        self.assertFalse(6 in m)
        self.assertEqual("2x3 Matrix", str(m))
        
        m2 = Matrix([[1, 2], [3, 4], [5, 6], [7, 2]])
        self.assertEqual(8, len(m2))
        self.assertEqual("4x2 Matrix", str(m2))

    def test_fill_interior(self):
        a = np.array([[13,  7,  7,  4,  8, 18, 16],
                      [ 4, 11,  7,  1,  4,  5, 18],
                      [16,  7,  8,  1,  3, 18,  9],
                      [13, 16,  7, 14,  4, 17, 17],
                      [12, 16, 11, 19,  2, 16,  5]])
        fill_interior(a, 88)
        self.assertEqual(np.array([[13,  7,  7,  4,  8, 18, 16],
                                    [ 4, 88, 88, 88, 88, 88, 18],
                                    [16, 88, 88, 88, 88, 88,  9],
                                    [13, 88, 88, 88, 88, 88, 17],
                                    [12, 16, 11, 19,  2, 16,  5]]).tolist(), a.tolist())


    def test_paint_edges(self):
        a =  np.array([[9, 5, 4, 9, 2],
                       [5, 5, 9, 5, 3],
                       [8, 8, 3, 3, 3],
                       [9, 8, 1, 9, 5],
                       [1, 1, 2, 6, 8]])
        paint_edges(a)
        self.assertEqual(np.array(   [[1, 1, 1, 1, 2],
                                       [4, 5, 9, 5, 2],
                                       [4, 8, 3, 3, 2],
                                       [4, 8, 1, 9, 2],
                                       [4, 3, 3, 3, 3]]).tolist(), a.tolist())

        a = np.array([[10, 11, 12],
                      [13, 14, 15],
                      [16, 17, 18]])
        paint_edges(a)
        self.assertEqual(np.array([[ 1,  1,  2],
                                    [ 4, 14,  2],
                                    [ 4,  3,  3]]).tolist(), a.tolist())


        a =  np.array([[9, 5, 4, 9, 2],
                       [5, 5, 9, 5, 3],
                       [8, 8, 3, 3, 3],
                       [9, 8, 1, 9, 5],
                       [1, 1, 2, 6, 8]])
                       
        paint_edges(a,100)
        self.assertEqual(np.array(   [[100, 100, 100, 100, 100],
                                       [100, 5, 9, 5, 100],
                                       [100, 8, 3, 3, 100],
                                       [100, 8, 1, 9, 100],
                                       [100, 100, 100, 100, 100]]).tolist(), a.tolist())

    def dropped_test_sums(self):
        a = np.array([[8, 3, 6, 7, 4],
                      [9, 8, 3, 5, 1],
                      [8, 7, 3, 1, 1]])

        rsum, csum, asum = sums(a)
        self.assertEqual([28, 26, 20], list(rsum.tolist()))
        self.assertEqual([25, 18, 12, 13,  6], list(csum.tolist()))
        self.assertEqual(74, asum)

if __name__ == "__main__":
    print(
"""
Oops! You shouldn't be running this file directly!
Read the 'Testing' section in the write-up again.
Mail to ista131-questions if any questions.
                                --whm""")
