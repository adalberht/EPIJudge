from typing import List

from test_framework import generic_test, test_utils


def generate_power_set(input_set: List[int]) -> List[List[int]]:
    if len(input_set) == 0: return [[]]
    def generate(i, bit_masks):
        if i == len(input_set):
            power_set.append([element for index, element in enumerate(input_set) if bit_masks[index]])
            return
        bit_masks[i] = False
        generate(i + 1, bit_masks)

        bit_masks[i] = True
        generate(i + 1, bit_masks)

    power_set = []
    generate(0, [False for _ in input_set])
    return power_set


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('power_set.py', 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
