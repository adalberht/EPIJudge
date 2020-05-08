from typing import List

from test_framework import generic_test


def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:
    memo = {score:1 for score in individual_play_scores}
    def compute_num_combination_for_final_score(final_score: int):
        if final_score in memo: return memo[final_score]
        
    return compute_num_combination_for_final_score(final_score)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
