"""
File: carcassonne_tile.py
Author: Christopher Reid
CSC 120 Spring 2022
Purpose: One of two sibling files that together simulate the game,
         Carcassonne. This program creates and stores information about
         various tile objects to be used in the game.
"""

class CarcassonneTile:
    """ Represents a tile in the Carcassonne board game. The tile can contain
    any combination of cities (connected or detached), grass or roads (can
    form a crossroad or lead to another edge).

    The constructor builds tiles using the 5 parameters passed in as arguments.
    Each argument represents a particular features and the numbers contained
    identify the edge with that feature. See Tile Side Encoding key below.

    Tile Side Encoding:
        -1 = Center
        0 = North
        1 = East
        2 = South
        3 = West
        None = Feature exists nowhere within the tile
    """

    def __init__(self, directions, city, city_connections, grass, road,
                 crossroads):
        """
        Parameters:
            directions: dict{maps integers to their respective tile side}
            city: list[edges with a city]
            city_connections: list[edges with connecting cities]
            grass: list[edges with grass]
            road: list[edges with a road]
            crossroads: dictionary{edge with crossroad: where it leads}
        """
        self._direct = None
        self._city = None
        self._connecting_cities = None
        self._grass = None
        self._road = None
        self._crossroads = None

        self.set_directions(directions)
        self.set_city(city)
        self.set_city_connections(city_connections)
        self.set_grass(grass)
        self.set_road(road)
        self.set_crossroads(crossroads)

    def set_directions(self, directions):
        """ Sets the self._direct field. """
        self._direct = directions

    def set_city(self, city):
        """ Sets the self._city field. """
        if city is not None:
            self._city = city

    def set_city_connections(self, connections):
        """ Sets the self._connecting_cities field. """
        if connections is not None:
            self._connecting_cities = connections

    def set_grass(self, grass):
        """ Sets the self._grass field. """
        if grass is not None:
            self._grass = grass

    def set_road(self, road):
        """ Sets the self._road field. """
        if road is not None:
            self._road = road

    def set_crossroads(self, crossroads):
        """ Sets the self._cross roads field. """
        if crossroads is not None:
            self._crossroads = crossroads

    def get_edge(self, side):
        """ Returns a string which indicates what is featured on that side
        of the tile. """
        ret = ''
        for key, val in self._direct.items():
            if side == key:
                if self._city is not None:
                    if key in self._city:
                        ret = 'city'
                if self._grass is not None:
                    if key in self._grass:
                        if self._road is not None:
                            if key in self._road:
                                ret = 'grass+road'
                            elif key not in self._road:
                                ret = 'grass'
                        else:
                            ret = 'grass'
                return ret

    def edge_has_road(self, side):
        """ Returns a bool value based on whether that edge has a road. """
        if self._road is not None:
            for key, val in self._direct.items():
                if side == key:
                    if key in self._road:
                        return True
        return False

    def edge_has_city(self, side):
        """ Returns a bool value based on whether that edge has a city."""
        if self._city is not None:
            for key, val in self._direct.items():
                if side == key:
                    if key in self._city:
                        return True
        return False

    def has_crossroads(self):
        """ Returns a bool value based on whether tha tile has a crossroad
        through the middle. """
        if self._crossroads is not None:
            if -1 in self._crossroads.values():
                return True
        return False

    def city_connects(self, side_1, side_2):
        """ Returns a bool value based on whether the two sides are both
        cities AND connected. """
        if side_1 == side_2:
            return True
        else:
            if self._connecting_cities is not None:
                for key, val in self._direct.items():
                    if side_2 == key:
                        if key in self._connecting_cities:
                            return True
        return False

    def road_get_connection(self, from_side):
        """ Returns the side that the provided road is connected to. """
        if self._crossroads is not None:
            for key, val in self._direct.items():
                if from_side == key:
                    for start, destination in self._crossroads.items():
                        if key == start:
                            return destination

    def rotate(self):
        """ Modifies fields from the constructor to simulate 'rotation' by
        adding 1 to any integer values with an upper limit of 3. Once all
        values of the rotated tile are extracted, a new tile is created and
        returned. """
        temp_n = self._direct[0]
        temp_e = self._direct[1]
        temp_s = self._direct[2]
        temp_w = self._direct[3]

        new_edges = {-1: 'Center', 0: temp_w, 1: temp_n, 2: temp_e, 3: temp_s}
        attributes = [self._city, self._connecting_cities, self._grass,
                      self._road]

        rotated = []
        for field in attributes:
            if field is None:
                rotated.append(field)
            else:
                new = []
                for val in field:
                    new.append((val + 1) % 4)
                rotated.append(new)

        if self._crossroads is not None:
            new_crossroads = {}
            for key, out_val in self._crossroads.items():
                if out_val == -1:
                    new_crossroads[(key + 1) % 4] = out_val
                else:
                    new_crossroads[(key + 1) % 4] = (out_val + 1) % 4
            rotated.append(new_crossroads)
        else:
            rotated.append(None)
        return CarcassonneTile(new_edges, rotated[0], rotated[1], rotated[2],
                               rotated[3], rotated[4])


#  NEW TILE TEMPLATE
#  tile## = CarcassonneTile(edges, None, None, None, None, None)

edges = {-1: 'Center', 0: "N", 1: 'E', 2: 'S', 3: 'W'}
tile01 = CarcassonneTile(edges, [0], None, [1, 2, 3], [1, 3], {1: 3, 3: 1})
tile02 = CarcassonneTile(edges, [0, 1, 3], [0, 1, 3], [2], None, None)
tile03 = CarcassonneTile(edges, None, None, [0, 1, 2, 3], [0, 1, 2, 3],
                         {0: -1, 1: -1, 2: -1, 3: -1})
tile04 = CarcassonneTile(edges, [0], None, [1, 2, 3], [1, 2], {1: 2, 2: 1})
tile05 = CarcassonneTile(edges, [0, 1, 2, 3], [0, 1, 2, 3], None, None, None)
tile06 = CarcassonneTile(edges, None, None, [0, 1, 2, 3], [0, 2], {0: 2, 2: 0})
tile07 = CarcassonneTile(edges, [1, 3], None, [0, 2], None, None)
tile08 = CarcassonneTile(edges, [1, 3], [1, 3], [0, 2], None, None)
tile09 = CarcassonneTile(edges, [0, 1], [0, 1], [2, 3], None, None)
tile10 = CarcassonneTile(edges, None, None, [0, 1, 2, 3], [1, 2, 3],
                         {1: -1, 2: -1, 3: -1})
tile11 = CarcassonneTile(edges, [0, 3], [0, 3], [1, 2], [1, 2], {1: 2, 2: 1})
tile12 = CarcassonneTile(edges, [0], None, [1, 2, 3], [2, 3], {2: 3, 3: 2})
