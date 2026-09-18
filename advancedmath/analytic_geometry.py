from function import calculate_square_root
from function import validate_values


def distance_between_points(x1, y1, x2, y2):
    validate_values(x1, y1, x2, y2)
    value = ((x2-x1) ** 2) + ((y2-y1) ** 2)
    return calculate_square_root(value)
