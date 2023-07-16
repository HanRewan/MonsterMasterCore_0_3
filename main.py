from Creature import *

if __name__ == '__main__':
    dragonTmpl = CreatureTemplate([33, 34, 33], [1, 1, 1, 1, 1, 95])
    dragon = Creature(90, dragonTmpl)
    dragon.display()