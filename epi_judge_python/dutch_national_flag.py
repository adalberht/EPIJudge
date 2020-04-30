import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)

def dutch_flag_partition_with_additional_memory(pivot_index: int, A: List[int]) -> None:
    pivot = A[pivot_index]
    less_elements, greater_elements = [], []
    count_pivot = 0
    for item in A:
        if item < pivot: less_elements.append(item)
        elif item == pivot: count_pivot += 1
        else: greater_elements.append(item)

    cur = 0
    def fill(elements: list):
        nonlocal cur
        for item in elements:
            A[cur] = item
            cur += 1
    
    fill(less_elements)
    fill([pivot for _ in range(count_pivot)])
    fill(greater_elements)

def dutch_flag_partition_single_pass(pivot_index: int, A: List[int]) -> None:
    pivot = A[pivot_index]
    smaller, equal, larger = 0, 0, len(A) - 1
    while equal <= larger:
        if A[equal] < pivot:
            # Swap A[equal] and A[smaller]
            A[equal], A[smaller] = A[smaller], A[equal]
            equal += 1
            smaller += 1
        elif A[equal] == pivot:
            equal += 1
        else:
            A[larger], A[equal] = A[equal], A[larger]
            larger -= 1

def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    pivot = A[pivot_index]
    lo = 0
    # Group Small Elements first
    for i in range(len(A)):
        if A[i] < pivot:
            A[lo], A[i] = A[i], A[lo]
            lo += 1
    
    for i in range(lo, len(A)):
        if A[i] == pivot:
            A[lo], A[i] = A[i], A[lo]
            lo += 1
            


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
