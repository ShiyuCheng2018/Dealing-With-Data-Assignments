from hw7 import *
import hw7
import unittest, json, pandas as pd, os, numpy as np
from compare_pandas import *
from compare_files import compare_files

''' 
Auxiliary files needed:
compare_pandas.py, compare_files.py
N_seaice_extent_daily_v3.0.csv
raw_data.pkl, clean_data.pkl, data_79_18.pkl, data_2019.pkl
columns.json
'''

class TestFns(unittest.TestCase):
    def test_get_data(self):
        ts_correct = pd.read_pickle('raw_data.pkl')
        self.assertTrue(compare_series(ts_correct, get_data(), 0.001, dtype=True))

    def test_clean_data(self):
        ts_correct = pd.read_pickle('clean_data.pkl')
        raw = pd.read_pickle('raw_data.pkl')
        better_be_none = clean_data(raw)
        self.assertTrue(compare_series(ts_correct, raw, 0.001, dtype=True))
        self.assertIsNone(better_be_none)
   
    def test_get_column_labels(self):
        with open('columns.json') as fp:
            correct = json.load(fp) 
        self.assertEqual(correct, get_column_labels())
        
    def test_extract_df(self):
        ts_correct = pd.read_pickle('clean_data.pkl')
        df_correct = pd.read_pickle('data_79_18.pkl')
        self.assertTrue(compare_frames(df_correct, extract_df(ts_correct), 0.001))
        
    def test_extract_2019(self):
        ts_clean_correct = pd.read_pickle('clean_data.pkl')
        ts_correct = pd.read_pickle('data_2019.pkl')
        ts = extract_2019(ts_clean_correct)
        self.assertTrue(compare_series(ts_correct, ts, 0.001, dtype=True))
        
    def test_main(self):
        if os.path.exists('data_79_18.csv'):
            os.remove('data_79_18.csv')
        if os.path.exists('data_2019.csv'):
            os.remove('data_2019.csv')
        hw7.main()
        # get rid of the apply F18 - the pkl is now float
        df_correct = pd.read_pickle('data_79_18.pkl')
        df = pd.read_csv('data_79_18.csv', index_col=0)
        self.assertTrue(compare_frames(df_correct, df, 0.001, dtype=True))
        ts_correct = pd.read_pickle('data_2019.pkl')
        # this actually creates a weird Series with index.name == 0.
        # could assign to None if I cared.
        ts = pd.read_csv('data_2019.csv', header=None, parse_dates=True, squeeze=True, index_col=0) 
        self.assertTrue(compare_series(ts_correct, ts, 0.001, dtype=True))
       
def main():
    test = unittest.defaultTestLoader.loadTestsFromTestCase(TestFns)
    results = unittest.TextTestRunner().run(test)
    print('Correctness score = ', str((results.testsRun - len(results.errors) - len(results.failures)) / results.testsRun * 100) + ' / 100')
    
if __name__ == "__main__":
    main()