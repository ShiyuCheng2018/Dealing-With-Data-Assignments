import numpy as np


class Jar:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__items = 0

    def add(self, add):
        if not self.is_full():
            if self.__items + add < self.__capacity:
                self.__items += add
            else:
                self.__items = self.__capacity

    def is_full(self):
        return self.__capacity == self.__items

    def __repr__(self):
        return f"Jar({self.__items}/{self.__capacity})"


class Counter:
    def __init__(self, name):
        self.__name = name
        self.__dict = {"clicks": 0, "max-count": 0, "resets": 0}
        self.__cur_click = 0

    def name(self):
        return self.__name

    def rename(self, new_name):
        self.__name = new_name

    def click(self):
        self.__dict["clicks"] += 1
        self.__cur_click += 1

        if self.__cur_click > self.__dict["max-count"]:
            self.__dict["max-count"] = self.__cur_click

    def reset(self):

        self.__cur_click = 0
        self.__dict["resets"] += 1

    def stats(self):
        return self.__dict

    def __repr__(self):
        return f"Counter(name={self.name()}, count={self.__dict['max-count']})"

    def __str__(self):
        return f"Counter {self.name()}:{self.__dict['max-count']}"


class CounterGroup:

    def __init__(self):
        self.__counterGroup = {}

    def add(self, add_counter):
        if add_counter.name() in sorted(self.__counterGroup.keys()):
            return False

        self.__counterGroup[add_counter.name()] = add_counter
        return True

    def counters(self):
        counters = []
        for counter in sorted(self.__counterGroup.keys()):
            counters.append(self.__counterGroup[counter])
        return counters

    def click_all(self):
        for counter in sorted(self.__counterGroup.keys()):
            self.__counterGroup[counter].click()

    def znz(self):
        first = []
        second = []
        for counter in sorted(self.__counterGroup.keys()):
            if self.__counterGroup[counter].stats()['max-count'] == 0:
                first.append(self.__counterGroup[counter])
            else:
                second.append(self.__counterGroup[counter])
        return first, second

    def __str__(self):
        string = "|"
        for counter in sorted(self.__counterGroup.keys()):
            string += self.__counterGroup[counter].name()+","

        return string[:-1]+"|"

    def __repr__(self):
        string = "|"

        if self.__counterGroup == {}:
            return string + "<empty>"+"|"

        for counter in sorted(self.__counterGroup.keys()):
            string +=  repr(self.__counterGroup[counter]) + ","
        return string[:-1]+"|"


class Matrix:

    def __init__(self, matrix):
        self.__matrix = matrix

    def __len__(self):
        return len(self.__matrix) * len(self.__matrix[0])

    def __contains__(self, item):
        if str(item) in repr(self):
            return True
        return False

    def __str__(self):
        return f"{len(self.__matrix)}x{len(self.__matrix[0])} Matrix"

    def __repr__(self):
        string = ""
        for row in self.__matrix:
            for col in row:
                string += str(col) + "      "
            string += "\n"

        return string


def fill_interior(array, value):
    array[1:-1, 1:-1] = value


def paint_edges(array, color=""):

    if color == "":
        array[0][0:-1] = 1
        array[0:-1, -1] = 2
        array[-1, 1:] = 3
        array[1:, 0] = 4
    else:
        array[0] = color
        array[-1] = color
        array[1:-1, 0] = color
        array[1:-1, -1] = color


def sums(array):

    return np.array(array).sum(axis=1), np.array(array).sum(axis=0), np.array(array).sum()


def q1():
    return '''
        >>>a = np.array([[1,2,3],[4,5]])
        >>>a
        >>>array([list([1, 2, 3]), list([4, 5])], dtype=object)
        
        I thought it would throw an error before testing, however, it does not. I figured it makes sense tho,
        since I did not intent to make a matrix, just an 2D array which allows each row has an unique length of elements.
        
    '''


def q2():
    return '''
    >>>import numpy as np
    >>>a = np.array([1,2,3,4,5])
    >>>a
    array([1, 2, 3, 4, 5])
    >>>a.dtype
    >>>dtype('int64')
    >>>a.dtype = 'float32'
    >>>a
    array([1.e-45, 0.e+00, 3.e-45, 0.e+00, 4.e-45, 0.e+00, 6.e-45, 0.e+00,
           7.e-45, 0.e+00], dtype=float32)
    >>>a.dtype = 'int32'
    >>>a
    array([1, 0, 2, 0, 3, 0, 4, 0, 5, 0], dtype=int32)
    >>>a.dtype = 'int16'
    >>>a
    array([1, 0, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 4, 0, 0, 0, 5, 0, 0, 0],
          dtype=int16)
    >>>a.dtype = 'int64'
    >>>a
    array([1, 2, 3, 4, 5])
        
    '''

def q3():
    return '''
    >>>x = np.array([{'x': 2, 'y': 5}])
    >>>x
    array([{'x': 2, 'y': 5}], dtype=object)
    >>>x.item()
    {'x': 2, 'y': 5}
    >>>x.keys()
    Traceback (most recent call last):
      File "<input>", line 1, in <module>
    AttributeError: 'numpy.ndarray' object has no attribute 'keys'
    >>>x.key()
    Traceback (most recent call last):
      File "<input>", line 1, in <module>
    AttributeError: 'numpy.ndarray' object has no attribute 'key'
    >>>x[0]['y']
    5
    >>>x[0].keys()
    dict_keys(['x', 'y'])
    >>>x[0].items()
    dict_items([('x', 2), ('y', 5)])
    '''


def q4():
    return '''
        1) a = Counter("test")
            English: Instance class Counter as a variable a with passing "test"
        
        2) a.click()
            English: call click() function from a
        
        3) F([Counter("a"), Counter("b")])
            English: passing an array with two Counter (passing "a", "b" respectively) objects as a reference of f function
        
        4)print([Counter("a"), Counter("b")][0])
            English: print an array with two Counter objects out with Counter special method __str__
    
    '''


def estimated_hours():
    return 10


def observation():
    return '''
        observation 1: https://docs.scipy.org/doc/numpy-1.10.1/user/basics.rec.html. This document page gave me great examples
                       of structured arrays in numpy, and how to manipulate dtypes
                       
        observation 2: The length of this assignment is very fair and really helped me to review Python class. Numpy is a very
                        interesting framework, it is perfectly working in order to manipulate numpy.array 
    
    '''