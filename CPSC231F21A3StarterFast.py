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
HALF_OF_TICK = 15
ZERO = 0

# STAR CONSTANTS
STAR_COLOR = "white"
STAR_COLOR2 = "grey"
LABEL_FROM_AXIS = 20


def calc_to_screen_coord(x, y, x_origin, y_origin, ratio):
    """
    Convert a calculator (x,y) to a pixel (screen_x, screen_y) based on origin location and ratio
    :param x: Calculator x
    :param y: Calculator y
    :param x_origin: Pixel x origin of pixel coordinate system
    :param y_origin: Pixel y origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: (screen_x, screen_y) pixel version of calculator (x,y)
    """
    # calculates screen x and screen y and returns those values
    screen_x = x_origin + (x * ratio)
    screen_y = y_origin + (y * ratio)
    return screen_x, screen_y


def calculate_min_value(origin, ratio):
    """
    Calculate smallest INTEGER (x or y) value to draw based on formula given in the assignment
    :param origin: Pixel (x or y) origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: min_value: Smallest (x or y) value to draw for a 0->WIDTH of screen
    """
    to_be_floored = (ZERO - origin)/ratio
    min_value = int(floor(to_be_floored))
    return min_value


def calculate_max_value(origin, ratio):
    """
    Calculate largest INTEGER (x or y) value to draw based on formula given in the assignment
    :param origin: Pixel (x or y) origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: max_value: Largest (x or y) value to draw for a 0->WIDTH of screen
    """
    to_be_ceiled = (WIDTH - origin)/ratio
    max_value = int(ceil(to_be_ceiled))
    return max_value


def calc_minmax_x(x_origin, ratio):
    """
    Calculate smallest and largest calculator INTEGER x value to draw for a 0->WIDTH of screen
    Smallest: Convert a pixel x=0 to a calculator value and return integer floor
    Largest : Convert a pixel x=WIDTH to a calculator value and return integer ceiling
    :param x_origin: Pixel x origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: (Smallest, Largest) x value to draw for a 0->WIDTH of screen
    """
    # calculates min and max values and returns them for x axis
    min_x_value = calculate_min_value(x_origin, ratio)
    max_x_value = calculate_max_value(x_origin, ratio)
    return min_x_value, max_x_value


def calc_minmax_y(y_origin, ratio):
    """
    Calculate smallest and largest calculator INTEGER y value to draw for a 0->HEIGHT of screen
    Smallest: Convert a pixel y=0 to a calculator value and return integer floor
    Largest : Convert a pixel y=HEIGHT to a calculator value and return integer ceiling
    :param y_origin: Pixel y origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: (Smallest, Largest) y value to draw for a 0->HEIGHT of screen
    """
    # calculates min and max values and returns them for y axis
    max_y_value = calculate_max_value(y_origin, ratio)
    min_y_value = calculate_min_value(y_origin, ratio)
    return min_y_value, max_y_value


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


def draw_x_axis(pointer, x_origin, y_origin, ratio):
    """
    Draw an x-axis centred on given origin, with given ratio
    :param pointer: Turtle pointer to draw with
    :param x_origin: Pixel x origin of pixel coordinate system
    :param y_origin: Pixel y origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: None (just draws in turtle)
    """
    # draw x axis
    draw_line(pointer, ZERO, y_origin, WIDTH, y_origin)
    # calculates minimum and maximum x values
    min_x, max_x = calc_minmax_x(x_origin, ratio)
    # x begins at minimum x value
    x = min_x
    # loops until the x value is smaller or equal to max_x
    while x <= max_x:
        # calculate screen_x and screen_y
        screen_x, screen_y = calc_to_screen_coord(x, ZERO, x_origin, y_origin, ratio)
        # draws ticks and labels on x axis
        draw_x_axis_tick(pointer, screen_x, screen_y)
        draw_x_axis_label(pointer, screen_x, screen_y, x)
        # jumps to next x
        x = x+1


def draw_y_axis(pointer, x_origin, y_origin, ratio):
    """
    Draw an y-axis centred on given origin, with given ratio
    :param pointer: Turtle pointer to draw with
    :param x_origin: Pixel x origin of pixel coordinate system
    :param y_origin: Pixel y origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: None (just draws in turtle)
    """
    # draw y axis
    draw_line(pointer, x_origin, ZERO, x_origin, HEIGHT)

    # calculates minimum and maximum y values
    min_y, max_y = calc_minmax_y(y_origin, ratio)
    # y begins at minimum y value
    y = min_y
    # loops until the y value is smaller or equal to max_y
    while y <= max_y:
        # calculate screen_x and screen_y
        screen_x, screen_y = calc_to_screen_coord(ZERO, y, x_origin, y_origin, ratio)
        # draws ticks and labels on y axis
        draw_y_axis_tick(pointer, screen_x, screen_y)
        draw_y_axis_label(pointer, screen_x, screen_y, y)
        # jumps to next y
        y = y+1


def prompt_for_input():
    stars_location_file = sys.argv[0]
    if stars_location_file == "":
        stars_location_file_input = input("Enter a stars location file: ")
        while stars_location_file_input == "":
            print("no file name given")
            stars_location_file_input = input("Enter a stars location file: ")
    return stars_location_file

    while 1:
        constellation_files = input("Enter a constellation file: ")
        if constellation_files == "":
            break

    # stars_location_file = input("Enter a stars location file: ")
    # if stars_location_file == "":
        # while 1:
            # print("no file name given")
            # stars_location_file = input("Enter a stars location file: ")
            # if stars_location_file != "":
                # break
    # while 1:
    #     constellation_files = input("Enter a constellation file: ")
    #     if constellation_files == "":
    #         break

def setup():
    """
    Setup the turtle window and return drawing pointer
    :return: Turtle pointer for drawing
    """
    turtle.bgcolor(BACKGROUND_COLOR)
    turtle.setup(WIDTH, HEIGHT, 0, 0)
    screen = turtle.getscreen()
    screen.delay(delay=0)
    screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
    pointer = turtle
    pointer.hideturtle()
    pointer.speed(0)
    pointer.up()
    return pointer


def main():
    """
    Main constellation program
    :return: None
    """

    # Handle arguments
    pointer = setup()

    # Read star information from file (function)
    # Turns off draw update until turtle.update() is called
    turtle.tracer(0)
    # Draw Axes (function)

    x_origin, y_origin = 300, 300
    ratio = 75

    # Draw axis
    pointer.color(AXIS_COLOR)
    draw_x_axis(pointer, x_origin, y_origin, ratio)
    draw_y_axis(pointer, x_origin, y_origin, ratio)

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
