


class AbilitiesDict:
    def __init__(self):
        self.abilities = self.generateemptydict()

    def generateemptydict(self):
        res = dict()
        for name in abilities:
            res[name] = dict()
        return res