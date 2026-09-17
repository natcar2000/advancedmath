def valida_valores(*valores):
    for valor in valores:
        if type(valor) not in (int, float):
            raise TypeError("Numbers must have integer or float values.")


def valida_coeficiente(coeficiente):
    if coeficiente == 0:
        raise ValueError("Coefficient 'a' must not be 0.")
    

def linear_function(a, b, x):    
    valida_valores(a, b, x)
    valida_coeficiente(a)
    
    return (a * x) + b


def linear_root(a, b):
    valida_valores(a, b)
    valida_coeficiente(a)

    return -b / a


def quadratic_function(a, b, c, x):
    valida_valores(a, b, c, x)
    valida_coeficiente(a)

    return (a * (x ** 2)) + (b * x) + c


def quadratic_roots(a, b, c):
    valida_valores(a, b, c)
    valida_coeficiente(a)

    discriminant = calculate_discriminant(a, b, c)

    if discriminant < 0:
        return "Negative discriminant. Function has no real roots."
    
    square_root = calculate_square_root(discriminant)
    
    x1 = (-b + square_root) / (2 * a)
    x2 = (-b - square_root) / (2 * a)

    return x1, x2


def calculate_discriminant(a, b, c):
    valida_valores(a, b, c)
    valida_coeficiente(a)

    return (b ** 2) - (4 * a * c)


def calculate_square_root(discriminant):
    valida_valores(discriminant)

    if discriminant == 0:
        return 0

    guess = discriminant
    for _ in range(20):
        guess = (guess + discriminant / guess) / 2

    return guess


def exponential_function(a, x, start=None):
    valida_valores(a, x)
    valida_coeficiente(a)

    if a == 1:
        raise ValueError("Value of 'a' cannot be 1.")

    if start is None:
        return a ** x

    valida_valores(start)       
    return start * (a ** x)
