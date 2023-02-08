#!/bin/python3

import numpy as np
import pandas as pd


class FileLoader:
    def load(self, path):
        try:
            df = pd.read_csv(path)
            print("This data set is of dimensions ({} x {}).".format(
                df.shape[0], df.shape[1]))
            return df
        except:
            return

    def display(self, df, n):
        try:
            print(df.iloc[:n])
        except:
            return
