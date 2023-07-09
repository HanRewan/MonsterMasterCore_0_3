from _local_data import *
from AbilitiesDict import *
from Ability import *
from CreatureTemplate import *

class Creature(AbilitiesDict):
    def __init__(self, dng: int, template: CreatureTemplate):
        super().__init__()
        self.stats = self.calculatestats(dng, template.statRate)

    def calculatestats(self, dng: int, statRate: dict):
        res = dict()
        for key, val in statRate.items():
            res[key] = 10 + random.randint(-2, 2) + val * dng / 500 * 19
        return res

    def display(self):
        for stat, value in self.stats.items():
            print(stat + ': ' + str(value) + ' Mod: ' + str((value-10)//2))
        for type, abls in self.abilities.items():
            print(type.upper())
            for name, abl in abls.items():
                abl.display()