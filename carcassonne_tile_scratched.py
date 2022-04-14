"""
File: carcassonne_tile_scratched.py
Author: Christopher Reid
CSC 120 Spring 2022
Purpose: REPLACE_ME
"""

class CarcassonneTile:
    def __init__(self, tile_type):
        self._north_side = TileSide()
        self._east_side = TileSide()
        self._south_side = TileSide()
        self._west_side = TileSide()
        self.set_attributes(tile_type)

    def set_attributes(self, tile_type):
        tiles = {1: {'N': (True, False, False, False, False),
                     'E': (True, False, False, False, False),
                     'S': (False, False, False, True, False),
                     'W': (True, False, False, False, False)}
                        }
        directions = 'NESW'

        tile = {'N': self._north_side,
                'E': self._east_side,
                'S': self._south_side,
                'W': self._west_side}

        for each in directions:
            tile[each].set_attribute(tiles[tile_type][each])

class TileSide:
    def __init__(self):
        self.city = False
        self.road = False
        self.connects = False
        self.grass = False
        self.cross_road = False

    def set_attribute(self, params):
        city, road, connect, grass, cross_road = params
        self.city = city
        self.road = road
        self.connects = connect
        self.grass = grass
        self.cross_road = cross_road

    def get_attributes(self):
        pass
        


tile01 = CarcassonneTile(1)
print(tile01._north_side.city)

'''tile02 = CarcassonneTile(2)
tile03 = CarcassonneTile(3)
tile04 = CarcassonneTile(4)'''