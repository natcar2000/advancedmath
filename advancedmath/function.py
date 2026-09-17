def validate_values(*values):
    for valor in values:
        if type(valor) not in (int, float):
            raise TypeError("Numbers must have integer or float values.")


def validate_coefficient(coefficient):
    if coeficiente == 0:
        raise ValueError("Coefficient 'a' must not be 0.")
    

def linear_function(a, b, x):    
    validate_values(a, b, x)
    validate_coefficient(a)
    
    return (a * x) + b


def linear_root(a, b):
    valida_values(a, b)
    valida_coefficient(a)

    return -b / a


def quadratic_function(a, b, c, x):
    validate_values(a, b, c, x)
    validate_coefficient(a)

    return (a * (x ** 2)) + (b * x) + c


def quadratic_roots(a, b, c):
    validate_values(a, b, c)
    validate_coefficient(a)

    discriminant = calculate_discriminant(a, b, c)

    if discriminant < 0:
        return "Negative discriminant. Function has no real roots."
    
    square_root = calculate_square_root(discriminant)
    
    x1 = (-b + square_root) / (2 * a)
    x2 = (-b - square_root) / (2 * a)

    return x1, x2


def calculate_discriminant(a, b, c):
    validate_values(a, b, c)
    validate_coefficient(a)

    return (b ** 2) - (4 * a * c)


def calculate_square_root(discriminant):
    validate_values(discriminant)

    if discriminant == 0:
        return 0

    guess = discriminant
    for _ in range(20):
        guess = (guess + discriminant / guess) / 2

    return guess


def exponential_function(a, x, start=None):
    validate_values(a, x)
    validate_coefficient(a)

    if a == 1:
        raise ValueError("Value of 'a' cannot be 1.")

    if start is None:
        return a ** x

    validate_values(start)       
    return start * (a ** x)


def logarithmic_function_1(base, x, medium=None, lower=None, upper=None, precision=1e-10):
    validate_values(base, x)
    validate_coefficient(base)
    
    if base == 1:
        raise ValueError("Value of base cannot be 1.")

    for value in range(x):
        if base ** value <= x:
            integer = value
            
    if base ** integer == x:
        return integer

    if lower is None and upper is None:
        lower = integer
        upper = integer+1

    medium = (lower+upper) / 2
    
    if base ** medium < x:
        lower = medium
    else:
        upper = medium
        
    if abs((base ** medium) - x) < precision:
        return medium
        
    return logarithmic_function_1(base, x, medium, lower, upper, precision)


def logarithmic_function_2(base, x, medium=None, lower=None, upper=None, precision=1e-10):    
    validate_values(base, x)
    validate_coefficient(base)
    
    integer = int(x)
    
    for value in range(integer):
        if base ** value <= x:
            v = value
    
    if lower is None and upper is None:
        lower = v
        upper = v+1
    
    medium = (lower+upper) / 2

    if base ** medium < x:
        lower = medium
    else:
        upper = medium
        
    if abs((base ** medium) - x) < precision:
        return medium
        
    return logarithmic_function_2(base, x, medium, lower, upper, precision)


def logarithmic_function_3(base, x, medium=None, lower=None, upper=None, precision=1e-10):    
    validate_values(base, x)
    validate_coefficient(base)

    result = logarithmic_function_2(base, 1/x)
    return -result
