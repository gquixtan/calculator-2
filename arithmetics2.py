
def add(x):
    """Return the sum of all the items in a list"""
    result = sum(x)
    print result

add([1, 2, 3])

def subtract(x):
    """ Return the subtraction if all the items in a list"""
    result = x[0]

    for i in x[1:]:
        result -= i

    print result

subtract([5, 3, 1])

