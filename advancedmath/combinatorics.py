from .exceptions import InvalidPermutationError


def factorial(n):
    if type(n) != int:
        raise TypeError("Value of 'n' must be a integer number.")
        
    if n < 0:
        raise ValueError("Value of 'n' must be a non-negative integer.")        
    elif n == 0 or n == 1: 
        return 1        
    else:
        return n * factorial(n-1)


def permutation(n, k):   
    if type(n) != int:
        raise TypeError("Value of 'n' must be a integer number.")
    
    if n < 0:
        raise ValueError("Value of 'n' must be a non-negative integer.")
    
    if type(k) != int:
        raise TypeError("Value of 'k' must be a integer number.")

    if k > n:
        raise InvalidPermutationError("Value of 'k' cannot be greater than 'n'.")

    if k < 0:
        raise ValueError("Value of 'k' must be a non-negative integer.")

    fac1 = factorial(n)
    fac2 = factorial(n-k)

    return fac1 // fac2
