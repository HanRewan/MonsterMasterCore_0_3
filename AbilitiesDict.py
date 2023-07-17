from _local_data import *


class AbilitiesDict:
    def __init__(self):
        self.abilities = self.generateemptydict()

    def generateemptydict(self):
        res = dict()
        for name in abilities:
            res[name] = list()
        return res