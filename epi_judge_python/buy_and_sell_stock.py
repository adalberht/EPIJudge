from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    mini, maxi = prices[0], prices[0]
    result = 0
    for price in prices:
        if price < mini:
            mini = price
            maxi = price
        elif price > maxi:
            maxi = price
            result = max(result, maxi - mini)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
