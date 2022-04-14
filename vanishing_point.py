### Author: Christopher Reid
### Course: CSC 110
### Description: This program displays a canvas with a dynamic landscape. The user can control the
#               distance at which the landscape can be viewed based on the y-axis positioning of the
#               mouse cursor within the canvas, simulating a 'vanishing point' illusion.

from graphics_110 import graphics
import random

def background():
    """
    This function outputs a clear blue rectangle on the canvas to simulate the sky. An ellipse is
    displayed to simulate the sun. As the mouse cursor y-value increases (moving the mouse downward)
    , so too do the x and y coordinates of the sun ellipse, moving it toward the bottom right corner
     of the canvas.
    """
    sky_color = gui.get_color_string(208, 243, 247)
    sun_color = gui.get_color_string(255, 255, 39)

    # Blue Sky Background
    gui.clear()
    gui.rectangle(0, 0, 700, 500, sky_color)

    # Sun
    gui.ellipse(350+gui.mouse_y, (gui.mouse_y*0.9), 100+gui.mouse_y*0.5, 100+gui.mouse_y*0.5,
                sun_color)

def image():
    """
    Except for the 'sun' this function controls the movement behaviors of the following image
    objects: Mountain, Pond, Tree Top & Bottom, Grass on image 'horizon'.

    A triangle is used to simulate the mountain and a green rectangle 'in front' to
    simulate an open field. Only the top of the mountain (second y-coordinate) alters the shape of
    the mountain. As the mouse cursor y-value increases (moving the mouse downward), the second
    y-coordinate of the triangle decreases. The field rectangle's y-value is positioned to form a
    horizon at y = 333.

    The pond is displayed by an ellipse with its y-coordinate, width and height increasing at
    different rates as the mouse cursor y-value increases (moving the mouse downward).

    The tall grass is displayed with a rectangle function within a while loop. As the mouse cursor
    y-value increases (moving the mouse downward), the height of each rectangle is decreasing AWAY
    from the horizon at y = 333 towards y = 0. The loop displays a 'grass' rectangle at the
    x-coordinate as determined by the index and the index increases by 5 every iteration until
    the grass stretches across the canvas.

    The tree leaves (ellipses) are moving closer to their side respective top corners as the mouse
    cursor y-value increases (moving the mouse downward). The tree bottoms (rectangles) are moving
    closer to their side respective bottom corners as the mouse cursor y-value increases
    (moving the mouse downward)

    All these functions collectively simulate the 'vanishing point illusion'.
    """
    field_color = gui.get_color_string(38, 227, 0)
    mountain_color = gui.get_color_string(158, 87, 62)
    trunk_color = gui.get_color_string(158, 87, 62)
    leaves_color = gui.get_color_string(17, 64, 3)

    # Mountain
    gui.triangle(0, 500, 350, 275-(gui.mouse_y*1.5), 700, 500, mountain_color)
    # Open Field
    gui.rectangle(0, 333, 700, 333, field_color)
    # Pond
    gui.ellipse(350, 333 + (gui.mouse_y*0.2), gui.mouse_y, gui.mouse_y*0.2, 'blue')

    # Grass Blades
    grass_x_coord = 0
    while grass_x_coord < 700:
        gui.rectangle(grass_x_coord, 333, 3, (-gui.mouse_y * 0.1), leaves_color)
        grass_x_coord += 5

    # Trees - Left/Right
    gui.rectangle(350-gui.mouse_y, 333+(gui.mouse_y * 0.15), -gui.mouse_y*0.3, gui.mouse_y*0.5,
                  trunk_color)
    gui.ellipse(350-(gui.mouse_y*1.15), 333-(gui.mouse_y * 0.30), -gui.mouse_y, gui.mouse_y*1.15,
                leaves_color)
    gui.rectangle(350+gui.mouse_y, 333+(gui.mouse_y*0.15), gui.mouse_y*0.3, gui.mouse_y*0.5,
                  trunk_color)
    gui.ellipse(350+(gui.mouse_y*1.15), 333-(gui.mouse_y*0.30), gui.mouse_y, gui.mouse_y*1.15,
                leaves_color)

def random_clouds(cloud_x, cloud_y):
    """
    This function displays 3 pairs of ellipses as clouds. An x and y coordinate pair are accepted as
    parameters. Each time the program is run, the the main() function generates 3 random x and y
    coordinate pairs which are passed to this function as the clouds' display locations. The
    'Child Cloud' is the second cloud of each cloud pair. It's coordinates will be slightly modified
    depending on the calculated coordinates of the 'Parent Cloud'.
    """
    cloud_color = gui.get_color_string(255, 255, 255)

    # 'Parent' Cloud
    gui.ellipse(cloud_x, cloud_y, 100, 75, cloud_color)
    # 'Child' Cloud based off Parent Cloud coordinates
    gui.ellipse(cloud_x + 45, cloud_y + 30, 100, 65, cloud_color)

def main():
    """
    This function establishes gui as a global variable so it may be referenced in all subsequent
    functions. First a 700 x 500 canvas is generated and 3 pairs of random integers between the
    canvas dimensions are generated  as x and y coordinates for the clouds. These are later passed
    as arguments to the random_clouds() function thrice to generate 3 cloud pairs in random
    locations each time the entire program is run.

    Each function displays a different element of the image: the background and moving objects.

    As the program heavily depends on the current location of the mouse cursor, the active x and y
    coordinates of the mouse cursor on the canvas are displayed in the top left corner, refreshing
    with each frame update.
    """
    global gui
    gui = graphics(700, 500, 'vanishing point')

    # First Cloud Random Coordinates
    cloud_one_x = random.randint(0, 180)
    cloud_one_y = random.randint(0, 225)
    # Second Cloud Random Coordinates
    cloud_two_x = random.randint(225, 440)
    cloud_two_y = random.randint(0, 200)
    # Third Cloud Random Coordinates
    cloud_three_x = random.randint(532, 700)
    cloud_three_y = random.randint(0, 225)

    while True:
        gui.clear()
        background()
        random_clouds(cloud_one_x, cloud_one_y)
        random_clouds(cloud_two_x, cloud_two_y)
        random_clouds(cloud_three_x, cloud_three_y)
        image()
        gui.text(0, 0, ('X = ' + str(gui.mouse_x)), 'black', 40)
        gui.text(0, 40, ('Y = ' + str(gui.mouse_y)), 'black', 40)
        gui.update_frame(60)

main()