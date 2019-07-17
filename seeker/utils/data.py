import random


class Data(object):
    def __int__(self):
        pass

    def randRange(self, start, stop):
        pass


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


class string(Data):
    def __int__(self):
        pass
