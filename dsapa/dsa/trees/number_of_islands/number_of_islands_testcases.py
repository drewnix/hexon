import pytest
import sys
from unittest import TestCase
from number_of_islands import number_of_islands


class TestCases(TestCase):
    def test_case_1(self):
        ans = number_of_islands([1, 2, 3, 4])
        self.assertEqual(ans, [1, 2, 3, 4])
        print(ans)

    def test_case_2(self):
        ans = number_of_islands([4, 3, 2, 1])
        self.assertEqual(ans, [4, 3, 2, 1])
        print(ans)

    def test_case_3(self):
        ans = number_of_islands([])
        self.assertEqual(ans, [])
        print(ans)


if __name__ == "__main__":
    sys.exit(pytest.main())
