from typing import List

from test_framework import generic_test

from bisect import bisect_left

from math import log2

def intersect_two_sorted_arrays_bisect(A: List[int], B: List[int]) -> List[int]:
    if len(A) > len(B): return intersect_two_sorted_arrays(B, A)
    result = []
    for item in A:
        index_in_b = bisect_left(B, item)
        if index_in_b < len(B) and B[index_in_b] == item:
            if len(result) == 0 or result[-1] != item:
                result.append(item)
    return result

def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    if len(A) > len(B): return intersect_two_sorted_arrays_bisect(B, A)
    if len(A) + len(B) > 0 and len(A) + len(B) > len(A) * log2(len(B)): return intersect_two_sorted_arrays_bisect(A, B)
    result = []
    s1, e1, s2, e2 = 0, len(A), 0, len(B)    
    while s1 < e1 and s2 < e2:
        a, b = A[s1], B[s2]
        if a == b:
            if not result or result[-1] != a: result.append(a)
            else:
                s1 += 1
                s2 += 1
        elif a < b: s1 += 1
        else: s2 += 1

    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
