
from arithmetic import *

def to_add(x):
    """Return the sum of all the items in a list"""

    result = sum(x)

    return result

print "this is the result of the sum: ", to_add([1, 2, 3])

def to_subtract(x):
    """ Return the subtraction if all the items in a list"""

    result = int(x.pop(0))

    for i in x:
        result = result - int(i)

    return result

print "this is the result of subtraction: ", to_subtract([2, 3, 6])

def to_divide(x):
    """ Return the division of all the items in a list"""

    result = float(x.pop(0))

    for i in x:
        result = result / i

    return result


print "this is the result of division: ", to_divide([12, 4, 2])

def to_multiply(x):
    """Multiply the items in a list."""

    result = int(x.pop(0))

    for i in x:
        result = result * i

    return result

print "this is the result of Multiply", to_multiply([2, 4, 2])
