"""
File: classes_prob1.py
Author: Christopher Reid
CSC 120 Spring 2022
Purpose: Long Project #5, This program defines three classes. Upon creation,
the data fields can be further modified.
"""

class Simplest:
    """ This class stores 3 given arguments into internal fields. """
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

class Rotate:
    """ This class stores 3 arguments within internal fields, rotating the
    values with every call of the rotate() method.
    """
    def __init__(self, first, second, third):
        """ Constructs the objects being modified. Caller must pass in three
        values. """
        self._first = first
        self._second = second
        self._third = third

    def get_first(self):
        """ Returns the current value of self._first. """
        return self._first

    def get_second(self):
        """ Returns the current value of self._second. """
        return self._second

    def get_third(self):
        """ Returns the current value of self._third. """
        return self._third

    def rotate(self):
        """ Swaps values of all three fields when called. """
        temp1 = self._first
        temp2 = self._second
        self._first = temp2
        self._second = self._third
        self._third = temp1

class Band:
    """ This class models the structure of a traditional music group
    consisting of a singer, a drummer and guitar players. As the number of
    guitar players can vary, they will be stored in an array. """
    def __init__(self, singer):
        self._singer = singer
        self._drummer = None
        self._guitars = []

    def get_singer(self):
        """ Returns the current lead singer. """
        return self._singer

    def set_singer(self, new_singer):
        """ Changes the current lead singer. """
        self._singer = new_singer

    def get_drummer(self):
        """ Returns the current band's drummer. """
        return self._drummer

    def set_drummer(self, new_drummer):
        """ Changes the current band's drummer. """
        self._drummer = new_drummer

    def add_guitar_player(self, new_guitar_player):
        """ Adds a guitar player to the guitar player list. """
        self._guitars.append(new_guitar_player)

    def fire_all_guitar_players(self):
        """ Completely clears the list of guitar players. Guitar players
        cannot be fired individually. They must all be fired, all at once. """
        self._guitars.clear()

    def get_guitar_players(self):
        """ Returns a copy of the list of guitar players. """
        return self._guitars.copy()

    def play_music(self):
        """ Plays music based on the current band members. Known singers are
        listed and produced specific song lyrics. All other singers produce
        the same generic lyrics. """

        known = ['Frank Sinatra', 'Kurt Cobain']
        if self._singer == known[0]:
            print('Do be do be do')
        elif self._singer == known[1]:
            print('bargle nawdle zouss')
        else:
            print('La la la')

        if self._drummer is not None:
            print('Bang bang bang!')

        for player in self._guitars:
            print('Strum!')