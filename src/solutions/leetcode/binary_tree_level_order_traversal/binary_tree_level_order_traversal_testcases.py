import sys
from unittest import TestCase

import pytest
from binary_tree_level_order_traversal import binary_tree_level_order_traversal


class TestCases(TestCase):
    def test_case_1(self):
        ans = binary_tree_level_order_traversal([1, 2, 3, 4])
        self.assertEqual(ans, [1, 2, 3, 4])
        print(ans)

    def test_case_2(self):
        ans = binary_tree_level_order_traversal([4, 3, 2, 1])
        self.assertEqual(ans, [4, 3, 2, 1])
        print(ans)

    def test_case_3(self):
        ans = binary_tree_level_order_traversal([])
        self.assertEqual(ans, [])
        print(ans)


if __name__ == "__main__":
    sys.exit(pytest.main())
