#!/usr/bin/env python3
"""takes a list mxd_lst of integers and
floats and returns their sum as a float"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list of integers and floats.

    Returns:
        float: The sum of all numbers in the input list.
    """
    return float(sum(mxd_lst))
