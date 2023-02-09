#!/bin/python3

import pandas as pd
import matplotlib.pyplot as plt
from FileLoader import FileLoader
from pandas.api.types import is_numeric_dtype


class MyPlotLib:
    @staticmethod
    def fix_features(df, features):
        try:
            new_df = df.copy()
            for feature in features:
                if is_numeric_dtype(new_df[feature]):
                    new_df[feature] = new_df[feature].fillna(
                        new_df[feature].median())
                else:
                    new_df = new_df.drop(feature, axis=1)
            return new_df
        except:
            return

    @staticmethod
    def histogram(df, features):
        try:
            new_df = MyPlotLib.fix_features(df, features)
            new_df.hist()
            plt.show()
        except:
            return

    @staticmethod
    def density(df, features):
        try:
            new_df = MyPlotLib.fix_features(df, features)
            new_df.plot.density()
            plt.show()
        except:
            return

    @staticmethod
    def pair_plot(df, features):
        try:
            new_df = MyPlotLib.fix_features(df, features)
            pd.plotting.scatter_matrix(new_df)
            plt.show()
        except:
            return

    @staticmethod
    def box_plot(df, features):
        try:
            new_df = MyPlotLib.fix_features(df, features)
            new_df.boxplot()
            plt.show()
        except:
            return


