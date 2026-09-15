from advancedmath.arithmetic import factorial

# Normal cases
assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(5) == 120
assert factorial(10) == 3628800


# Invalid input: negative number
try:
    factorial(-1)
except ValueError:
    pass
else:
    raise AssertionError("factorial(-1) should raise ValueError")


# Invalid input: incorrect type
try:
    factorial(3.5)
except TypeError:
    pass
else:
    raise AssertionError("factorial(3.5) should raise TypeError")


print("All tests passed!")
