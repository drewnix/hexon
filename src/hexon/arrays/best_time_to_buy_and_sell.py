
"""

min_seen = 7
max_seen = 3
max_prof = 0

 m_a
    a
[7, 5, 3, 6, 4, 2, 8, 1, 2, 6, 7, 10, 5, 10, 8, 2, 3]
                                                   b

lowest_seen = 7
highest_seen = 3
biggest_diff =

5



99

 a
[1,100,2,102,3,110,5,200,3,300,2,4,100]
                                    b

profit = 99
if a < b:
   a += 1

                                             m_b

min_a = 0           # 0
max_b = len(ary)-1  # 14
max_prof = 2
a = 0
b = len(ary)
while a < max_b or b > min_a:
    a += 1
    b -= 1
    if ary[max_b]-ary[a] > max_prof:
        max_prof = ary[max_b]-ary[a]
        min_a = a
    if ary[b]-ary[min_a] > max_prof:
        max_prof = ary[b]-ary[min_a]
        max_b = b





    if ary[a] > max_b or ar:
        a+=1
    if ary[b] > min_a:
        b-=1

    if ary[b]-ary[a] > max_prof:
        max_b = ary[b]
        min_a = ary[a]
        max_prof = ary[b]-ary[a]


                          b


    a     b
[7, 1, 5, 3, 6, 4, 1]




"""

from typing import List
from unittest import TestCase
import pytest
import sys


class Solution:
    def __init__(self):
        pass

    @staticmethod
    def max_profit_n2(prices: List[int]) -> int:
        max_gain = 0
        for i in range(len(prices)):
            for n in range(i, len(prices)):
                diff = prices[n]-prices[i]
                if diff > max_gain:
                    max_gain = diff

        return max_gain

    @staticmethod
    def max_profit_n(prices: List[int]) -> int:
        min_price = prices[0]
        max_gain = 0
        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i])
            max_gain = max(max_gain, prices[i]-min_price)

        return max_gain


class TestCases(TestCase):
    def test_case_1(self):
        sol = Solution()
        prices = [7, 1, 5, 3, 6, 4]
        self.assertEqual(sol.max_profit_n(prices), 5)

    def test_case_2(self):
        sol = Solution()
        prices = [7, 6, 4, 3, 1]
        self.assertEqual(sol.max_profit_n(prices), 0)


if __name__ == "__main__":
    sys.exit(pytest.main())
