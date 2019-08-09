import pandas as pd

"""
writing this exploratory data analysis
file with support of single CSV. 
Will improve this in the next version of the module.
"""


class EDA:
    def __init__(self, file=None, delimiter=",", target=None, predictor=None):

        self.is_target_predictor_set = True
        self.discrete_variables = []
        self.continuous_variables = []
        self.feature_types = {}
        if file:
            self.df = pd.read_csv(file, delimiter=delimiter)
            self.target = target
            self.predictor = predictor

        self.set_target_predictor()
        self.feature_types = self.set_data_type()
        self.discrete_variables, self.continuous_variables = self.set_type_of_variable()

    def set_target_predictor(self):

        if self.target and self.predictor:
            return
        elif self.target:
            self.predictor = [item for item in self.df.columns if item != self.target]
        elif self.predictor:
            self.predictor = [item for item in self.df.columns if item != self.predictor]
        else:
            self.is_target_predictor_set = False
            return

    def shape(self):
        return self.df.shape

    def head(self, num=5):
        return self.df.head(num)

    def get_types(self):
        return self.df.info()

    def describe(self):
        return self.df.describe()

    def variable_category(self):
        """
        returns the dictionary that
        lists predictor and target variables
        :return dict:
        """
        if self.is_target_predictor_set:
            data = {"Predictor Variable": self.predictor, "Target Variable": self.target}
        else:
            data = {"info": "Predictor and  Target variables have not be set yet."}
        return data

    def set_data_type(self):
        data = {}
        for column in self.df.columns:
            if self.df.dtypes[column] == 'int64':
                data[column] = 'Integer'
            elif self.df.dtypes[column] == "bool":
                data[column] = 'Boolean'
            elif self.df.dtypes[column] == "float64":
                data[column] = "Floating Point"
            elif self.df.dtypes[column] == "object":
                data[column] = "String"
            else:
                raise Exception("Unhandled Data Type.")
        return data

    def set_type_of_variable(self):
        """
        identifies whether the feature is
        continuous or discrete variable.
        :return dict:
        TOD0: Improve the algorithm
        """
        data = {"categorial": [], "continuous": []}
        total_length = self.shape()[0]
        for column in self.df.columns:
            if self.feature_types[column] == "String":
                data["categorial"].append(column)
                continue

            unique_entries = len(self.df[column].unique())
            print(unique_entries, column, total_length)
            if unique_entries <= 0.05 * total_length:
                if total_length >= 10 ** 6:
                    data["continuous"].append(column)
                else:
                    data["categorial"].append(column)
            else:
                data["continuous"].append(column)
        return data["categorial"], data["continuous"]

    def informatics(self):
        print("Dataset Informatics:")
        print("Shape: ", end="")
        print("{0} Datapoints x {1} features".format(self.df.shape[0], self.df.shape[1]))
        print("****************************")


class UnivariateAnalysis(EDA):
    def __init__(self):
        super().__init__()

    def central_tendency(self):
        pass

    def continuous_variables(self):
        for column in self.df.columns:
            pass



class BivariateAnalysis(EDA):
    def __init__(self):
        super().__init__()


class MissingData(EDA):
    def __init__(self):
        super().__init__()


class Outliers(UnivariateAnalysis, BivariateAnalysis):
    def __init__(self):
        super().__init__()

# t = EDA(file="test.csv")
# print (t.continuous_variables)
# print(t.discrete_variables)
# print(t.df['Age'].describe())
#
# import sys
#
# sys.path.append("../visual")
# from visual import Draw
#
# d = Draw(t.df)
#
# x = d.missing_data_visualisation()
#
# # Save the full figure...
# plt.savefig('full_figure.png')
