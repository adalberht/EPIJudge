from typing import List

from test_framework import generic_test
import heapq

def merge_sorted_arrays_not_pythonic(sorted_arrays: List[List[int]]) -> List[int]:
    sorted_arrays_iter = [iter(arr) for arr in sorted_arrays]
    min_heap = []

    for i, it in enumerate(sorted_arrays_iter):
        first_element = next(it, None)
        if first_element is not None:
            heapq.heappush(min_heap, (first_element, i))
    
    result = []

    while min_heap:
        smallest_element, smallest_index = heapq.heappop(min_heap)
        smallest_array_iter = sorted_arrays_iter[smallest_index]
        next_element = next(smallest_array_iter, None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, smallest_index))
        result.append(smallest_element)
        
    return result

def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
   return list(heapq.merge(*sorted_arrays))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
