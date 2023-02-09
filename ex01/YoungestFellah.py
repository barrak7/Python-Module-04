#!/bin/python3

from FileLoader import FileLoader
import pandas as pd


def youngest_fellah(df, year):
    try:
        young = {'man': None, 'woman': None}
        new_df = df.loc[df['Year'] == year]
        young['man'] = (new_df.loc[df['Sex'] == 'M'])['Age'].min()
        young['woman'] = (new_df.loc[df['Sex'] == 'F'])['Age'].min()
        return young
    except:
        return


loader = FileLoader()
data = loader.load("../athlete_events.csv")

print(youngest_fellah(data, 2004))
