import pandas as pd

"""
writing this exploratory data analysis
file with support of single CSV. 
Will improve this in the next version of the module.
"""


class EDA:
    def __int__(self, file=None, delimiter=' '):
        if file:
            self.df = pd.read_csv(file, delimiter=delimiter)

    def shape(self):
        return self.df.shape

    def head(self, num=5):
        return self.df.head(num)

    def getTypes(self):
        return self.df.info()

    def describe(self):
        return self.df.describe()

    def __str__(self):
        print("Dataset Infomatics:")
        print("Shape:")
        print("{0} Rows x {1} Columns".format(self.df.shape[0], self.df.shape[1]))
