from function import calculate_square_root
from function import validate_values


def arithmetic_mean(*values):
    total = 0
    
    for value in values:
        validate_values(value)
        total += value
    
    return total / len(values)


def weighted_mean(weights, *values):
    if len(weights) != len(values):
        raise ValueError("Weights and values data must have the same length.")
    
    total = 0
    numerator = 0
    
    for index in range(len(weights)):
        validate_values(weights[index], values[index])
        numerator += weights[index] * values[index]
        total += weights[index]
    
    if total == 0:
        raise ValueError("The total of weights must be different of zero.")
        
    return numerator / total
