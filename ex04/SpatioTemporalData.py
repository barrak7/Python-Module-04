#!/bin/python

import pandas as pd
from FileLoader import FileLoader


class SpatioTemporalData:
    def __init__(self, df):
        self.df = df

    def when(self, location):
        try:
            return self.df[self.df['City'] == location]['Year'].unique().tolist()
        except:
            return

    def where(self, year):
        try:
            return self.df[self.df['Year'] == year]['City'].unique().tolist()
        except:
            return


loader = FileLoader()
data = loader.load('../athlete_events.csv')
sp = SpatioTemporalData(data)
print(sp.where(1896))
# Output
['Athina']
print(sp.where(2016))
# Output
['Rio de Janeiro']
print(sp.when('Athina'))
# Output
[2004, 1906, 1896]
print(sp.when('Paris'))
# Output
[1900, 1924]
