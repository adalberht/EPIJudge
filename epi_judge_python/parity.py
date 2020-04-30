from test_framework import generic_test

LOOKUP_TABLE = []

def build_lookup_table():
    for i in range(2 ** 16):
        LOOKUP_TABLE.append(parity_optimized(i))

def parity_brute_force(x: int) -> int:
    count = 0
    while x:
        if x & 1:
            count += 1
        x >>= 1
    return count % 2

def parity_optimized(x: int) -> int:
    result = 0
    while x:
        result ^= 1
        x = x & (x - 1)
    return result

def parity_look_up(x: int) -> int:
    BITMASK = 0xFFFF
    result = 0
    for w in range(4):
        index = x >> w*16
        if w != 3:
            index = index & BITMASK
        result ^= LOOKUP_TABLE[index]
    return result

def parity(x: int) -> int:
    return parity_look_up(x)


if __name__ == '__main__':
    build_lookup_table()
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
