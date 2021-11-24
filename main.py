import sys


def draw_bounding_box(pointer, stars_with_names_dictionary, used_stars):
    for star in used_stars:
        star_details = stars_with_names_dictionary[star]
        star_details_values = star_details.pop(3)
        y_values = star_details[1]
        x_values = star_details[0]
        max_x = max(x_values)
        max_y = max(y_values)
        min_x = min(x_values)
        min_y = min(y_values)
        right_boundary = max_x + HALF_OF_TICK
        left_boundary = min_x - HALF_OF_TICK
        top_boundary = max_y + HALF_OF_TICK
        bottom_boundary = min_y - HALF_OF_TICK
        pointer.color(BOUNDARY_COLOR)
        draw_line(pointer, left_boundary, top_boundary, right_boundary, top_boundary)
        draw_line(pointer, right_boundary, top_boundary, right_boundary, bottom_boundary)
        draw_line(pointer, right_boundary, bottom_boundary, left_boundary, bottom_boundary)
        draw_line(pointer, left_boundary, bottom_boundary, left_boundary, top_boundary)
