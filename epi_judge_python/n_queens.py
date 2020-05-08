from typing import List

from test_framework import generic_test

def n_queens(n: int) -> List[List[int]]:
    all_placements = []
    def is_valid_upper_diagonal(c, current_placements):
        c, r = c - 1, current_placements[c] - 1
        while c >= 0:
            if current_placements[c] == r:
                return False
            c, r = c - 1, r - 1
        return True

    def is_valid_lower_diagonal(c, current_placements):
        c, r = c - 1, current_placements[c] + 1
        while c >= 0:
            if current_placements[c] == r:
                return False
            c, r = c - 1, r + 1
        return True

    def backtrack(c, current_placements, used_rows):
        if c == n:
            all_placements.append([*current_placements])
            return
        for r in range(n):
            if r in used_rows: continue
            current_placements[c] = r
            if is_valid_lower_diagonal(c, current_placements) and is_valid_upper_diagonal(c, current_placements):
                used_rows.add(r)
                backtrack(c + 1, current_placements, used_rows)
                used_rows.remove(r)
            
            current_placements[c] = None
            
    backtrack(0, [None for _ in range(n)], set())
    return all_placements

def comp(a, b):
    return sorted(a) == sorted(b)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('n_queens.py', 'n_queens.tsv', n_queens,
                                       comp))
