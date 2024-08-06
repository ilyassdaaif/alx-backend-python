#!/usr/bin/env python3
"""Module for creating an asyncio.Task from wait_random."""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task for wait_random(max_delay).

    Args:
        max_delay (int): The maximum delay to pass to wait_random.

    Returns:
        asyncio.Task: A Task that will run wait_random(max_delay).
    """
    return asyncio.create_task(wait_random(max_delay))
