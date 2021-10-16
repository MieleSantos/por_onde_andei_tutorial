import pandas as pd


def load_data():
    return pd.read_csv("places.csv")


def save_data(df):
    df.to_csv("places.csv")
