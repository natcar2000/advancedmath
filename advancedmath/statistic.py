from function import calculate_square_root
from function import validate_values


def mean(*roll):
    total = 0
    
    for data in roll:
        validate_values(data)
        total += data
    
    return total / len(roll)
