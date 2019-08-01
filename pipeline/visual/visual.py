import missingno as msno
import seaborn as sn


class Draw:
    def __init__(self, df=None):
        if len(df):
            self.df = df

    def heatmap(self):
        return sn.heatmap(self.df, annot=True)

    def missing_data_visualisation(self):
        return msno.matrix(self.df)
