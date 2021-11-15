import sys


#stars_location_file = 'C:\\Users\\serge\\OneDrive\\Desktop\\University\\2021\\Cpsc 231\\assignments\\A3\\CPSC_231_A3\\StarFiles\\stars_1.dat'
stars_location_file = "C:/Users/serge/OneDrive/Desktop/University/2021/Cpsc 231/assignments/A3/CPSC_231_A3/StarFiles/stars_1.dat"

#stars_location_file = "C:/Users/serge/OneDrive/Desktop/University/2021/Cpsc 231/assignments/A3/CPSC_231_A3/StarFiles/stars_1_invalid_number_of_entries.dat"
#stars_location_file = "C:/Users/serge/OneDrive/Desktop/University/2021/Cpsc 231/assignments/A3/CPSC_231_A3/StarFiles/stars_1_invalid_number_of_entries_greater_than_seven.dat"
#stars_location_file = "C:/Users/serge/OneDrive/Desktop/University/2021/Cpsc 231/assignments/A3/CPSC_231_A3/StarFiles/stars_1_invalid_number_of_entries_ending_with_comma.dat"


#stars_location_file = "xxx"
#stars_location_file = "xxx.dat"
#stars_location_file = ".dat"
#stars_location_file = ""

# Checking file extension https://coderedirect.com/questions/120290/how-can-i-check-the-extension-of-a-file
if not stars_location_file.endswith('.dat'):
    print(f"extension of the file '{stars_location_file}' is not '.dat'. Exiting")
    sys.exit(1)
try:
    #  Reading file https://www.w3schools.com/python/python_file_open.asp
    # Exit with error https://stackoverflow.com/questions/9426045/difference-between-exit0-and-exit1-in-python
    # Try/except errors while opening file https://stackoverflow.com/questions/5627425/what-is-a-good-way-to-handle-exceptions-when-trying-to-read-a-file-in-python
    opened_file = open(stars_location_file, "r")
except FileNotFoundError:
    print(f"This file '{stars_location_file}' is not found. Exiting.")
    sys.exit(1)
except Exception as error:
    print(f"Unexpected error happened trying to open this file '{stars_location_file}'. Error {error}")
    sys.exit(1)

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
    x = star_information[0]
    y = star_information[1]
    mag = star_information[4]
    names = star_information[6]
    star_list = [x, y, mag, names]
    all_stars_list.append(star_list)
    if names != "":
        stars_with_names_dictionary[names] = star_list
        print(f"{names} is at ({x},{y}) with magnitude {mag}")
# ALPHERATZ is at (0.873265,0.031968) with magnitude 2.07
# print(stars_with_names_dictionary)

try:
    opened_file.close()
except Exception as error:
    print(f"Unexpected error happened trying to close this file '{stars_location_file}'. Error {error}")
    sys.exit(1)





