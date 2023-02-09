#!/bin/python3

import pandas as pd


def how_many_medals(df, name):
    try:
        new_df = df[df['Name'] == name]
        medals = {}
        years = new_df.groupby('Year')
        for year, values in years:
            medals[year] = {'G': 0, 'S': 0, 'B': 0}
            count = values['Medal'].value_counts().to_dict()
            for key in count:
                if key[0] in medals[year]:
                    medals[year][key[0]] = count[key]

        return medals
    except:
        return
