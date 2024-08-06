#!/usr/bin/env python3
"""Module for measuring the runtime of wait_n."""

import asyncio
import time
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay) and returns total_time / n.

    Args:
        n (int): The number of times to call wait_n.
        max_delay (int): The maximum delay to pass to wait_n.

    Returns:
        float: The average time per call.
    """
    start_time = time.time()

    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()
    total_time = end_time - start_time

    return total_time / n


if __name__ == "__main__":
    print(measure_time(5, 9))
