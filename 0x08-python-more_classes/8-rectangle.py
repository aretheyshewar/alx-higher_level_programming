#!/usr/bin/python3
"""
Defines a Rectangle class.
"""


class Rectangle:
    """Rectangle class defined by width and height.
    Attributes:
        number_of_instances: number of Rectangle instances,
        increments with every instantitation,
        decrements with every deletion
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance.
        Args:
            width: width of the rectangle
            height: height of the rectangle

