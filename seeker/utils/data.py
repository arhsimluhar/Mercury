import random

import numpy as np


class Data(object):
    def __int__(self):
        pass

    def randRange(self, start, stop, size=1):
        return random.choice(range(start, stop), k=size)


class integer(Data):
    def __int__(self):
        pass

    def randInt(self, start, stop):
        return random.randint(start, stop)



class float(Data):
    def __int__(self):
        pass

    def randFloat(self, start, stop):
        return random.uniform(start, stop)

    def randRange(self, start, stop, step=1, size=1):
        return random.choice(np.linspace(start, stop, step), k=size)


class string(Data):
    def __int__(self):
        pass
