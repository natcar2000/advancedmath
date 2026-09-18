def factorial(n):
    if n == 0 or n == 1: 
        return 1        
    else:
        return n * factorial(n-1)


def validate_values(n, k):
    if type(n) != int:
        raise TypeError("Value must be a integer number.")
        
    if n < 0:
        raise ValueError("Value must be a non-negative integer.")
    
    if k > n:
        raise ValueError("Value of k must be smaller than n.")
        
    return True


def permutation(n):
    return factorial(n)


def permutation_with_repetition(n, *repetitions):
    denominator = 1
    soma = 0
    
    for repetition in repetitions:
        validate_values(n, repetition)
        fac = factorial(repetition)
        denominator *= fac
        soma += repetition

    if soma > n:
        raise ValueError("The sum of the repetitions can't be greater than n.")
    
    return factorial(n) // denominator


def circular_permutation(n):
    return factorial(n-1)


def arrangement(n, k):   
    validate_values(n, k)
    return factorial(n) // factorial(n-k)


def combination(n, k):
    validate_values(n, k)
    return factorial(n) // (factorial(k) * factorial(n-k))


def combination_with_repetition(n, k):
    validate_subset(n, k)
    return combination(n+k-1, k)
