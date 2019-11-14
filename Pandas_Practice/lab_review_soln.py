import pandas as pd
from datetime import datetime

def is_diagonal(m):
    for r in range(len(m)):
        for c in range(len(m[0])):
            if r != c and m[r][c] != 0:
                return False
    return True
            
def is_symmetric(m):
    for r in range(len(m)):
        for c in range(len(m[0])):
            if not m[r][c] == m[c][r]:
                return False
    return True

def string_mean(s):
    nums = [float(x) for x in s.split()]
    return sum(nums)/len(nums)

#bin and hex answers
'''
BIN

178         255

39          170

HEX

0b10101011           0b00010010   
171                  18


0b00111101           0b11111111
61                   255

Hex Sequence
Ghost
'''  

def to_datetime(datestr):
    lst = datestr.split("/")
    return datetime(int(lst[2]), int(lst[0]), int(lst[1]))
    
def get_year(ts, yr):
    year = []
    for dt in ts.index:
        if dt.year == yr:
            year.append(ts[dt])
    return year
    
def argmax(df):
    max_val, row, col = df.iloc[0, 0], df.index[0], df.columns[0]
    for r in df.index:
        for c in df:
            if df.loc[r, c] > max_val:
                max_val, row, col = df.iloc[r, c], r, c
    return row, col
    
def address_frame(base_address, element_size, rows, cols):
    index = []
    for i in range(rows):
        index.append('row_' + str(i))
    columns = []
    for i in range(cols):
        columns.append('col_' + str(i))
    df = pd.DataFrame(index=index, columns=columns, dtype=int)
    for i in range(rows):
        for j in range(cols):
            df.iloc[i, j] = base_address + (i * cols + j) * element_size
    return df
    
    
def main():
    m = [[1, 0], [1, 1]]
    print(is_diagonal(m))
    
if __name__ == "__main__":
    main()
