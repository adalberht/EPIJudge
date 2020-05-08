from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    is_negative = False
    if x < 0:
        is_negative = True
        x = -x
    result = [] if x > 0 else ['0']

    while x:
        result.append(chr(ord('0') + x % 10))
        x //= 10

    return ('-' if is_negative else '') + ''.join(reversed(result))


def string_to_int(s: str) -> int:
    is_negative = s[0] == '-'
    start = 1 if is_negative else 0
    if s[0] == '+': start += 1

    result = 0
    for i in range(start, len(s)):
        result = (result * 10) + ord(s[i]) - ord('0')
    return result if not is_negative else result * -1


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
