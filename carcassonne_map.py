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
                    checks = 0
                    for check in adjacent:
                        for key, direc in check.items():
                            if key not in self._map.keys():
                                checks += 1
                            elif key in self._map.keys():
                                edge1 = tile.get_edge(direc[0])
                                edge2 = self._map.get(key).get_edge(direc[1])
                                if edge1 == edge2:
                                    checks += 1
                    if checks < 4:
                        return False
                    else:
                        if tryOnly:
                            return True
                        else:
                            self._map[coord] = tile
                            return True
            return False

    def trace_road_one_direction(self, x, y, side):
        traveled = []
        start = (x, y)
        leaving = side
        no_repeats = set()
        while leaving != -1:
            break_flag = False
            north = {(start[0], start[1] + 1): (0, 2)}
            east = {(start[0] + 1, start[1]): (1, 3)}
            south = {(start[0], start[1] - 1): (2, 0)}
            west = {(start[0] - 1, start[1]): (3, 1)}
            adjacent = [north, east, south, west]
            checks = 0
            for check in adjacent:
                for coord, route in check.items():
                    if coord in self._map.keys() and route[0] == leaving:
                        if coord not in no_repeats:
                            ending = self._map.get(coord).road_get_connection\
                                (route[1])
                            traced = coord[0], coord[1], route[1], ending
                            traveled.append(traced)
                            no_repeats.add(coord)
                            start = coord
                            leaving = traced[-1]
                            break_flag = True
                            break
                        else:
                            return traveled
                if break_flag:
                    break
                else:
                    checks += 1
                if checks == 4:
                    return traveled
        return traveled