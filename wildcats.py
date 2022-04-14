"""
File: wildcats.py
Author: Christopher Reid
CSC 120 Spring 2022
Purpose: This function displays squatting stick figures with text on a graphic
interface unit.
"""

import graphics_210

def school_banner(gui, count):
    """
    Displays custom text at various inteverals of time along the y-axis of
    the canvas.

    ---Parameters---

    gui: the image canvas

    count: iterator used to manipulate the movement animation
    """
    text_size = 140

    university_x = 90
    of_x = 300
    arizona_x = 90
    wildcats_x = 2
    wildcats_y = 450

    if count == 2:
        gui.text(university_x, 20, 'University!', 'red', text_size)
    elif count == 4:
        gui.text(of_x, 100, 'OF!', 'royal blue', text_size)
    elif count == 6:
        gui.text(arizona_x, 250, 'ARIZONA!', 'red', text_size)
    elif count == 8 or count == 9:
        gui.text(wildcats_x, wildcats_y, 'W', 'red', text_size)
        gui.text(wildcats_x + 125, wildcats_y, 'I', 'royal blue', text_size)
        gui.text(wildcats_x + 150, wildcats_y, 'L', 'red', text_size)
        gui.text(wildcats_x + 240, wildcats_y, 'D', 'royal blue', text_size)
        gui.text(wildcats_x + 340, wildcats_y, 'C', 'red', text_size)
        gui.text(wildcats_x + 450, wildcats_y, 'A', 'royal blue', text_size)
        gui.text(wildcats_x + 550, wildcats_y, 'T', 'red', text_size)
        gui.text(wildcats_x + 650, wildcats_y, 'S', 'royal blue', text_size)
        gui.text(wildcats_x + 750, wildcats_y, '!', 'red', text_size)

def upper_body(gui, center, torso_length, offset, neck, shoulder, count):
    """
    This function controls the upper bodies of the stick figures; the torso
    and anything north.

    ---Parameters---

    gui: the image canvas

    center: the x_coordinate of each stick figure's torso

    torso_length: the number of pixels along the y-axis the torso should cover

    offset: modifies the distance from the torso center to each respective
    foot

    neck: additional lineage along the y-axis, the 'stem' for the head of
    each figure

    shoulder: the northern limit of the torso

    count: iterator used to manipulate the movement animation
    """
    left_foot = center - offset
    right_foot = center + offset
    head_size = 75

    if count % 2 == 0 and count != 8:
        arm_length_down = torso_length * 0.8
        arm_down = shoulder + arm_length_down

        #  Arms
        gui.line(center, shoulder, left_foot, arm_down, 'black', 2)
        gui.line(center, shoulder, right_foot, arm_down, 'black', 2)
        #  Neck
        gui.line(center, shoulder, center, neck, 'black', 2)
        #  Head
        gui.ellipse(center, neck, head_size + 6, head_size + 6, 'black')
        gui.ellipse(center, neck, head_size, head_size, 'white')

    elif count == 8 or count == 9:
        arm_length_up = torso_length * 0.7
        arm_up = shoulder - arm_length_up

        #  Arms
        gui.line(center, shoulder, left_foot, arm_up, 'black', 2)
        gui.line(center, shoulder, right_foot, arm_up, 'black', 2)
        #  Neck
        gui.line(center, shoulder, center, neck, 'black', 2)
        #  Head
        gui.ellipse(center, neck, head_size + 6, head_size + 6, 'black')
        gui.ellipse(center, neck, head_size, head_size, 'white')

    else:
        bent_shoulder = shoulder + 50
        bent_neck = neck + 50
        arm_length_down = torso_length * 0.6
        arm_down = bent_shoulder + arm_length_down

        #  Arms
        gui.line(center, bent_shoulder, left_foot, arm_down, 'black', 2)
        gui.line(center, bent_shoulder, right_foot, arm_down, 'black', 2)
        #  Neck
        gui.line(center, bent_shoulder, center, bent_neck,
                 'black', 2)
        #  Head
        gui.ellipse(center, bent_neck, head_size + 6, head_size + 6,
                    'black')
        gui.ellipse(center, bent_neck, head_size, head_size, 'white')

def lower_body(gui, ground, count, offset, crotch, shoulder, center):
    """
    This function controls the stick figures' squatting animation.

    ---Parameters---

    gui: the image canvas

    ground: the most southward possible y-coordinate on the canvas

    count: iterator used to manipulate the movement animation

    offset: modifies the distance from the torso center to each respective
    foot

    crotch: the intersection of the leg segments, southbound limit of the
    torso

    shoulder: the northern limit of the torso

    center: the x_coordinate of each stick figure's torso
    """
    left_foot = center - offset
    right_foot = center + offset

    if count % 2 == 0 or count == 9:
    #  Straight Legs

        #  Feet to Crotch
        gui.line(left_foot, ground, center, crotch, 'black', 2)
        gui.line(right_foot, ground, center, crotch, 'black', 2)
        #  Torso
        gui.line(center, crotch, center, shoulder, 'black', 2)

    else:
    #  Bent Legs
        knees = ground - 75
        bent_crotch = knees - 50

        #  Feet to Knees
        gui.line(left_foot, ground, left_foot, knees, 'black', 2)
        gui.line(right_foot, ground, right_foot, knees, 'black', 2)
        #  Knees to Crotch
        gui.line(left_foot, knees, center, bent_crotch, 'black', 2)
        gui.line(right_foot, knees, center, bent_crotch, 'black', 2)
        #  Torso
        gui.line(center, bent_crotch, center, shoulder, 'black', 2)

def stick_men(gui, gui_width, ground, count):
    """
    This function generates the stick figures on the gui. The for loop
    modifies how many stick figures are displayed on the canvas. Each
    variable is used to create the different components of the stick figure
    when passed into functions.

    ---Parameters---

    gui: the image canvas

    gui_width: the width of the canvas

    ground: the most southern possible y-coordinate on the canvas,
    references the canvas's height variable

    count: iterator used to manipulate the movement animation
    """
    for i in range(1, 4):
        torso_center = i * (gui_width / 4)
        offset = 50

        torso_length = 180
        crotch = ground - 150

        torso = crotch - torso_length
        shoulder = torso + 25
        neck = torso - 25

        lower_body(gui, ground, count, offset, crotch, shoulder,
                   torso_center)
        upper_body(gui, torso_center, torso_length, offset, neck,
                   shoulder, count)

def main():
    gui_width = 800
    gui_floor = 800
    gui = graphics_210.graphics(gui_width, gui_floor, 'WILDCATS')

    while not gui.is_destroyed():
        count = 0
        gui.clear()
        while count != 10:
            #  Background
            gui.rectangle(0, 0, gui_width, gui_floor, 'silver')
            #  Builds Stick-Men
            stick_men(gui, gui_width, gui_floor, count)
            #  Builds School Banner
            school_banner(gui, count)
            
            count += 1
            if count == 10:
                count = 0

            gui.update_frame(4)

main()