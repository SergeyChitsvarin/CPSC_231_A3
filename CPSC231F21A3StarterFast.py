# DO NOT EDIT THE FOLLOWING LINES
# COURSE CPSC 231 FALL 2021
# INSTRUCTOR: Jonathan Hudson
# Wi52C3g7ZzkJ7XBcVRHY
# DO NOT EDIT THE ABOVE LINES

# INFORMATION FOR YOUR TA

import sys
import os
import turtle

# STARTER CONSTANTS
BACKGROUND_COLOR = "black"
WIDTH = 600
HEIGHT = 600
# AXIS CONSTANTS
AXIS_COLOR = "blue"
HALF_OF_TICK = 15
ZERO = 0
MIDDLE_OF_SCREEN = 300
# STAR CONSTANTS
STAR_COLOR = "white"
STAR_COLOR2 = "grey"


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


def drawing_axes_lines(pointer):
    """
    Draws the Y and X axes in blue so that the origin is at (300, 300)
    :param pointer: the turtle pointer that draws
    :return: drawing on the turtle screen
    """
    pointer.color(AXIS_COLOR)
    pointer.penup()
    pointer.goto(ZERO, MIDDLE_OF_SCREEN)
    pointer.pendown()
    pointer.goto(WIDTH, MIDDLE_OF_SCREEN)
    pointer.penup()
    pointer.goto(MIDDLE_OF_SCREEN, HEIGHT)
    pointer.pendown()
    pointer.goto(MIDDLE_OF_SCREEN, ZERO)
    pointer.penup()


def drawing_ticks_x_axis(pointer):
    """
    Draws ticks on the X axis using the turtle pointer
    :param pointer: the turtle pointer that draws
    :return: drawing on the turtle screen
    """
    pointer.color(AXIS_COLOR)
    pointer.penup()
    pointer.goto(ZERO, MIDDLE_OF_SCREEN+HALF_OF_TICK)
    pointer.pendown()
    pointer.goto(ZERO, MIDDLE_OF_SCREEN-HALF_OF_TICK)
    pointer.penup()


def drawing_ticks_y_axis(pointer):
    """
    Draws ticks on the Y axis using the turtle pointer
    :param pointer: the turtle pointer that draws
    :return: drawing on the turtle screen
    """
    pointer.color(AXIS_COLOR)
    pointer.penup()
    pointer.goto(MIDDLE_OF_SCREEN+HALF_OF_TICK, HEIGHT)
    pointer.pendown()
    pointer.goto(MIDDLE_OF_SCREEN-HALF_OF_TICK, HEIGHT)
    pointer.penup()


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


def main():
    """
    Main constellation program
    :return: None
    """

    # Handle arguments
    pointer = setup()
    drawing_ticks_x_axis(pointer)
    drawing_axes_lines(pointer)
    drawing_ticks_y_axis(pointer)
    # Read star information from file (function)
    # Turns off draw update until turtle.update() is called
    turtle.tracer(0)
    # Draw Axes (function)
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
