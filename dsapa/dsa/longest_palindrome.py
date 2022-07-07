
"""


"""

from typing import List
from unittest import TestCase
import pytest
import sys
import timeit
from line_profiler import line_profiler


def longest_palindrome_optimal(s: str) -> int:
    ans = 0
    d = {}

    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1

    for k, v in d.items():
        ans += v // 2 * 2

    if ans < len(s):
        ans += 1

    return ans


class TestCases(TestCase):
    def test_case_1(self):
        s = "abccccdd"
        self.assertEqual(longest_palindrome_optimal(s), 7)

    def test_case_2(self):
        s = "a"
        self.assertEqual(longest_palindrome_optimal(s), 1)
        timeit.timeit("longest_palindrome_optimal(s)")


if __name__ == "__main__":
    sys.exit(pytest.main())
