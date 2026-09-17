def validate_values(*values):
    for valor in values:
        if type(valor) not in (int, float):
            raise TypeError("Numbers must have integer or float values.")


def validate_coefficient(coefficient):
    if coefficient == 0:
        raise ValueError("Coefficient 'a' must not be 0.")
    

def linear_function(a, b, x):    
    validate_values(a, b, x)
    validate_coefficient(a)
    
    return (a * x) + b


def linear_root(a, b):
    validate_values(a, b)
    validate_coefficient(a)

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

    if discriminant < 0:
        raise ValueError("Cannot calculate the square root of a negative value.")

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


def logarithmic_function(base, x, medium=None, lower=None, upper=None, precision=1e-10):
    validate_values(base, x)
    validate_coefficient(base)
    
    value = 0
    power = 1
    
    if base < 0:
        raise ValueError("Base cannot be smaller than 0.")

    if base == 1:
        raise ValueError("Base cannot be 1.")
        
    if x <= 0:
        raise ValueError("Value of x must be greater than 0.")

    elif x == 1:
        return 0
        
    elif 0 < x < 1:
        return -logarithmic_function(base, 1 / x, precision=precision)

    while power <= x:
        integer = value
        value += 1
        power *= base

    if base ** integer == x:
        return integer

    if lower is None and upper is None:
        lower = integer
        upper = integer + 1

    medium = (lower + upper) / 2

    if base ** medium < x:
        lower = medium
    else:
        upper = medium

    if abs((base ** medium) - x) < precision:
        return medium
        
    return logarithmic_function(base, x, medium, lower, upper, precision)
