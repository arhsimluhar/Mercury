import seaborn as sn


class Draw(object):
    def __int__(self, df=None):
        if df:
            self.df = df

    def heatmap(self):
        return sn.heatmap(self.df, annot=True)
