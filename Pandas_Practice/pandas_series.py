import pandas as pd
import numpy as np


# 1. Write a Python program to create and display a one-dimensional array-like object containing an array of data using Pandas module.
def make_series():
    ds = pd.Series([2, 4, 6, 8, 10])
    print(ds)
    print()
    print(ds.iloc[0])
    return ds

# 2. Write a Python program to convert a Panda module Series to Python list and it's type.
def serise_to_list():
    ds = pd.Series([2, 4, 6, 8, 10])
    print("Pandas Series and type")
    print(ds)
    print(type(ds))
    print("Convert Pandas Series to Python list")
    print(ds.tolist())
    print(type(ds.tolist()))

# 3. Write a Python program to add, subtract, multiple and divide two Pandas Series.Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 9]
def add_subtract_multiple_divide():
    ds1 = pd.Series([2, 4, 6, 8, 10])
    ds2 = pd.Series([1, 3, 5, 7, 9])
    ds = ds1 + ds2
    print("Add")
    print(ds)
    print("Subtract")
    ds = ds1 - ds2
    print(ds)
    print("Multiple")
    ds = ds1 * ds2
    print(ds)
    print("divide")
    ds = ds1 / ds2
    print(ds)

# 4. Write a Python program to get the largest integer smaller or equal to the division of the inputs.Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 9]
def compare_series():
    ds1 = pd.Series([2, 4, 6, 8, 10])
    ds2 = pd.Series([1, 3, 5, 7, 10])
    print("Equals:")
    print(ds1 == ds2)
    print("Greater than:")
    print(ds1 > ds2)
    print("Less than:")
    print(ds1 < ds2)

# 5. Write a Python program to convert a dictionary to a Pandas series.

def dictionary_to_series(dict):
    print("Original dictionary")
    print(dict)
    new_series = pd.Series(dict)
    print("Converted series: ")
    print(new_series)

# 6. Write a Python program to convert a NumPy array to a Pandas series.
def numpyarray_pandasseries():
    np_array = np.array([10, 20, 30, 40, 50])
    print("Numpy array:")
    print(np_array)
    new_series = pd.Series(np_array)
    print("Converted Pandas series: ")
    print(new_series)

# 7. Write a Python program to change the data type of given a column or a Series.
# 8. Write a Python Pandas program to convert the first column of a DataFrame as a Series.
# 9. Write a Pandas program to convert a given Series to an array.
# 10. Write a Pandas program to convert Series of lists to one Series.
# 11. Write a Pandas program to sort a given Series.
# 12. Write a Pandas program to add some data to an existing Series.
# 13. Write a Pandas program to create a subset of a given series based on value and condition.
# 14. Write a Pandas program to change the order of index of a given series.
# "15. Write a Pandas program to create the mean and standard deviation of the data of a given Series."

def tryme():
    data = np.arange(16).reshape(4, 4)
    df = pd.DataFrame(data, index=["one", "two", "three", "four"], columns=["a", "b", "c", "d"])
    print(df)
    print()
    print("df.loc['one', 'a'] = ", df.loc["one", "a"])
    print("df.iloc[0, 0] = ", df.iloc[0, 0])
    print()
    print("df.loc['one':'two', 'a':'b'] : ")
    print(df.loc['one':'two', 'a':'b'])
    print()
    print("df.iloc[0:2, 0:2] : ")
    print(df.iloc[0:2, 0:2])
    print()
    print('df[["a", "b"]] : ')
    print(df[["a", "b"]])
    print()
    print("df.index : ")
    print(df.index)
    print()
    print("[i for i in df] : ")
    print([i for i in df])
    print()



def main():
    make_series()
    # serise_to_list()
    # add_subtract_multiple_divide()
    # compare_series()
    dict = {"a": 100, "b": 200, "c": 300, "d": 400, "e": 800}
    # dictionary_to_series(dict)
    # numpyarray_pandasseries()
    # tryme()

if __name__ == '__main__':
    main()