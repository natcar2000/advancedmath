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


def calculate_discriminant(a, b, c):
    valida_valores(a, b, c)
    valida_coeficiente(a)

    return (b ** 2) - (4 * a * c)


def calculate_square_root(discriminant):
    for number in range(0, discriminant + 1):
        if number ** 2 == discriminant:
            return number
