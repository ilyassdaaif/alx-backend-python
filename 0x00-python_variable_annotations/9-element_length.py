#!/usr/bin/env python3
"""
9-element-length
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples where each tuple contains a
    sequence from lst and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
