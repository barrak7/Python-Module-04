#!/bin/python3

import pandas as pd
from FileLoader import FileLoader
from HowManyMedals import how_many_medals


def how_many_medals_by_country(df, country):
    try:
        medals = {}
        new_df = df[df['Team'] == country]
        new_df = new_df.groupby('Name')
        for i, athlete in new_df:
            medals_p = how_many_medals(athlete, i)
            for key in medals_p:
                if key not in medals:
                    medals[key] = medals_p[key]
                else:
                    for medal in medals_p[key]:
                        medals[key][medal] += medals_p[key][medal]
        return medals
    except:
        return


loader = FileLoader()
data = loader.load("../athlete_events.csv")

print(how_many_medals_by_country(data, "China"))
