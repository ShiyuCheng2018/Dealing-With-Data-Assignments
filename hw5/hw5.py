# Shiyu Cheng 23329948
# Fri. 11:00-1:00 Hayley
# 10/18/2019
# hw5

from datetime import timedelta
import pandas as pd


def read_frame():
    """
    This function does not take any parameter, it converts cvs file to DataFrame
    :return: DataFrame
    """

    months = ["Jan_r", "Jan_s", "Feb_r", "Feb_s", "Mar_r", "Mar_s", "Apr_r", "Apr_s", "May_r", "May_s", "Jun_r",
              "Jun_s",
              "Jul_r", "Jul_s", "Aug_r", "Aug_s", "Sep_r", "Sep_s", "Oct_r", "Oct_s", "Nov_r", "Nov_s", "Dec_r",
              "Dec_s"]

    return pd.read_csv("sunrise_sunset.csv", dtype=str, names=months)


def get_series(sunFrame):
    """
    This function takes DataFrame as paramter and return two series based on the parameter.
    :param sunFrame:
    :return: rise series and set serise
    """
    rise_months = ["Jan_r", "Feb_r", "Mar_r", "Apr_r", "May_r", "Jun_r", "Jul_r", "Aug_r", "Sep_r", "Oct_r", "Nov_r",
                   "Dec_r"]
    set_months = ["Jan_s", "Feb_s", "Mar_s", "Apr_s", "May_s", "Jun_s", "Jul_s", "Aug_s", "Sep_s", "Oct_s", "Nov_s",
                  "Dec_s"]

    rise = pd.concat([sunFrame[month] for month in rise_months]).dropna()
    rise.index = pd.date_range(start='1/1/2018', end='12/31/2018')
    set = pd.concat([sunFrame[month] for month in set_months]).dropna()
    set.index = pd.date_range(start='1/1/2018', end='12/31/2018')

    return rise, set


def longest_day(rise, sunset):
    """
    This function takes two Pandas series as the parameter, and return the longest day in a year
    :param rise:
    :param sunset:
    :return: string, int
    """

    rise_mins = []
    set_mins = []

    for time in (rise):
        rise_mins.append(int(time[0])*60+int(time[1:]))
    for time in (sunset):
        set_mins.append(int(time[0:2])*60+int(time[2:]))

    rise[:] = rise_mins
    sunset[:] = set_mins
    days = sunset-rise
    hours = str(days[days.idxmax()] // 60) + str(days[days.idxmax()] - (days[days.idxmax()] // 60)*60)

    return days.idxmax(), hours


def sunrise_dif(rise, theday):
    """
    This function takes a series and Timestamp as the paramter, and return the sunrise difference between 90-days-before
     of theday and 90-days-after of theday.
    :param rise:
    :param theday:
    :return: int
    """
    rise_mins = []
    my_rise = rise.copy()
    for time in my_rise:
        mytime = str(time)
        mins = int(mytime[0]) * 60 + int(mytime[1:])
        rise_mins.append(mins)

    my_rise[:] = rise_mins

    day_90_before = my_rise[theday - timedelta(90)]
    day_90_after = my_rise[theday + timedelta(90)]
    return int(day_90_before) - int(day_90_after)


def main():
    DataFrame = read_frame()
    rise, sunset = get_series(DataFrame)
    longest_day(rise, sunset)
    sunrise_dif(pd.read_pickle('sunrise.pkl'), pd.Timestamp('2018-4-17 00:00:00', freq='D'));

if __name__ == "__main__":
    main()
