#!/bin/python3

import pandas as pd
from FileLoader import FileLoader


def proportion_by_sport(df, year, sport, gender):
    try:
        new_df = df.loc[df['Year'] == year].loc[df['Sex'] == gender]
        return new_df.loc[new_df['Sport'] == sport]['ID'].unique().shape[0] / new_df['ID'].unique().shape[0]
    except:
        return


loader = FileLoader()
data = loader.load("../athlete_events.csv")
print(proportion_by_sport(data, 2004, 'Tennis', 'F'))
