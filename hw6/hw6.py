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
    dataframe["Region"] = dataframe["Region"].str.strip()
    dataframe["Region"] = dataframe["Region"].str.title()
    dataframe.index.name = None
    dataframe.index = dataframe.index[:].str.strip()
    return dataframe

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
    dataframe["Growth Rate"] = dataframe["Birthrate"] - dataframe["Deathrate"]
    return dataframe


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
                # print(dataframe.index[rate], dataframe["Years to Extinction"][rate])

    return dataframe



def dying_countries():
    pass


def main():
    """
    This function that prints out the five countries that are going to extinction sooner
    :return:
    """
    csv = "countries_of_the_world.csv"
    DataFrame = csv_to_dataframe(csv)
    # print(format_df(DataFrame))
    # print(pd.read_pickle('all_countries1.pkl').index[:])
    countries = years_to_extinction(growth_rate(format_df(DataFrame)))

    countries_extinction = []
    extinctions = []
    for country in range(len(countries)):
        if(countries["Years to Extinction"][country]) > 0:
            countries_extinction.append((countries.index[country], countries["Years to Extinction"][country]))
            extinctions.append(countries["Years to Extinction"][country])

    for extinction in sorted(list(set(extinctions)))[:5]:
        for country in countries_extinction:
            if extinction == country[1]:
                print(str(country[0])+": "+str(country[1])+" Years to Extinction")


if __name__ == "__main__":
    main()
