# DO NOT EDIT THE FOLLOWING LINES
# COURSE CPSC 231 FALL 2021
# INSTRUCTOR: Jonathan Hudson
# Wi52C3g7ZzkJ7XBcVRHY
# DO NOT EDIT THE ABOVE LINES

# INFORMATION FOR YOUR TA

# Class: CPSC 231 FALL 2021
# Name: Sergey Chitsvarin
# Tutorial: 02
# Student id: 30154758
# Date: 2021/11/23
# description: This program draws certain stars and constellations in the galaxy by using user input via command line arguments.
# in the command line arguments the user can provide "-names" and a stars location file. The "-names" trigger makes the program draw names for the stars that have names.
# The stars location file is a path to the stars information and only the stars in that certain file will be drawn. If the stars location file was not provided the program will continue asking
# until a valid file path is given. After the program will continue asking for constellation files to draw in alternating colors until the user enters "".

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

# COLOR CONSTANTS
TOTAL_COLORS = 3
RED_MODULUS = 1
YELLOW_MODULUS = 2
GREEN_MODULUS = 0


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
    # References: this code is taken from my Assignment 2 from class CPSC 231 Fall 2021 submitted on oct 22, 2021
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
        # if more than one argument is given the argument that is not "-names" is assigned as stars_location_file and "-names" is returned as false however if it is "-names" the program asks for a stars location file.
        if sys.argv[1] == "-names":
            stars_location_file = input("enter a stars location file: ")
            return True, stars_location_file
        else:
            stars_location_file = sys.argv[1]
            return False, stars_location_file
    else:
        # if no arguments were given the program will ask for the stars_location_file and return false for "-names".
        stars_location_file = input("enter a stars location file: ")
        return False, stars_location_file


def three_or_more_arguments():
    """
    Function handles input if three or more arguments are given and returns a boolean value for "-names" and a constellation file
    :return: boolean value for "-names" and a stars location file path.
    """
    if len(sys.argv) == MAX_NUMBER_OF_ARGUMENTS:
        # if 3 arguments are given and one of them is "-names" the other argument is assigned as stars_location_file.
        if sys.argv[1] or sys.argv[2] == "-names":
            if sys.argv[1] == "-names":
                stars_location_file = sys.argv[2]
                return True, stars_location_file
            elif sys.argv[2] == "-names":
                stars_location_file = sys.argv[1]
                return True, stars_location_file
        if sys.argv[1] or sys.argv[2] != "-names":
            # if neither of the arguments beside the name were not names the program exits because "-names" was not provided.
            print("There was no '-names' given in the two arguments, therefore the program can not be executed.")
            sys.exit(1)
    else:
        # if more than 3 arguments are given the program exits and tells the user too many arguments given.
        print("Too many arguments given.")
        sys.exit(1)


def handle_input():
    """
    Function decides weather the "three_or_more_arguments" or the "two_or_less_arguments" functions should be used
    :return: "three_or_more_arguments" or the "two_or_less_arguments" functions.
    """
    if len(sys.argv) > 2:
        # use the function for 3 or more arguments if there are more than 2 arguments.
        return three_or_more_arguments()
    if len(sys.argv) <= 2:
        # use the function for 2 or less arguments if the length of the command line is less than or equal to two.
        return two_or_less_arguments()


def read_line_by_line_constellation(opened_file):
    """
    Function goes through the constellation file line by line
    :param: opened_file is the constellation file provided by the user that is open
    :return: constellation_name, the name of the constellation and constellation_list a list of all the edges in the constellation.
    """
    constellation_list = []
    line_number = 0
    constellation_name = None
    for line in opened_file:
        line_number = line_number + 1
        if line_number == 1:
            # since the first line always contains the name the program counts the lines and makes sure to assign the name of the constellation to the first line stripped.
            constellation_name = line.rstrip()
        else:
            constellation_edges = line.rstrip().split(",")
            if not (len(constellation_edges) == NUMBER_OF_ENTRIES_IN_CONSTELLATION_FILE):
                # if the length of the constellation edges seperated by commas is not 2 the program gives out a warning.
                print("Invalid number of entries separated by commas on one of the lines, should be equal to 2.")
                sys.exit(1)
            constellation_list.append(constellation_edges)
    return constellation_name, constellation_list


def print_and_get_used_stars(constellation_name, constellation_list):
    """
    Function uses the constellation_name and the constellation_list to print what constellation contains certain stars.
    :param: constellation_name, name of the certain constellation.
    :param: constellation_list, list of all the stars and their details in the constellation.
    :return: constellation_name, the name of the constellation and constellation_list a list of all the edges in the constellation.
    """
    # references: Getting keys from a dictionary https://www.geeksforgeeks.org/python-get-dictionary-keys-as-a-list/
    used_stars = {}
    for sub_list in constellation_list:
        # the function goes through the list of constellations one by one.
        for name in sub_list:
            # the function goes through the sub_list of constellations to get the name and put it in as a key for the used_stars dictionary.
            used_stars[name] = True
    print(f"{constellation_name} constellation contains {list(used_stars.keys())}")
    return used_stars


def drawing_constellation(pointer, constellation_list, stars_with_names_dictionary, constellation_color):
    """
    Function draws a constellation in turtle using pointer, constellation_list, stars_with_names_dictionary and constellation_color
    :param: pointer, Turtle pointer to draw with.
    :param: constellation_list, a list of all the edges for a certain constellation
    :param: stars_with_names_dictionary, a dictionary that provides the details about stars using their name as the key
    :param: constellation_color, one of three colors(red,yellow,green) which alternate with each constellation drawn.
    :return: Function draws a given constellation in turtle.
    """
    try:
        for pairs in constellation_list:
            # function goes through each pair that creates an edge in the constellation.
            star_1 = pairs[0]
            star_2 = pairs[1]
            list_star_1 = stars_with_names_dictionary[star_1]
            list_star_2 = stars_with_names_dictionary[star_2]
            # finding the x and y for the first and the second star in the edge.
            x1 = list_star_1[0]
            y1 = list_star_1[1]
            x2 = list_star_2[0]
            y2 = list_star_2[1]
            # finding the on screen values for the x and y of both stars.
            screen_x1, screen_y1 = calc_to_screen_coord(x1, y1)
            screen_x2, screen_y2 = calc_to_screen_coord(x2, y2)
            pointer.color(constellation_color)
            # finally using all the values to draw the constellation.
            draw_line(pointer, screen_x1, screen_y1, screen_x2, screen_y2)
    except KeyError as error:
        # error in case the constellation can not be found.
        print(f"The star named {error} can not be found.")
        sys.exit(1)


def get_color(constellation_counter):
    """
    Get color for an equation based on counter of how many equations have been drawn (this is the xth equation)
    :param constellation_counter: Number x, for xth constellation being drawn
    :return: A string color for turtle to use
    """
    # References: this code is taken from my Assignment 2 from class CPSC 231 Fall 2021 submitted on oct 22, 2021
    # calculates modulus using equation counter and total colours
    modulus = constellation_counter % TOTAL_COLORS
    # returns alternate colors based on value of modulus
    if modulus == RED_MODULUS:
        return "red"
    if modulus == YELLOW_MODULUS:
        return "yellow"
    if modulus == GREEN_MODULUS:
        return "green"


def handle_constellation_file_input(pointer, stars_with_names_dictionary):
    """
    Function handles the input of constellation files using multiple functions.
    :param: pointer, Turtle pointer to draw with.
    :param: stars_with_names_dictionary, a dictionary that provides the details about stars using their name as the key
    :return: Function goes through constellation files exits the program for certain issues, and draws the constellations if no errors found.
    """
    constellation_counter = 0
    while True:
        # Read constellation file (function)
        constellation_file_path = input("Enter a constellation file: ")
        if constellation_file_path == "":
            # if the user enters "" for the constellation path file the program exits.
            exit()
        if os.path.isfile(constellation_file_path) is True:
            # if the file path exists draw the constellation with the correct color as well as checking for any other errors through use of other functions.
            constellation_color = get_color(constellation_counter)
            constellation_counter = constellation_counter + 1
            check_file_extension(constellation_file_path)
            opened_file = open_file(constellation_file_path)
            constellation_name, constellation_list = read_line_by_line_constellation(opened_file)
            used_stars = print_and_get_used_stars(constellation_name, constellation_list)
            close_file(opened_file, constellation_file_path)
            # Draw Constellation (function)
            drawing_constellation(pointer, constellation_list, stars_with_names_dictionary, constellation_color)
            turtle.update()
            # Draw bounding box (Bonus) (function)
            turtle.update()

        else:
            print("Entered path is not a file")


def check_user_input():
    """
    Function assigns print_names and stars_location_file values.
    :return: print_names, is a boolean value which if true will make the program draw names. Stars_location_file, is the path to the stars file.
    """
    print_names, stars_location_file = handle_input()
    # print_names and stars_location_file variables are assigned.
    return print_names, stars_location_file


def check_file_extension(stars_location_file):
    """
    Function checks if the extension of the file is ".dat" if it is not the function exits the program.
    :param: stars_location_file, the path given by the user to the star files.
    :return: Function goes through the stars_location_file making sure it will only be valid if the extension is ".dat"
    """
    # Checking file extension https://coderedirect.com/questions/120290/how-can-i-check-the-extension-of-a-file
    if not stars_location_file.endswith('.dat'):
        # if the stars_location_file does not end with ".dat" the program exits and provides an explanation.
        print(f"extension of the file '{stars_location_file}' is not '.dat'. Exiting")
        sys.exit(1)


def open_file(file_path):
    """
    Function reads through the file making sure it is not empty, the file exists as well as any other common errors.
    :param: file_path, the file path that goes to certain files such as constellation or star files.
    :return: opened_file, function opens the file and returns the opened file.
    """
    try:
        #  Reading file https://www.w3schools.com/python/python_file_open.asp
        # Exit with error https://stackoverflow.com/questions/9426045/difference-between-exit0-and-exit1-in-python
        # Check if a file is empty using os.stat(): https://thispointer.com/python-three-ways-to-check-if-a-file-is-empty/
        # Try/except errors while opening file https://stackoverflow.com/questions/5627425/what-is-a-good-way-to-handle-exceptions-when-trying-to-read-a-file-in-python
        opened_file = open(file_path, "r")
        if os.stat(file_path).st_size == ZERO:
            print(f"File {file_path} is empty")
            sys.exit(1)
            # if the file is empty the program exits with a warning.
    except FileNotFoundError:
        print(f"This file '{file_path}' is not found. Exiting.")
        # if the file can not be found the program exits with a warning.
        sys.exit(1)
    except Exception as error:
        # if any common error occurs the program exits with descriptive message.
        print(f"Unexpected error happened trying to open this file '{file_path}'. Error {error}")
        sys.exit(1)
    return opened_file


def read_line_by_line_stars(opened_file):
    """
    Function goes through the stars file and uses the information to create the stars_with_names_dictionary and the all_stars_list.
    :param: opened_file, the opened stars file.
    :return: stars_with_names_dictionary, a dictionary that provides the details about stars using their name as the key, all_stars_list, a list of the details of all stars.

    """
    # reading file line by line https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list
    # rstrip function https://www.geeksforgeeks.org/python-string-rstrip/?ref=lbp
    # add elements to list https://www.w3schools.com/python/python_lists_add.asp
    stars_with_names_dictionary = {}
    all_stars_list = []
    for line in opened_file:
        # function loops through every line in the opened_file.
        star_information = line.rstrip().split(',')
        if not len(star_information) == 7:
            # if the length of the line is not as it should be the program exits with a descriptive message.
            print("invalid number of entries separated by commas, should be equal to 7.")
            sys.exit(1)
        x = float(star_information[0])
        y = float(star_information[1])
        mag = float(star_information[4])
        names = star_information[6].split(';')
        for name in names:
            # function loops through all of the names and places individual name with it's details.
            star_list = [x, y, mag, name]
            all_stars_list.append(star_list)
            if name != "":
                stars_with_names_dictionary[name] = star_list
                print(f"{name} is at ({x},{y}) with magnitude {mag}")
    return all_stars_list, stars_with_names_dictionary


def close_file(opened_file, file_path):
    """
    Function closes the previously opened file
    :param: opened_file, the previously opened file containing either star or constellation information.
    :param: file_path, either the path to star files or constellation files.
    :return: Function closes opened file.
    """
    try:
        opened_file.close()
    except Exception as error:
        # program checks for any errors while closing the file and exits the program if there are errors found with a descriptive message.
        print(f"Unexpected error happened trying to close this file '{file_path}'. Error {error}")
        sys.exit(1)


def read_star_information(stars_location_file):
    """
    Function checks stars_location_files, opens them uses them to read the information and closes the file using other functions
    :param: stars_location_file, path given by user to the star files
    :return: stars_with_names_dictionary, a dictionary that provides the details about stars using their name as the key, all_stars_list, a list of the details of all stars.
    """
    check_file_extension(stars_location_file)
    opened_file = open_file(stars_location_file)
    all_stars_list, stars_with_names_dictionary = read_line_by_line_stars(opened_file)
    close_file(opened_file, stars_location_file)
    return all_stars_list, stars_with_names_dictionary


def draw_star(pointer, x, y, mag, star_color):
    """
    Function draws a star in turtle using pointer, x, y, mag and star_color
    :param: pointer, Turtle pointer to draw with.
    :param: x, on screen x location of star.
    :param: y, on screen y location of star.
    :param: mag, magnitude of the star
    :param: star_color, the color of the star depending on if it has a name or does not have a name.
    :return: Function draws a given star in turtle.
    """
    # function finds the on screen values, draws the star with the correct diameter using the magnitude of the star.
    screen_x, screen_y = calc_to_screen_coord(x, y)
    pointer.penup()
    pointer.goto(screen_x, screen_y)
    pointer.color(star_color)
    pointer.pendown()
    diameter = 10/(mag + 2)
    pointer.dot(diameter)
    pointer.penup()


def draw_star_name(pointer, name_of_star, x, y):
    """
    Function draws a star name in turtle
    :param: pointer, Turtle pointer to draw with.
    :param: name_of_star, the name of a certain star.
    :param: x, on screen x location of star.
    :param: y, on screen y location of star.
    :return: Function draws a given star name in turtle.
    """
    screen_x, screen_y = calc_to_screen_coord(x, y)
    # function goes to the on screen coordinates of the star and adds 5 pixels over it to make sure the name of the s tar does not get in the way of the star.
    pointer.goto(screen_x, screen_y + HALF_OF_TICK)
    pointer.write(name_of_star, font=("Arial", 5, "normal"))


def drawing_stars(pointer, print_names, all_stars_list, stars_with_names_dictionary):
    """
    Function draws a star in turtle using pointer, x, y, mag and star_color
    :param: pointer, Turtle pointer to draw with.
    :param: print_names
    :param: all_stars_list, a list of the details of all stars.
    :param: stars_with_names_dictionary, a dictionary that provides the details about stars using their name as the key
    :return: Function draws multiple stars and their names in turtle screen.
    """
    # https://www.geeksforgeeks.org/iterate-over-a-list-in-python/
    for i in all_stars_list:
        x = i[0]
        y = i[1]
        mag = i[2]
        draw_star(pointer, x, y, mag, STAR_COLOR2)
        # the function draws stars from the all_star_list
    # https://www.w3schools.com/python/trypython.asp?filename=demo_dictionary_loop_items
    for star_name, my_value in stars_with_names_dictionary.items():
        # the function takes the key and the value assigned in the stars_with_names_dictionary and draws the stars and their names.
        x = my_value[0]
        y = my_value[1]
        mag = my_value[2]
        draw_star(pointer, x, y, mag, STAR_COLOR)
        if print_names is True:
            draw_star_name(pointer, star_name, x, y)


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
    handle_constellation_file_input(pointer, stars_with_names_dictionary)


main()

print("\nClick on window to exit!\n")
turtle.exitonclick()
