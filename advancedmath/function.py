def linear_function(a, b, x):
    if a == 0:
        raise ValueError("Coeficient 'a' must nob be 0.")

    if type(a) not in (int, float) or type(b) not in (int, float) or type(x) not in (int, float):
        raise TypeError("Numbers must have integer or float values.")

    return (a * x) + b
