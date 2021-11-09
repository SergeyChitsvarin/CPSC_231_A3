# DO NOT EDIT THE FOLLOWING LINES
# COURSE CPSC 231 FALL 2021
# INSTRUCTOR: Jonathan Hudson
# Wi52C3g7ZzkJ7XBcVRHY
# DO NOT EDIT THE ABOVE LINES

# INFORMATION FOR YOUR TA

import sys
import os
import turtle
from math import *

# STARTER CONSTANTS
BACKGROUND_COLOR = "black"
WIDTH = 600
HEIGHT = 600

# AXIS CONSTANTS
AXIS_COLOR = "blue"
HALF_OF_TICK = 5
ZERO = 0
LABEL_FROM_AXIS = 27
MIN_Y = -1
MIN_X = -1
MAX_Y = 1
MAX_X = 1
X_ORIGIN = 300
Y_ORIGIN = 300
RATIO = 75
STEP_SIZE = 0.25

# STAR CONSTANTS
STAR_COLOR = "white"
STAR_COLOR2 = "grey"


def calc_to_screen_coord(x, y):
    """
    Convert a calculator (x,y) to a pixel (screen_x, screen_y) based on origin location and ratio
    :param x: Calculator x
    :param y: Calculator y
    :return: (screen_x, screen_y) pixel version of calculator (x,y)
    """
    # calculates screen x and screen y and returns those values
    screen_x = X_ORIGIN + (x * 4 * RATIO)
    screen_y = Y_ORIGIN + (y * 4 * RATIO)
    return screen_x, screen_y


def draw_line(pointer, screen_x1, screen_y1, screen_x2, screen_y2):
    """
    Draw a line between tow pixel coordinates (screen_x_1, screen_y_1) to (screen_x_2, screen_y_2)
    :param pointer: Turtle pointer to draw with
    :param screen_x1: The pixel x of line start
    :param screen_y1: The pixel y of line start
    :param screen_x2: The pixel x of line end
    :param screen_y2: The pixel y of line end
    :return: None (just draws in turtle)
    """
    # go to starting point
    pointer.penup()
    pointer.goto(screen_x1, screen_y1)
    # put pen down
    pointer.pendown()
    # go to line end point
    pointer.goto(screen_x2, screen_y2)
    pointer.penup()


def draw_x_axis_tick(pointer, screen_x, screen_y):
    """
    Draw an x-axis tick for location (screen_x, screen_y)
    :param pointer: Turtle pointer to draw with
    :param screen_x: The pixel x of tick location on axis
    :param screen_y: The pixel y of tick location on axis
    :return: None (just draws in turtle)
    """
    # defines start and end of tick
    screen_y1 = screen_y + HALF_OF_TICK
    screen_y2 = screen_y - HALF_OF_TICK
    # draws tick on x-axis
    draw_line(pointer, screen_x, screen_y1, screen_x, screen_y2)


def draw_x_axis_label(pointer, screen_x, screen_y, label_text):
    """
    Draw an x-axis label for location (screen_x, screen_y), label is label_text
    :param pointer: Turtle pointer to draw with
    :param screen_x: The pixel x of tick location on axis
    :param screen_y: The pixel y of tick location on axis
    :param label_text: The string label to draw
    :return: None (just draws in turtle)
    references:
    1)writing on screen in turtle https://stackoverflow.com/questions/15141031/python-turtle-draw-text-with-on-screen-with-larger-font
    2) align text to centre in turtle https://stackoverflow.com/questions/42265682/how-to-center-text-using-turtle-module-in-python
    """
    # this goes to specified x and y location and writes text below the x axis
    pointer.penup()
    pointer.goto(screen_x, screen_y-LABEL_FROM_AXIS)
    pointer.write(label_text, align="center")


def draw_y_axis_tick(pointer, screen_x, screen_y):
    """
    Draw an y-axis tick for location (screen_x, screen_y)
    :param pointer: Turtle pointer to draw with
    :param screen_x: The pixel x of tick location on axis
    :param screen_y: The pixel y of tick location on axis
    :return: None (just draws in turtle)
    """
    # defines start and end of tick
    screen_x1 = screen_x - HALF_OF_TICK
    screen_x2 = screen_x + HALF_OF_TICK
    # draws tick on y-axis
    draw_line(pointer, screen_x1, screen_y, screen_x2, screen_y)


def draw_y_axis_label(pointer, screen_x, screen_y, label_text):
    """
    Draw an y-axis label for location (screen_x, screen_y), label is label_text
    :param pointer: Turtle pointer to draw with
    :param screen_x: The pixel x of tick location on axis
    :param screen_y: The pixel y of tick location on axis
    :param label_text: The string label to draw
    :return: None (just draws in turtle)
    references:
    1)writing on screen in turtle https://stackoverflow.com/questions/15141031/python-turtle-draw-text-with-on-screen-with-larger-font
    """
    # this goes to specified x and y location and writes text on the left side of y axis.
    pointer.penup()
    pointer.goto(screen_x - LABEL_FROM_AXIS, screen_y)
    pointer.write(label_text)


def draw_x_axis(pointer):
    """
    Draw an x-axis centred on given origin, with given ratio
    :param pointer: Turtle pointer to draw with
    :return: None (just draws in turtle)
    """
    # draw x axis
    draw_line(pointer, ZERO, Y_ORIGIN, WIDTH, Y_ORIGIN)

    # x begins at minimum x value
    x = MIN_X
    # loops until the x value is smaller or equal to max_x
    while x <= MAX_X:
        # calculate screen_x and screen_y
        screen_x, screen_y = calc_to_screen_coord(x, ZERO)
        # draws ticks and labels on x axis
        draw_x_axis_tick(pointer, screen_x, screen_y)
        draw_x_axis_label(pointer, screen_x, screen_y, x)
        # jumps to next x
        x = x + STEP_SIZE


def draw_y_axis(pointer):
    """
    Draw an y-axis centred on given origin, with given ratio
    :param pointer: Turtle pointer to draw with
    :return: None (just draws in turtle)
    """
    # draw y axis
    draw_line(pointer, X_ORIGIN, ZERO, X_ORIGIN, HEIGHT)

    # y begins at minimum y value
    y = MIN_Y
    # loops until the y value is smaller or equal to max_y
    while y <= MAX_Y:
        # calculate screen_x and screen_y
        screen_x, screen_y = calc_to_screen_coord(ZERO, y)
        # draws ticks and labels on y axis
        draw_y_axis_tick(pointer, screen_x, screen_y)
        draw_y_axis_label(pointer, screen_x, screen_y, y)
        # jumps to next y
        y = y+0.25


def get_stars_location_file():
    if len(sys.argv) > 1:
        if sys.argv[1] == "-names":
            stars_location_file = input("enter a stars location file: ")
        else:
            stars_location_file = sys.argv[1]
    else:
        stars_location_file = input("enter a stars location file: ")
    return stars_location_file


def two_arguments_or_more():
    if len(sys.argv) == 3:
        if sys.argv[1] or sys.argv[2] == "-names":
            if sys.argv[1] == "-names":
                stars_location_file = sys.argv[2]
                return stars_location_file
            elif sys.argv[2] == "-names":
                stars_location_file = sys.argv[1]
                return stars_location_file
        if sys.argv[1] or sys.argv[2] != "-names":
            print("There was no names given in the two arguments, therefore the program can not be executed.")
            exit()
    else:
        print("Too many arguments given.")
        exit()
    return


def constellation_file():
    constellation_files = input("Enter a constellation file: ")
    while constellation_files != "":
        constellation_files = input("Enter a constellation file: ")


def prompt_for_input():
    if len(sys.argv) > 2:
        two_arguments_or_more()
    if len(sys.argv) <= 2:
        stars_location = get_stars_location_file()
    constellation_file()


def setup():
    """
    Setup the turtle window and return drawing pointer
    :return: Turtle pointer for drawing
    """
    turtle.bgcolor(BACKGROUND_COLOR)
    turtle.setup(WIDTH, HEIGHT, ZERO, ZERO)
    screen = turtle.getscreen()
    screen.delay(delay=ZERO)
    screen.setworldcoordinates(ZERO, ZERO, WIDTH, HEIGHT)
    pointer = turtle
    pointer.hideturtle()
    pointer.speed(ZERO)
    pointer.up()
    return pointer


def main():
    """
    Main constellation program
    :return: None
    """

    # Handle arguments
    prompt_for_input()
    # Read star information from file (function)
    # Turns off draw update until turtle.update() is called
    turtle.tracer(0)
    # Draw Axes (function)
    pointer = setup()
    pointer.color(AXIS_COLOR)
    draw_x_axis(pointer)
    draw_y_axis(pointer)

    turtle.update()
    # Draw Stars (function)
    turtle.update()
    # Loop getting filenames
    while False:
        # Read constellation file (function)
        # Draw Constellation (function)
        turtle.update()
        # Draw bounding box (Bonus) (function)
        turtle.update()
        pass


main()

print("\nClick on window to exit!\n")
turtle.exitonclick()
