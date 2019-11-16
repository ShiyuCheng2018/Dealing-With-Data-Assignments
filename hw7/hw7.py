# Shiyu Cheng 23329948
# Fri. 11:00-1:00 Hayley
# 11/15/2019
# hw7


import datetime
import pandas as pd
import numpy as np

def get_data():
    """
    This function hard code a csv file, and return a nice format DataFrame
    :return: DataFrame
    """
    df = pd.read_csv("N_seaice_extent_daily_v3.0.csv", skiprows=2,names=[0, 1, 2, 'Extent'], usecols=[0, 1, 2, 3], parse_dates={'Dates':[0, 1, 2]}, header=None)
    df.index = df["Dates"]
    df_extent = df["Extent"]
    del df_extent.index.name

    start = datetime.datetime(1978, 10, 26)
    end = datetime.datetime(2019, 10, 17)
    index = pd.date_range(start, end)

    # print(df_extent.reindex(index))
    return df_extent.reindex(index)


def clean_data(series):
    """
    This function pass a Series, and fill missing data days
    :param series: Series
    :return: nothing
    """

    for cur_day in range(0, len(series.index)):
        # print(str(series.iloc[cur_day]))
        pre_day = cur_day - 1
        fol_day = cur_day + 1
        if str(series.iloc[cur_day]) == "nan":
            if(str(series.iloc[fol_day]) != "nan") and str(series.iloc[pre_day]) != "nan":
                series.iloc[cur_day] = (series.iloc[pre_day] + series.iloc[fol_day]) / 2

    for cur_day in range(0, len(series.index)):
        if(str(series.iloc[cur_day]) == "nan"):
            same_day_fol_year = series.index[cur_day] + datetime.timedelta(days=366)
            same_day_pre_year = series.index[cur_day] - datetime.timedelta(days=365)
            series.iloc[cur_day] = (series[same_day_fol_year] + series[same_day_pre_year]) / 2

def get_column_labels():
    '''
    This function generates and return a list of date with the format mmdd
    :return: list
    '''

    mmdd = []
    start = datetime.datetime.strptime("2019-01-01", "%Y-%m-%d")
    end = datetime.datetime.strptime("2019-12-31", "%Y-%m-%d")
    index = pd.date_range(start, end)

    for date in index.tolist():

        if len(str(date.day)) == 1:
            day = "0"+str(date.day)
        else:
            day = str(date.day)
        if len(str(date.month)) == 1:
            month = "0"+str(date.month)
        else:
            month = str(date.month)
        mmdd.append(month+day)

    return mmdd

def extract_df(data):
    '''
    This function taks cleaned Series and return a new DataFrame. Years from 1979-2018
    :param data: Series
    :return: DataFrame
    '''
    # print(data)
    lables = [year for year in range(1979, 2019)]
    mmdd = get_column_labels()

    matrix = []

    for label in lables:
        row = []
        for index in data.index:
            if str(label) == str(index.year) and (str(index.month)+str(index.day) !="229" ):
                row.append(data.loc[index])
        # print(len(row))
        matrix.append(row)

    frame = pd.DataFrame(matrix,lables, mmdd)

    return frame

def extract_2019(data):
    """
    this function take a Series as an argument
    :param data: Series
    :return: Series
    """
    for index in range(len(data.index)):
        if(data.index[index].year == 2019):
            index_2019 = index
            break

    return data.iloc[index_2019:]

def main():
    """
    a series steps to make csv files.
    :return:
    """
    Series = get_data()
    clean_data(Series)
    get_column_labels()
    extract_df(Series).to_csv("data_79_18.csv")
    extract_2019(Series).to_csv("data_2019.csv")

if __name__ == "__main__":
    main()
