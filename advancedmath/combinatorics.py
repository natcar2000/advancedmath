def factorial(n):
    validate_values(n)
    
    if n == 0 or n == 1: 
        return 1        
    else:
        return n * factorial(n-1)


def validate_values(n, k=None):
    if type(n) != int:
        raise TypeError("Value(s) must be a integer number.")

    if n < 0:
        raise ValueError("Value(s) must be a non-negative integer.")

    if k is not None:
        if type(k) != int:
            raise TypeError("Value(s) must be a integer number.")   
        if k < 0:
            raise ValueError("Value(s) must be a non-negative integer.")
        if k > n:
            raise ValueError("Value(s) of k must be smaller than or equal to n.")
        
    return True


def permutation(n):
    validate_values(n)
    return factorial(n)


def permutation_with_repetition(n, *repetitions):
    denominator = 1
    soma = 0
    
    for repetition in repetitions:
        validate_values(n, repetition)
        fac = factorial(repetition)
        denominator *= fac
        total_repetitions += repetition

    if total_repetitions > n:
        raise ValueError("The sum of the repetitions can't be greater than n.")
    
    return factorial(n) // denominator


def circular_permutation(n):
    if n == 0:
        raise ValueError("Value of n must be greater than 0.")
        
    validate_values(n)
    
    return factorial(n-1)


def arrangement(n, k):   
    validate_values(n, k)
    return factorial(n) // factorial(n-k)


def combination(n, k):
    validate_values(n, k)
    return factorial(n) // (factorial(k) * factorial(n-k))


def combination_with_repetition(n, k):
    validate_values(n, k)
    
    if n == 0:
        if k == 0:
            return 1
        raise ValueError("Value of n must be greater than 0 when k is greater than 0.")

    return combination(n+k-1, k)
