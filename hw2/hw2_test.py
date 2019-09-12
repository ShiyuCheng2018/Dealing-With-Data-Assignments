# Version: 1.0

from hw2 import *
import unittest, io
from contextlib import redirect_stdout

class TestFns(unittest.TestCase):
    def setUp(self):
        pass # no common set-up for the moment...

    def test_first_last(self):
        self.assertEqual((10,30), first_last([10,20,30]))
        self.assertEqual((1,1), first_last([1]))
        self.assertEqual((1,9), first_last(list(range(1,10,2))))
        
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

    def test_substr_in_values(self):
        d1 = {}
        d2 = {'dog':['rocket', 'patches', 'moca', 'latte']}
        d3 = {'dog':['rocket', 'patches', 'moca', 'latte'], 'cat':['crystal', 'shamrock']}
        d4 = {'DOG':['ROCKET'],'dog':['rocket']}
        self.assertEqual([], substr_in_values(d1, 'a'))
        self.assertEqual(['dog'], substr_in_values(d2, 'rock'))
        self.assertEqual([], substr_in_values(d2, 'sim'))
        self.assertEqual(['cat', 'dog'], substr_in_values(d3, 'rock'))
        self.assertEqual(['cat', 'dog'], substr_in_values(d3, 'ROCK'))
        self.assertEqual(['dog'], substr_in_values(d3, 'patch'))
        self.assertEqual(['cat', 'dog'], substr_in_values(d3, ''))
        self.assertEqual(['DOG','dog'], substr_in_values(d4, 'ket'))
        
    def test_count_lets(self):
        self.assertEqual([4, 'a', 3, 'b', 1, 'c'], count_lets("b aa cba? AB!"))

        self.assertEqual([3, 'a', 0, 'b', 0, 'c', 0, 'd', 0, 'e', 0, 'f', 0, 'g', 0, 'h', 0, 'i',
                          0, 'j', 0, 'k', 0, 'l', 0, 'm', 0, 'n', 0, 'o', 0, 'p', 0, 'q', 0, 'r',
                          0, 's', 0, 't', 0, 'u', 0, 'v', 0, 'w', 0, 'x', 0, 'y', 0, 'z'],
                          count_lets("aaa",True))
        self.assertEqual(
            [3, 'a', 3, 'd', 5, 'e', 3, 'h', 2, 'i', 1, 'l', 1, 'm', 2, 'n', 3, 'o', 2,
            'p', 2, 'r', 5, 's', 6, 't', 2, 'u', 1, 'v', 2, 'w', 2, 'y'],
            count_lets("ISTA 131 Hw1, Due: Thursday 9/5/2019 at 23:59:59 MST, Python Review + Nested Loops"))

        self.assertEqual([], count_lets(" ?!(#&!"))

        self.assertEqual([5, 'a', 4, 'b', 3, 'c', 1, 'e', 1, 'l', 1, 'n', 1, 'o', 1, 's', 2, 't', 1, 'u'],
            count_lets(">>> count_lets(\"b aa cba? AB!\")\n[4, 'a', 3, 'b', 1, 'c']"))

        self.assertEqual([5, 'a', 4, 'b', 3, 'c', 0, 'd', 1, 'e', 0, 'f', 0, 'g', 0, 'h',
                          0, 'i', 0, 'j', 0, 'k', 1, 'l', 0, 'm', 1, 'n', 1, 'o', 0, 'p',
                          0, 'q', 0, 'r', 1, 's', 2, 't', 1, 'u', 0, 'v', 0, 'w', 0, 'x', 0, 'y', 0, 'z'],
                          count_lets(">>> count_lets(\"b aa cba? AB!\")\n[4, 'a', 3, 'b', 1, 'c']", True))


    def test_print_index(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            r = """
8 unique words: be, not, or, question, questioned, the, to, will

be : 1, 2, 3
not : 2
or : 1
question : 3
questioned : 3
the : 3
to : 1, 2, 3
will : 1
"""[1:]
            print_index("lines.txt")
            self.assertEqual(r, buf.getvalue())
            
        with io.StringIO() as buf, redirect_stdout(buf):
            r = """
54 unique words: a, and, any, are, assignment, be, citing, concise, contain, described, descriptions, docstring, documentation, does, duplicate, explaining, for, function, functions, good, helper, however, if, in, is, no, number, of, or, parameters, paraphrase, reason, require, requiredu, returned, seems, should, simply, so, that, the, there, therefore, these, this, those, to, used, value, what, write, writeup, writing, you

a : 2, 12
and : 14
any : 11, 13, 14
are : 2
assignment : 1
be : 3
citing : 13
concise : 12
contain : 12
described : 3
descriptions : 7
docstring : 12
documentation : 8
does : 13
duplicate : 7
explaining : 12
for : 7, 9
function : 13
functions : 2, 8, 9, 11
good : 3
helper : 11
however : 9
if : 9
in : 3
is : 1, 9
no : 3, 8
number : 2
of : 2
or : 7
parameters : 13
paraphrase : 7
reason : 4
require : 4
requiredu : 9
returned : 14
seems : 3
should : 11
simply : 2
so : 3
that : 2
the : 9, 13
there : 3
therefore : 8
these : 8
this : 1, 3
those : 7, 11
to : 3, 4, 7
used : 14
value : 14
what : 12
write : 9
writeup : 3
writing : 2
you : 4, 9
"""[1:]
            print_index("lines2.txt")
            self.assertEqual(r, buf.getvalue())
        with io.StringIO() as buf, redirect_stdout(buf):
            r = """
51 unique words: april, august, b, ba, bb, bc, bd, be, bf, bg, bh, bi, bj, c, ca, cabj, cb, cc, cd, ce, cf, cg, ch, ci, cj, d, da, db, december, e, f, february, fr, g, h, i, j, january, july, june, march, may, mo, november, october, sa, september, su, th, tu, we

april : 11
august : 20
b : 4, 13, 22, 31
ba : 5, 6, 14, 15, 23, 32, 33
bb : 5, 6, 14, 15, 23, 24, 32, 33
bc : 5, 6, 14, 15, 23, 24, 32, 33
bd : 6, 14, 15, 23, 24, 32, 33
be : 6, 15, 23, 24, 32, 33
bf : 6, 15, 24, 33
bg : 6, 15, 16, 24, 33
bh : 6, 7, 15, 16, 24, 33, 34
bi : 6, 7, 15, 16, 24, 25, 33, 34
bj : 6, 7, 15, 16, 24, 25, 33, 34
c : 4, 13, 14, 22, 31
ca : 7, 15, 16, 24, 25, 33, 34
cabj : 1
cb : 7, 16, 24, 25, 33, 34
cc : 7, 16, 25, 34
cd : 7, 16, 17, 25, 34
ce : 7, 8, 16, 17, 25, 34, 35
cf : 7, 8, 16, 17, 25, 26, 34, 35
cg : 7, 8, 16, 17, 25, 26, 34, 35
ch : 8, 16, 17, 25, 26, 34, 35
ci : 8, 17, 25, 26, 34, 35
cj : 8, 17, 26, 35
d : 4, 5, 13, 14, 22, 31, 32
da : 8, 17, 18, 26, 35
db : 8, 9, 17, 26, 35
december : 29
e : 4, 5, 13, 14, 22, 23, 31, 32
f : 4, 5, 13, 14, 22, 23, 31, 32
february : 2
fr : 3, 12, 21, 30
g : 5, 13, 14, 22, 23, 31, 32
h : 5, 14, 22, 23, 31, 32
i : 5, 14, 23, 32
j : 5, 14, 15, 23, 32
january : 2
july : 20
june : 11
march : 2
may : 11
mo : 3, 12, 21, 30
november : 29
october : 29
sa : 3, 12, 21, 30
september : 20
su : 3, 12, 21, 30
th : 3, 12, 21, 30
tu : 3, 12, 21, 30
we : 3, 12, 21, 30
"""[1:]
            print_index("lines3.txt")
            self.assertEqual(r, buf.getvalue())

            

    def test_four_lines(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            r = """
ABCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrstuvwxyz
0123456789
!"#$%&'()*+,-./
"""[1:]
            four_lines()
            self.assertEqual(r, buf.getvalue())
            
    def test_cp_range(self):
        self.assertEqual((97,100), cp_range("badcab"))
        self.assertEqual((46,46), cp_range("."))
        self.assertEqual((48,57), cp_range("29288119318031"))
        self.assertEqual((40,121), cp_range("mystery([(0x41,0x5),(0x2c,0x000000000),(0b101101,0b0001),(0x5a,5)]))"))
        
    def test_mystery(self):
        self.assertEqual('AAAAA-ZZZZZ', mystery([(0x41,0x5),(0x2c,0x000000000),(0b101101,0b0001),(0x5a,5)]))
        self.assertEqual(']]]^^^^^^^', mystery([(0b1011101,0b11),(0b1011110,0b111)]))
        self.assertEqual('...222', mystery([(ord('.'),len("abc")),(ord(chr(len(range(50)))),len({1:2,3:4,5:6}))]))

    def test_binhex(self):
        self.assertEqual('0101\n   5', binhex(5))
        self.assertEqual('0010 0101\n   2    5', binhex(37))
        self.assertEqual('0001 0000 0000\n   1    0    0', binhex(256))
        self.assertEqual('1111 1110\n   F    E', binhex(254))
        self.assertEqual("0111 1101\n   7    D", binhex(125))
        self.assertEqual("0111 1010 1011 0100 1001\n   7    A    B    4    9", binhex(502601))
        self.assertEqual('1100 1010 1111 1110 1011 1010 1011 1110\n   C    A    F    E    B    A    B    E',
            binhex(0xCafeBabe)) # see https://en.wikipedia.org/wiki/Magic_number_(programming)
        self.assertEqual('1100 0000 1010 0010 1001 0000 1000 1001 1010 0001 0000 0110 1011 0011 0110 1001 1010 1010 0111 0001\n   C    0    A    2    9    0    8    9    A    1    0    6    B    3    6    9    A    A    7    1',
            binhex(909693152283576251296369))

    def test_my_int(self):
        self.assertEqual(7, my_int("7"))
        self.assertEqual(131, my_int("131"))
        self.assertEqual(-131, my_int("-131"))
        self.assertEqual(101001010100, my_int("101001010100"))
        self.assertEqual(1234567890, my_int("1234567890"))
        self.assertEqual(0, my_int("0"))
        self.assertEqual(0, my_int("-000000000000"))
        self.assertEqual(131, my_int("131"))
        self.assertEqual(305, my_int("131", base=16))
        self.assertEqual(46655, my_int("ZZZ", 36))
        self.assertEqual(51839, my_int("CA7F", 16))
        self.assertEqual(3, my_int("|||", 1))
        self.assertEqual(-85077226839810975801998541637059037, my_int("-913933810687850286477017", 30))
        self.assertEqual(6562, my_int("100000001", 3))
        self.assertEqual(161875260207, my_int("10010110110000100001000111001100101111",2))
        self.assertEqual(19208032625158076564565, my_int("10010110110000100001000111001100101111",4))
        self.assertEqual(4503006022212814949384022228270120983771591339124327931, my_int("10010110110000100001000111001100101111",30))
        self.assertEqual(1350603213372875805324098512367532454283588743289490456636, my_int("10010110110000100001000111001100101111",35))
        self.assertEqual(3830027075366444490061718616210232549774642936477852393333, my_int("10010110110000100001000111001100101111",36))


if __name__ == "__main__":
    print(
"""
Oops! You shouldn't be running this file directly!
Read the 'Testing' section in the write-up again.
Mail to ista131-questions if any questions.
                                --whm""")
