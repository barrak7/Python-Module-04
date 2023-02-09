#!/bin/python3

import numpy as np
import pandas as pd
from MyPlotLib import MyPlotLib as mpl
from FileLoader import FileLoader

class Komparator:
    def __init__(self, df):
        self.df = df

    def compare_box_plots(self, categorical_var, numerical_var):
        try:
            groups = self.df.groupby(categorical_var)
            new_df = pd.DataFrame()
            features = []
            for group, data in groups:
                features.append(group)
                data = data.rename(columns={numerical_var:group})
                data = pd.DataFrame(data[group])
                new_df = pd.concat([new_df, data])
            mpl.box_plot(new_df, features)
        except:
            return

    def density(self, categorical_var, numerical_var):
        try:
            groups = self.df.groupby(categorical_var)
            new_df = pd.DataFrame()
            features = []
            for group, data in groups:
                features.append(group)
                data = data.rename(columns={numerical_var:group})
                data = pd.DataFrame(data[group])
                new_df = pd.concat([new_df, data])
            mpl.density(new_df, features)
        except:
            return

    def compare_histograms(self, categorical_var, numerical_var):
        try:
            groups = self.df.groupby(categorical_var)
            new_df = pd.DataFrame()
            features = []
            for group, data in groups:
                features.append(group)
                data = data.rename(columns={numerical_var:group})
                data = pd.DataFrame(data[group])
                new_df = pd.concat([new_df, data])
            mpl.histogram(new_df, features)
        except:
            return

