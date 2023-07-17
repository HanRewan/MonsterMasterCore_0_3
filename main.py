from Creature import *

if __name__ == '__main__':
    dragonTmpl = CreatureTemplate([40, 40, 20], [16, 23, 16, 16, 13, 16])
    dragon = Creature(10, dragonTmpl)
    dragon.display()