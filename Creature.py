from _local_data import *
from AbilitiesDict import *
from Ability import *
from CreatureTemplate import *
from math import *


class Creature(AbilitiesDict):
    def __init__(self, dng: int, template: CreatureTemplate):
        super().__init__()
        self.cap = self.calculatecap(dng)
        self.stats = self.calculatestats(dng, template.statRate)
        self.generate_abilities_powers(dng, template.abilRate)

    def calculatestats(self, dng: int, statRate: dict):
        res = dict()
        for key, val in statRate.items():
            res[key] = 10 + random.randint(-2, 2) + val * dng / 500 * 19
        return res

    def display(self):
        for stat, value in self.stats.items():
            print(stat + ': ' + str(round(value)) + ' Mod: ' + str(round((value - 10) // 2)))
        for type, abls in self.abilities.items():
            print(type.upper())
            for abl in abls:
                abl.display()

    def calculatecap(self, dng: int):
        return max(1, round(sqrt(dng/4)*100))
    def get_max_cap(self, power):
        return power/2

    def _helper_generate_abilities_powers(self, key, total_power):
        while self.get_max_cap(total_power)>=self.cap:
            self.abilities[key].append(Ability(self.get_max_cap(total_power)))
            total_power -= self.get_max_cap(total_power)
        self.abilities[key].append(Ability(self.cap))
        return

    def generate_abilities_powers(self, dng, abilRate):
        for key in abilRate.keys():
            total_power = abilRate[key]*dng
            self._helper_generate_abilities_powers(key, total_power)
