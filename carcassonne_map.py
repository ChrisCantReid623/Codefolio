"""
File: carcassonne_map.py
Author: Christopher Reid
CSC 120 Spring 2022
Purpose: One of two sibling files that together simulate the game,
         Carcassonne. This program creates the 'map' game board. This program
         checks for specific parameters before tiles can be successfully
         placed on the board.
"""
import carcassonne_tile


class CarcassonneMap:
    """ Represents the map used in the Carcassonne board game. The board
    is represented using a dictionary where the coordinates of each
    successfully laid tile serve as the keys and the corresponding values
    are the tile objects themselves."""
    def __init__(self):
        """ The constructor initiates the map, placing tile01, at position
        (0,0)."""
        self._map = {(0, 0): carcassonne_tile.tile01}

    def get_all_coords(self):
        """ Returns all (x,y) coordinates of the current tiles in the map. """
        coords = set()
        for key in self._map:
            coords.add(key)
        return coords

    def find_map_border(self):
        """ Returns a set containing all (x,y) locations of the tile locations
        where a new tile may be placed based on current tiles."""
        border_tiles = set()
        for key in self._map:
            north = key[0], key[1] + 1
            if north not in self._map.keys():
                border_tiles.add(north)
            east = key[0] + 1, key[1]
            if east not in self._map.keys():
                border_tiles.add(east)
            south = key[0], key[1] - 1
            if south not in self._map.keys():
                border_tiles.add(south)
            west = key[0] - 1, key[1]
            if west not in self._map.keys():
                border_tiles.add(west)
        return border_tiles

    def get(self, x, y):
        """ Returns the tile at the specified (x,y) location."""
        coord = (x, y)
        if coord in self._map.keys():
            return self._map[coord]
        return None

    def add(self, x, y, tile, confirm=True, tryOnly=False):
        """ Performs a series of checks, before adding a given tile at the
        provided (x,y) location. The subject tile must share edge
        characteristics with all adjacent tiles to avoid rejection. """
        coord = (x, y)
        if not confirm and not tryOnly:
            self._map[coord] = tile
            return True
        else:
            if coord not in self._map:
                available = self.find_map_border()
                if coord in available:
                    north = {(coord[0], coord[1] + 1): (0, 2)}
                    east = {(coord[0] + 1, coord[1]): (1, 3)}
                    south = {(coord[0], coord[1] - 1): (2, 0)}
                    west = {(coord[0] - 1, coord[1]): (3, 1)}

                    adjacent = [north, east, south, west]

                    sides_passed = 0
                    for check in adjacent:
                        for key, direct in check.items():
                            if key not in self._map.keys():
                                sides_passed += 1
                            elif key in self._map.keys():
                                cur_edge = tile.get_edge(direct[0])
                                compared_edge = self._map.get(key). \
                                    get_edge(direct[1])
                                if cur_edge == compared_edge:
                                    sides_passed += 1
                    if sides_passed < 4:
                        return False
                    else:
                        if tryOnly:
                            return True
                        else:
                            self._map[coord] = tile
                            return True
            return False
