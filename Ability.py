class Ability:
    def __init__(self):
        self.name = str()
        self.descr = str()
        self.range = int()
        self.radius = int()
        self.dmgtype = str()

    def display(self):
        print('Ability name: ' + self.name)
        print('Description: ' + self.descr)
        print('Range: ' + str(self.range))
        print('Radius: ' + str(self.radius))
        print('Type of damage: ' + self.dmgtype)