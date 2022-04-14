"""
File: carcassonne_tile_scratched.py
Author: Christopher Reid
CSC 120 Spring 2022
Purpose: This is Part 1 of a 4 part Carcassonne Tile Game simulation program.
         This program creates and stores information about various tile
         objects to be used in the game.
"""


class CarcassonneTile:
    def __init__(self, city, grass, road, crossroads):
        self._direct = {0: 'N', 1: 'E', 2: 'S', 3: 'W'}

        self._city = None
        self._grass = None
        self._road = None
        self._crossroads = None

        self.set_city(city)
        self.set_grass(grass)
        self.set_road(road)
        self.set_crossroads(crossroads)

    def set_city(self, city):
        if city is not None:
            side_with_cities = []
            for num in city:
                if num in self._direct:
                    side_with_cities.append(self._direct.get(num))
            self._city = side_with_cities

    def set_grass(self, grass):
        if grass is not None:
            side_with_grass = []
            for num in grass:
                if num in self._direct:
                    side_with_grass.append(self._direct.get(num))
            self._grass = side_with_grass

    def set_road(self, road):
        if road is not None:
            side_with_road = []
            for num in road:
                if num in self._direct:
                    side_with_road.append(self._direct.get(num))
            self._road = side_with_road

    def set_crossroads(self, crossroads):
        if crossroads is not None:
            self._crossroads = crossroads

    def get_edge(self, side):
        info = ''
        if self._city is not None:
            if self._direct.get(side) in self._city:
                info = 'city'
        if self._direct.get(side) in self._grass:
            if self._direct.get(side) in self._road:
                info = 'grass+road'
            elif self._direct.get(side) not in self._road:
                info = 'grass'
        return info

    def edge_has_road(self, side):
        if self._road is None:
            return False
        if self._direct.get(side) in self._road:
            return True
        return False

    def edge_has_city(self, side):
        if self._city is None:
            return False
        elif self._direct.get(side) in self._city:
            return True
        return False

    def has_crossroads(self):
        if self._crossroads is not None:
            if -1 in self._crossroads.values():
                return True
        return False

    def city_connects(self, side_1, side_2):
        if self._direct.get(side_2) in self._city:
            if side_1 == side_2:
                return True
            else:
                if side_1 == 0 and side_2 == 1 or 3:
                    return True
                elif side_1 == 1 and side_2 == 0 or 2:
                    return True
                elif side_1 == 2 and side_2 == 3 or 1:
                    return True
                elif side_1 == 3 and side_2 == 2 or 0:
                    return True
        return False

    def road_get_connection(self, from_side):
        if self._crossroads is not None:
            if from_side in self._crossroads:
                return self._crossroads.get(from_side)

# ___CarcassonneTile Input Key_______________
# Argument Format = (city, grass, road, crossroads)
# city = list of ints
# grass = list of ints
# road = list of ints
# crossroad = dict (Connections and Inverse Connections)

# ___Location Encoding_______________
# 0 - North
# 1 - East
# 2 - South
# 3 - West


tile01 = CarcassonneTile([0], [1, 2, 3], [1, 3], {1: 3, 3: 1})

tile02 = CarcassonneTile([0, 1, 3], [2], [], None)

tile03 = CarcassonneTile(None, [0, 1, 2, 3], [0, 1, 2, 3],
                         {0: -1, 1: -1, 2: -1, 3: -1})

tile04 = CarcassonneTile([0], [1, 2, 3], [1, 2], {1: 2, 2: 1})
