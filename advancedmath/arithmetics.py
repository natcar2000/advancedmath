def factorial(n):
    if type(n) != int:
        raise TypeError("The value of 'n' must be a integer number.")
    if n < 0:
        raise ValueError("The value of 'n' must be a non-negative integer.")
    elif n == 0 or n == 1: 
        return 1
    else:
        return n * factorial(n-1)
