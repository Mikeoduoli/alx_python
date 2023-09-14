#!/usr/bin/python3
"""
Module contains the definition of class Square that inherits from Rectangle.
"""

Rectangle = __import__('7-rectangle').Rectangle  # Import Rectangle class
# Import integer_validator function
integer_validator = __import__('7-base_geometry').integer_validator


class Square(Rectangle):
    """
    Square class inherits from Rectangle and represents a square shape.
    """

    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square's sides.

        Raises:
            ValueError: If size is not a positive integer.
        """
        integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__width * self.__height
