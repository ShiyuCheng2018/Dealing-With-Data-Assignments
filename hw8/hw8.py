# Shiyu Cheng 23329948
# Fri. 11:00-1:00 Hayley
# 11/27/2019
# hw8

import pandas as pd, matplotlib.pyplot as plt, datetime

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

def get_2019():
    '''
    This function reads the data from data_2019.csv, and return a Series
    :return: Series
    '''
    df = pd.read_csv("data_2019.csv", names=["date", "time"])
    df["time"].index = get_column_labels()[0: 290]
    y2019 = df["time"]
    return y2019


def extract_fig_1_frame(df):
    '''
    This function takes the DataFrame I created in hw5, and return DataFrame
    :param df: DataFrame
    :return: DataFrame
    '''
    two_s = 2*df.std()
    mean = df.mean()
    new = mean.to_frame(name="mean").join(two_s.to_frame(name="two_s"))
    return pd.DataFrame(new).transpose()


def extract_fig_2_frame(df):
    '''
    This function takes the DataFrame I created in hw7
    :param df: DataFrame
    :return: DataFrame
    '''
    mean_1980 = df.iloc[1:11, ].mean()
    mean_1990 = df.iloc[11:21,].mean()
    mean_2000 = df.iloc[21: 31].mean()
    mean_2010 = df.iloc[31:40,].mean()

    new = mean_1980.to_frame(name="1980s")\
        .join(mean_1990.to_frame(name="1990s"))\
        .join(mean_2000.to_frame(name="2000s"))\
        .join(mean_2010.to_frame(name="2010s"))
    return pd.DataFrame(new).transpose()

def make_fig_1(df_1):
    '''
    This function takes a figure 1 frame and hw5 frame, and creates a image
    :param df_1: DataFrame
    :return:
    '''
    df_2 = extract_fig_1_frame(df_1)
    plt.plot(df_2.loc["mean"], label="mean")
    plt.plot(df_1.loc[2012], linestyle="--", label="2012")
    plt.plot(get_2019(), label="2019")
    sd_1, = plt.plot(df_2.loc["mean"] + df_2.loc["two_s"], color="DarkGray")
    sd_2, = plt.plot(df_2.loc["mean"] - df_2.loc["two_s"], color="DarkGray")
    x = sd_1.get_xdata()
    y_1 = sd_1.get_ydata()
    y_2 = sd_2.get_ydata()
    plt.xticks(range(0, 365, 50))
    plt.fill_between(x, y_1, y_2, facecolor="DarkGray", label="$\pm2$ std devs")
    plt.margins(x=0)
    plt.legend(loc='upper right')
    plt.ylabel("NH Sea Ice Extent ($\mathregular{10^6}$ $\mathregular{km^2}$)")


def make_fig_2(df_1):
    '''
    This function takes a figure 2 frame, and creates a image
    :param df_1: DataFrame
    :return:
    '''
    df_2 = extract_fig_2_frame(df_1)
    plt.plot(df_2.loc["1980s"], linestyle="--", label="1980s")
    plt.plot(df_2.loc["1990s"], linestyle="--", label="1990s")
    plt.plot(df_2.loc["2000s"], linestyle="--", label="2000s")
    plt.plot(df_2.loc["2010s"], linestyle="--", label="2010s")
    plt.plot(get_2019(), label="2019")
    plt.xticks(range(0, 365, 50))
    plt.margins(x=0)
    plt.legend()
    plt.ylabel("NH Sea Ice Extent ($\mathregular{10^6}$ $\mathregular{km^2}$)")


def main():
    """
    a series steps to make csv files.
    :return:
    """
    df = pd.read_csv("data_79_18.csv", index_col=0)
    plt.figure()
    make_fig_1(df)
    plt.figure()
    make_fig_2(df)
    plt.show()

if __name__ == "__main__":
    main()


