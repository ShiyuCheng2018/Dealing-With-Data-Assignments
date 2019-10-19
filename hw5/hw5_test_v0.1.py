from hw5 import *
import unittest, numpy as np, pandas as pd, json, sqlite3 
from compare_pandas import *

''' 
Auxiliary files needed:
    compare_pandas.py
    sun_frame.pkl, daylength_series.pkl, results_frame.pkl
This one is needed by hw5.py and is therefore required:
    sunrise_sunset.csv
'''

class TestFns(unittest.TestCase):
    def test_read_frame(self):
        correct = pd.read_pickle('sun_frame.pkl')
        sf = read_frame()
        self.assertTrue(compare_frames_str(correct, sf))
        
    def test_get_series(self):
        rise_correct = pd.read_pickle('sunrise.pkl')
        set_correct = pd.read_pickle('sunset.pkl')
        sun_frame = pd.read_pickle('sun_frame.pkl')
        rise, set = get_series(sun_frame)
        self.assertTrue(compare_series_str(rise_correct, rise))
        self.assertTrue(compare_series_str(set_correct, set))
   
    def test_longest_day(self):
        rise_correct = pd.read_pickle('sunrise.pkl')
        set_correct = pd.read_pickle('sunset.pkl')
        self.assertEqual((pd.Timestamp('2018-06-18 00:00:00', freq='D'), '1416'), longest_day(rise_correct, set_correct))

    def test_sunrise_dif(self):
        rise = pd.read_pickle('sunrise.pkl')
        entries = {

                   '2018-4-1 00:00:00': 125,
                    '2018-4-17 00:00:00': 116,
                    '2018-06-18 00:00:00': 19,
                    '2018-05-27 00:00:00': 59,
                    '2018-05-18 00:00:00': 75}

        for key, val in entries.items():
            self.assertEqual(val, sunrise_dif(rise, pd.Timestamp(key, freq = 'D')))
    
def main():
    test = unittest.defaultTestLoader.loadTestsFromTestCase(TestFns)
    results = unittest.TextTestRunner().run(test)
    print('Correctness score = ', str((results.testsRun - len(results.errors) - len(results.failures)) / results.testsRun * 100) + ' / 100')
    
if __name__ == "__main__":
    main()