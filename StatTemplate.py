from _local_data import *


class StatTemplate:
    def __init__(self, statRate):
        self.checkweights(*statRate)
        self.statRate = self.mkstatdict(statRate, stats)

    def mkstatdict(self, rate, names):
        if len(rate) != len(names):
            raise IndexError("Size of rate and names arrays must be equal.")

        res = dict()
        for i in range(len(rate)):
            res[names[i]] = rate[i]
        return res

    def checkweights(self, *args):
        if sum(args) != 100:
                print(args)
                raise TypeError("Weights must sum up to 100.")
