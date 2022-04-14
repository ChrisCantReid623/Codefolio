"""
File: classes_prob2.py
Author: Christopher Reid
CSC 120 Spring 2022
Purpose: Long Project #5, This program gives information on RGB values. Three
values are given as arguments upon creation of an object.
"""

class Color:
    """ This class represents the RGB values of a color, stored in an
    internal list. """
    def __init__(self, r, g, b):
        """ The constructor accepts three values representing color RGY,
        checking if they are within the range of 0 to 255. Values outside
        that range are automatically rounded within bounds. """
        self._colors = [r, g, b]

        index = 0
        for rgb_val in self._colors:
            if rgb_val < 0:
                self._colors[index] = 0
            elif rgb_val > 255:
                self._colors[index] = 255
            index += 1

    def __str__(self):
        """ Returns a string containing a tuple of the provided RGB values. """
        return f'rgb{tuple(self._colors)}'.replace(' ', '')

    def html_hex_color(self):
        """ Returns a string encoding the RGB values as hexadecimal
        characters. """
        hex_red = f'{self._colors[0]:02X}'
        hex_green = f'{self._colors[1]:02X}'
        hex_blue = f'{self._colors[2]:02X}'

        return str(f'#{hex_red}{hex_green}{hex_blue}').replace(' ', '')

    def get_rgb(self):
        """ Returns a standard tuple of the RGB values. """
        return tuple(self._colors)

    def set_standard_color(self, name):
        """ Accept a color string as an argument, this method performs a
        case-sensitive check that matches one of four predefined colors.
        The list containing the RBG values is then modified to contain the
        values of that new color. """
        red_rgb = [255, 0, 0]
        yellow_rgb = [255, 255, 0]
        white_rgb = [255, 255, 255]
        black_rgb = [0, 0, 0]

        if name.lower() == 'red':
            self._colors = red_rgb
        elif name.lower() == 'yellow':
            self._colors = yellow_rgb
        elif name.lower() == 'white':
            self._colors = white_rgb
        elif name.lower() == 'black':
            self._colors = black_rgb

        return self._colors

    def remove_red(self):
        """ Sets the red RGB component to zero. """
        self._colors[0] = 0