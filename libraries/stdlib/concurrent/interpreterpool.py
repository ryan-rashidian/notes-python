"""Demonstration of InterpreterPoolExecutor implemented in Python 3.14

The InterpreterPoolExecutor calls a pool of interpreters asychronously.
It is a ThreadPoolExecutor subclass.

Each worker runs on its own thread, with its own interpreter.

Each interpreter has its own GIL, so code runs unblocked on each CPU
core, offering multi-core parallelism in Python.
"""

import math
import os
import time

from concurrent.futures import InterpreterPoolExecutor, as_completed

cores = os.cpu_count()


def process() -> float:
    """Simulate heavy processing."""
    start = time.perf_counter()
    results = []
    for i in range(1000, 12000):
        results.append(math.factorial(i))
    end = time.perf_counter()
    return end - start


def process_with_pool() -> float:
    """Simulate heavy processing with InterpreterPoolExecutor."""
    start = time.perf_counter()
    results = []
    with InterpreterPoolExecutor(max_workers=cores) as executor:
        workers = [
            executor.submit(math.factorial, i)
            for i in range(1000, 12000)
        ]
        for worker in as_completed(workers):
            results.append(worker.result())
    end = time.perf_counter()
    return end - start


if __name__ == '__main__':
    try:
        print('Demonstration of InterpreterPoolExecutor.\n')
        print(f'Processing data using pool of {cores} workers...')
        timer_pool = process_with_pool()
        print(f'Timer: {timer_pool:.2f} seconds')

        print('Processing data using single interpreter...')
        timer_without = process()
        print(f'Timer: {timer_without:.2f} seconds')

    except KeyboardInterrupt:
        print('\nExit demonstration.')

