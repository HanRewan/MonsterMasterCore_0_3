from _local_data import *
from StatTemplate import *

class CreatureTemplate(StatTemplate):
    def __init__(self, abilRate, statRate):
        """
        :param abilRate: division of abilities by weights
            :subpart ATK: weight of attack power
            :subpart DEF: weight of defence power
            :subpart MOB: weight of mobility/stealth
        :param statRate: dict of stats weights (Basic DnD stats).
        remark: all weights Lists above must sum up to 100
        """
        super().__init__(statRate)
        self.checkweights(abilRate)
        self.abilRate = self.mkstatdict(abilRate, abilities)