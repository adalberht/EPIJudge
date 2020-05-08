from typing import List

from test_framework import generic_test

from bisect import bisect_left

def search_first_of_k(A: List[int], k: int) -> int:
    i = bisect_left(A, k)
    return i if i < len(A) and A[i] == k else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
