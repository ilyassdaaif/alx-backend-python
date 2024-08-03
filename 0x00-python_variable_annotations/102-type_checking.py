#!/usr/bin/env python3
"""
This module demonstrates the use of type annotations in Python.
It includes a function that "zooms" a tuple by repeating each element
a specified number of times.

The code has been adjusted to pass type checking, specifically:
- Using Tuple as input and List as output for zoom_array
- Correcting the type of the 'factor' parameter to int
- Ensuring the input 'array' is a tuple, not a list
"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Create a new list with each element of the input tuple
    repeated 'factor' number of times.

    Args:
        lst (Tuple): The input tuple to zoom.
        factor (int): The number of times to repeat each element.
        Defaults to 2.

    Returns:
        List: A new list with zoomed elements.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
