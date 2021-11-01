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


def prompt_for_input():
    stars_location_file = input("Enter a stars location file: ")
    if stars_location_file == "":
        print("no file name given")
        while 1:
            constellation_files = input("Enter a constellation file: ")
            if constellation_files == "":
                break


prompt_for_input()


def main(user_input):
    """
    Main constellation program
    :return: None
    """
    print(user_input)
    # Handle arguments
    pointer = setup()
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


main(sys.argv[0:])

print("\nClick on window to exit!\n")
turtle.exitonclick()