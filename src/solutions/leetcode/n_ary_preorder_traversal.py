"""


"""

import sys
from typing import List, Union
from unittest import TestCase

import pytest
from pptree import print_tree


class Node:
    def __init__(self, name, val, children=None):
        if children is None:
            children = []
        self.name = name
        self.val = val
        self.children = children


def create_tree(values: List[int]):
    level = 0
    tree_vals = [[]]

    for i in values:
        if i is None:
            level += 1
            tree_vals.append([])
            continue

        tree_vals[level].append(i)

    root = Node("1", 1)
    root.children = [Node("3", 3), Node("2", 2), Node("4", 4)]
    root.children[0].children = [Node("5", 5), Node("6", 6)]

    return root


def preorder(root: "Node") -> List[int]:
    if root is not None:
        ans = [root.val]
    else:
        return []

    for i in root.children:
        ans.extend(preorder(i))

    return ans


class TestCases(TestCase):
    def test_case_1(self):
        root = create_tree([1, None, 3, 2, 4, None, 5, 6])
        print_tree(root, childattr="children", nameattr="name", horizontal=True)
        ans = preorder(root)
        self.assertEqual(ans, [1, 3, 5, 6, 2, 4])
        print(ans)

    # def test_case_2(self):
    #     root = create_tree([1,None,2,3,4,5,None,None,6,7,None,8,None,9,10,None,
    #                         None,11,None,12,None,13,None,None,14])
    #     ans = preorder(root)
    #     print(ans)

    def test_case_3(self):
        root = None
        ans = preorder(root)
        print(ans)


if __name__ == "__main__":
    sys.exit(pytest.main())
