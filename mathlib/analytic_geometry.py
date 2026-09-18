from function import calculate_square_root
from function import validate_values


def distance_between_points(x1, y1, x2, y2):
    validate_values(x1, y1, x2, y2)
    value = ((x2-x1) ** 2) + ((y2-y1) ** 2)
    return calculate_square_root(value)


def midpoint(x1, y1, x2, y2):
    validate_values(x1, y1, x2, y2)
    x, y = (x1+x2)/2, (y1+y2)/2
    return x, y


def slope(x1, y1, x2, y2):
    validate_values(x1, y1, x2, y2)
    if x1 == x2:
        return "Undefined slope."
        
    return (y2-y1) / (x2-x1)
