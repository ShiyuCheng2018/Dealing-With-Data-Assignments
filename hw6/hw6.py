# Shiyu Cheng 23329948
# Fri. 11:00-1:00 Hayley
# 10/25/2019
# hw6

from datetime import timedelta
import pandas as pd
import numpy as np

def csv_to_dataframe(csv):
    """
    This function transfer csv to dataframe
    :param csv:
    :return: DataFrame
    """
    data = pd.read_csv(csv,thousands='.', decimal=',', index_col=[0])
    return data


def format_df(dataframe):
    """
    This file well formats DataFrame
    :param dataframe:
    :return: DataFrame
    """
    dataframe.Region = dataframe.Region.str.title().str.strip()
    dataframe.index = dataframe.index.str.strip()
    dataframe.index.name = None

def dod(p, r):
    num_yrs = 0
    while p > 2:
        p = p + p * r/1000
        num_yrs += 1
    return num_yrs

def growth_rate(dataframe):
    """
    This function calculate growth rate of each country and add into DataFrame
    :param dataframe:
    :return: DataFrame
    """
    dataframe["Growth Rate"] = dataframe.Birthrate - dataframe.Deathrate


def years_to_extinction(dataframe):
    """
    This function calculate countries which have negetive growth rate
    :param dataframe:
    :return: DataFrame
    """

    dataframe["Years to Extinction"] = np.nan
    for rate in range(len(dataframe["Growth Rate"])):
        the_rate = dataframe["Growth Rate"][rate]
        if the_rate != "nan":
            if the_rate < 0:
                dataframe["Years to Extinction"][rate] = dod(dataframe["Population"][rate], the_rate)

def dying_countries(df):
    df = df["Years to Extinction"]
    a = 0
    for i in range(len(df)):
        if str(df.iloc[a]) == "nan":
            df.drop(df.index[a], inplace=True)
        else:
            a += 1
    df = df.sort_values(ascending=True)
    return df


def main():
    """
    This function that prints out the five countries that are going to extinction sooner
    :return:
    """
    df = csv_to_dataframe('countries_of_the_world.csv')
    format_df(df)
    growth_rate(df)
    years_to_extinction(df)
    d_df = dying_countries(df)
    for i in range(0, 5):
        print(str(d_df.index[i]) + ": " + str(d_df[i]) + " " + str(d_df.name))

if __name__ == "__main__":
    main()
