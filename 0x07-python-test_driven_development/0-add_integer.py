#!usr/bin/python3
"""function that adds 2 integers."""


def add_integer(a, b=98):
    """Return addition of a and b.

        TypeError: If either of a or b is a non-integer and non-float.
    """
    try:
        if not isinstance(a, (int, float)):
            raise TypeError("a must be an integer")
        if not isinstance(b, (int, float)):
            raise TypeError("b must be an integer")

        # Cast a and b to integers if they are floats
        a = int(a) if isinstance(a, float) else a
        b = int(b) if isinstance(b, float) else b

        # Add the integers and return the result
        return a + b
    
    except TypeError as error:
        print("TypeError:", error)
