def linear_function(a, b, x):
    if type(a) not in (int, float) or type(b) not in (int, float) or type(x) not in (int, float):
        raise TypeError("Numbers must have integer or float values.")
    
    if a == 0:
        raise ValueError("Coefficient 'a' must not be 0.")

    return (a * x) + b
