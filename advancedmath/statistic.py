from function import calculate_square_root


def validate_values(*values):
    if len(values) == 0:
        raise ValueError("At least one value is required.")


def arithmetic_mean(*values):    
    validate_values(values)
    
    total = 0
    
    for value in values:
        validate_values(value)
        total += value
    
    return total / len(values)


def weighted_mean(weights, *values):
    validate_values(weights)
    validate_values(values)
 
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


def mode(*values):
    validate_values(values)
    
    times = []
    elements = []
    modes = []
       
    for value in values:
        if value not in elements:
            occurrences = values.count(value)
            times.append(occurrences)
            elements.append(value)
            
    
    for i in range(len(times)):
        if times[i] == max(times):
            modes.append(elements[i])
        
    if len(values) > 1 and max(times) == 1:
        return "No mode."
        
    return modes
    return numerator / total


def median(*values):
    validate_values(values)
    
    values = sorted(values)
    
    if len(values) % 2 == 1:
        return values[len(values) // 2]
    
    factor1 = values[len(values) // 2]
    factor2 = values[len(values) // 2 - 1]
    
    return (factor1 + factor2) / 2
