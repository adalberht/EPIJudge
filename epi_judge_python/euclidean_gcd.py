from test_framework import generic_test


def gcd(x: int, y: int) -> int:
    if y < x: return gcd(y, x)
    while y > 0:
        x, y = y, x % y
    return x


if __name__ == '__main__':
    exit(generic_test.generic_test_main('euclidean_gcd.py', 'gcd.tsv', gcd))
