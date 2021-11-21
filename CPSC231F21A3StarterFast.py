# DO NOT EDIT THE FOLLOWING LINES
# COURSE CPSC 231 FALL 2021
# INSTRUCTOR: Jonathan Hudson
# Wi52C3g7ZzkJ7XBcVRHY
# DO NOT EDIT THE ABOVE LINES

# INFORMATION FOR YOUR TA

import sys
import os
# reference: https://www.geeksforgeeks.org/python-os-path-isfile-method/
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
MAX_NUMBER_OF_ARGUMENTS = 3

# FILE CONSTANTS
NUMBER_OF_ENTRIES_IN_CONSTELLATION_FILE = 2


def calc_to_screen_coord(x, y):
    """
    Convert a calculator (x,y) to a pixel (screen_x, screen_y) based on origin location and ratio
    :param x: Calculator x
    :param y: Calculator y
    :return: (screen_x, screen_y) pixel version of calculator (x,y)
    """
    # Refferences: this code is taken from my Assignment 2 from class CPSC 231 Fall 2021 submitted on oct 22, 2021
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
    # Refferences: this code is taken from my Assignment 2 from class CPSC 231 Fall 2021 submitted on oct 22, 2021
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
    # Refferences: this code is taken from my Assignment 2 from class CPSC 231 Fall 2021 submitted on oct 22, 2021
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
    1)this code is taken from my Assignment 2 from class CPSC 231 Fall 2021 submitted on oct 22, 2021
    2)writing on screen in turtle https://stackoverflow.com/questions/15141031/python-turtle-draw-text-with-on-screen-with-larger-font
    3) align text to centre in turtle https://stackoverflow.com/questions/42265682/how-to-center-text-using-turtle-module-in-python
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
    # References: this code is taken from my Assignment 2 from class CPSC 231 Fall 2021 submitted on oct 22, 2021
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
    1)this code is taken from my Assignment 2 from class CPSC 231 Fall 2021 submitted on oct 22, 2021
    2)writing on screen in turtle https://stackoverflow.com/questions/15141031/python-turtle-draw-text-with-on-screen-with-larger-font
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
    # References: this code is taken from my Assignment 2 from class CPSC 231 Fall 2021 submitted on oct 22, 2021
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
    # References: this code is taken from my Assignment 2 from class CPSC 231 Fall 2021 submitted on oct 22, 2021
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


def two_or_less_arguments():
    """
    Function handles input if two or less command line arguments are given and returns the stars location file and a boolean value
    :return: stars location file path and a boolean value for "-names"
    """
    if len(sys.argv) > 1:
        if sys.argv[1] == "-names":
            stars_location_file = input("enter a stars location file: ")
            return True, stars_location_file
        else:
            stars_location_file = sys.argv[1]
            return False, stars_location_file
    else:
        stars_location_file = input("enter a stars location file: ")
        return False, stars_location_file


def three_or_more_arguments():
    """
    Function handles input if three or more arguments are given and returns a boolean value for "-names" and a constellation file
    :return: boolean value for "-names" and a stars location file path.
    """
    if len(sys.argv) == MAX_NUMBER_OF_ARGUMENTS:
        if sys.argv[1] or sys.argv[2] == "-names":
            if sys.argv[1] == "-names":
                stars_location_file = sys.argv[2]
                return True, stars_location_file
            elif sys.argv[2] == "-names":
                stars_location_file = sys.argv[1]
                return True, stars_location_file
        if sys.argv[1] or sys.argv[2] != "-names":
            print("There was no '-names' given in the two arguments, therefore the program can not be executed.")
            exit()
    else:
        print("Too many arguments given.")
        exit()


def handle_input():
    """
    Function decides weather the "three_or_more_arguments" or the "two_or_less_arguments" functions should be used
    :return: "three_or_more_arguments" or the "two_or_less_arguments" functions.
    """
    if len(sys.argv) > 2:
        return three_or_more_arguments()
    if len(sys.argv) <= 2:
        return two_or_less_arguments()


def read_line_by_line_constellation(opened_file):
    constellation_list = []
    line_number = 0
    constellation_name = None
    for line in opened_file:
        line_number = line_number + 1
        if line_number == 1:
            constellation_name = line.rstrip()
        else:
            constellation_edges = line.rstrip().split(",")
            if not (len(constellation_edges) == NUMBER_OF_ENTRIES_IN_CONSTELLATION_FILE):
                print("Invalid number of entries separated by commas on one of the lines, should be equal to 2.")
                sys.exit(1)
            constellation_list.append(constellation_edges)
    return constellation_name, constellation_list


def constellation_to_console(constellation_name, constellation_list):
    # references: Getting keys from a dictionary https://www.geeksforgeeks.org/python-get-dictionary-keys-as-a-list/
    used_stars = {}
    for sub_list in constellation_list:
        for name in sub_list:
            used_stars[name] = True
    print(f"{constellation_name} constellation contains {list(used_stars.keys())}")


def handle_constellation_file_input():
    while True:
        # Read constellation file (function)
        constellation_file_path = input("Enter a constellation file: ")
        if constellation_file_path == "":
            exit()
        if os.path.isfile(constellation_file_path) is True:
            check_file_extension(constellation_file_path)
            opened_file = open_file(constellation_file_path)
            constellation_name, constellation_list = read_line_by_line_constellation(opened_file)
            constellation_to_console(constellation_name, constellation_list)
            # return_into_console_constellation(opened_file)
            close_file(opened_file, constellation_file_path)
            # Draw Constellation (function)
            turtle.update()
            # Draw bounding box (Bonus) (function)
            turtle.update()
        else:
            print("Entered path is not a file")


def check_user_input():
    """
    *****************************CHANGE ME LATER***************************************
    :return: "three_or_more_arguments" or the "two_or_less_arguments" functions.
    """
    print_names, stars_location_file = handle_input()
    return print_names, stars_location_file


def check_file_extension(stars_location_file):
    # Checking file extension https://coderedirect.com/questions/120290/how-can-i-check-the-extension-of-a-file
    if not stars_location_file.endswith('.dat'):
        print(f"extension of the file '{stars_location_file}' is not '.dat'. Exiting")
        sys.exit(1)


def open_file(file_path):
    try:
        #  Reading file https://www.w3schools.com/python/python_file_open.asp
        # Exit with error https://stackoverflow.com/questions/9426045/difference-between-exit0-and-exit1-in-python
        # Check if a file is empty using os.stat(): https://thispointer.com/python-three-ways-to-check-if-a-file-is-empty/
        # Try/except errors while opening file https://stackoverflow.com/questions/5627425/what-is-a-good-way-to-handle-exceptions-when-trying-to-read-a-file-in-python
        opened_file = open(file_path, "r")
        if os.stat(file_path).st_size == ZERO:
            print(f"File {file_path} is empty")
            sys.exit(1)
    except FileNotFoundError:
        print(f"This file '{file_path}' is not found. Exiting.")
        sys.exit(1)
    except Exception as error:
        print(f"Unexpected error happened trying to open this file '{file_path}'. Error {error}")
        sys.exit(1)
    return opened_file


def read_line_by_line_stars(opened_file):
    # reading file line by line https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list
    # rstrip function https://www.geeksforgeeks.org/python-string-rstrip/?ref=lbp
    # add elements to list https://www.w3schools.com/python/python_lists_add.asp
    stars_with_names_dictionary = {}
    all_stars_list = []
    for line in opened_file:
        star_information = line.rstrip().split(',')
        if not len(star_information) == 7:
            print("invalid number of entries separated by commas, should be equal to 7.")
            sys.exit(1)
        x = float(star_information[0])
        y = float(star_information[1])
        mag = float(star_information[4])
        names = star_information[6].split(';')
        for name in names:
            star_list = [x, y, mag, name]
            all_stars_list.append(star_list)
            if name != "":
                stars_with_names_dictionary[name] = star_list
                print(f"{name} is at ({x},{y}) with magnitude {mag}")
    print(all_stars_list)
    return all_stars_list, stars_with_names_dictionary


def close_file(opened_file, file_path):
    try:
        opened_file.close()
    except Exception as error:
        print(f"Unexpected error happened trying to close this file '{file_path}'. Error {error}")
        sys.exit(1)


def read_star_information(stars_location_file):
    check_file_extension(stars_location_file)
    opened_file = open_file(stars_location_file)
    all_stars_list, stars_with_names_dictionary = read_line_by_line_stars(opened_file)
    close_file(opened_file, stars_location_file)
    return all_stars_list, stars_with_names_dictionary


def draw_star(pointer, x, y, mag, star_color):
    screen_x, screen_y = calc_to_screen_coord(x, y)
    pointer.penup()
    pointer.goto(screen_x, screen_y)
    pointer.color(star_color)
    pointer.pendown()
    diameter = 10/(mag + 2)
    pointer.dot(diameter)
    pointer.penup()


def draw_star_name(pointer, name_of_star, x, y):
    screen_x, screen_y = calc_to_screen_coord(x, y)
    pointer.goto(screen_x, screen_y + HALF_OF_TICK)
    pointer.write(name_of_star, font=("Arial", 5, "normal"))


def drawing_stars(pointer, print_names, all_stars_list, stars_with_names_dictionary):
    # https://www.geeksforgeeks.org/iterate-over-a-list-in-python/
    for i in all_stars_list:
        x = i[0]
        y = i[1]
        mag = i[2]
        draw_star(pointer, x, y, mag, STAR_COLOR2)
    # https://www.w3schools.com/python/trypython.asp?filename=demo_dictionary_loop_items
    for star_name, my_value in stars_with_names_dictionary.items():
        x = my_value[0]
        y = my_value[1]
        mag = my_value[2]
        draw_star(pointer, x, y, mag, STAR_COLOR)
        if print_names is True:
            draw_star_name(pointer, star_name, x, y)


def drawing_constellation():
    print("hi")


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
    print_names, stars_location_file = check_user_input()
    # Read star information from file (function)
    all_stars_list, stars_with_names_dictionary = read_star_information(stars_location_file)
    # Turns off draw update until turtle.update() is called
    turtle.tracer(0)
    # Draw Axes (function)
    pointer = setup()
    pointer.color(AXIS_COLOR)
    draw_x_axis(pointer)
    draw_y_axis(pointer)

    turtle.update()
    # Draw Stars (function)
    drawing_stars(pointer, print_names, all_stars_list, stars_with_names_dictionary)
    turtle.update()
    # Loop getting filenames
    handle_constellation_file_input()


main()

print("\nClick on window to exit!\n")
turtle.exitonclick()
