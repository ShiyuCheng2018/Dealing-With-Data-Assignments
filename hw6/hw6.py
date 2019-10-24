from datetime import timedelta
import pandas as pd

def csv_to_dataframe(csv):
    data = pd.read_csv(csv,thousands='.', decimal=',', index_col=[0])
    return data


def format_df():
    pass


def growth_rate():
    pass


def years_to_extinction():
    pass


def dying_countries():
    pass


def main():
    csv = "/Users/shiyucheng/MyProjects/ISTA131/Homework/Python_Review/hw6/countries_of_the_world.csv"
    print(csv_to_dataframe())


if __name__ == "__main__":
    main()
