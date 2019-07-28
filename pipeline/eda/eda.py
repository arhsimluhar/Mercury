import pandas as pd

"""
writing this exploratory data analysis
file with support of single CSV. 
Will improve this in the next version of the module.
"""


class EDA:
    def __init__(self, file=None, delimiter=",", predictor=None):
        if file:
            self.df = pd.read_csv(file, delimiter=delimiter)
        if predictor:
            self.predictorVal = predictor

    def shape(self):
        return self.df.shape

    def head(self, num=5):
        return self.df.head(num)

    def getTypes(self):
        return self.df.info()

    def describe(self):
        return self.df.describe()

    def variableCategory(self):
        pass

    def dataType(self):
        pass

    def typeOfVariable(self):
        pass

    def informatics(self):
        print("Dataset Infomatics:")
        print("Shape: ", end="")
        print("{0} Datapoints x {1} features".format(self.df.shape[0], self.df.shape[1]))
        print("****************************")


class univariateAnalysis(EDA):
    def __init__(self):
        super().__init__()


class bivariateAnalysis(EDA):
    def __init__(self):
        super().__init__()


class MissingData(EDA):
    def __init__(self):
        super().__init__()


class Outliers(univariateAnalysis, bivariateAnalysis):
    def __init__(self):
        super().__init__()
