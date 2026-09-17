def factorial(n):
    if type(n) != int:
        raise TypeError("Value must be a integer number.")
        
    if n < 0:
        raise ValueError("Value must be a non-negative integer.")        
    elif n == 0 or n == 1: 
        return 1        
    else:
        return n * factorial(n-1)


def permutation(n):
    return factorial(n)


def circular_permutation(n):
    return factorial(n-1)


def arrangement(n, k):   
    return factorial(n) // factorial(n-k)


def combination(n, k):
    return factorial(n) // (factorial(k) * factorial(n-k))


def combination_with_repetition(n, k):
    return combination(n+k-1, k)
