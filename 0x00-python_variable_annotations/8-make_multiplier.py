#!/usr/bin/env python3
"""
takes a float multiplier as argument and returns
a function that multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies its float
    argument by a given multiplier.
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier
    return multiplier_function
