
#map.py

import random

from metadata import *
from engine import *


class Map:
    terrain={}
    width=0
    height=0
    @classmethod
    def getMap(cls): return cls.terrain
    @classmethod
    def getTerrain(cls, _hex): return cls.terrain[_hex]
    @classmethod
    def terrainCost(cls, hexf, hext):
        terrain1 = cls.getTerrain(hexf)
        terrain2 = cls.getTerrain(hext)
        cost = 0
        if terrain1 == TER_GRASS:
            cost = 1
        elif terrain1 == TER_SAND:
            cost = 2
        elif terrain1 == TER_SNOW:
            cost = 2
        elif terrain1 == TER_ROCK:
            cost = 1
        elif terrain1 == TER_TAR:
            cost = 5
        return cost
    @classmethod
    def create(cls, width, height):
        cls.width = width
        cls.height = height
        for j in range(cls.width):
            for i in range(cls.height):
                cls.terrain[Hex(j, i)] = TER_GRASS
                if random.random()*100 < 40:
                    cls.terrain[Hex(j, i)] = TER_TAR
