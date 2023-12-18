

"""

Possible solutions:
* Create an set of seen nodes, check if curr.next is in seen, if it is, return its pos in list
    * Time complexity: O(N) -> we would span full list
    * Space complexity: O(N) -> we would have to store every node in the list


seen = []

"""


from algo.utils.linked_list import (
    ListNode, list_from_array_with_cycle, list_from_array
)
from typing import Optional


class Solution:
    def __init__(self):
        pass

    @staticmethod
    def detect_cycle(head: Optional[ListNode]) -> int:
        node = head
        seen: list[ListNode] = []

        while node is not None:
            for i, n in enumerate(seen):
                if node == n:
                    return i

            seen.append(node)
            node = node.next

        return -1

    @staticmethod
    def detect_cycle_return_node(self, head: ListNode) -> ListNode:
        node = head
        seen = set()

        while node is not None:
            if node in seen:
                # we've seen this one before... return it
                return node

            seen.add(node)
            node = node.next


def test_case_1():
    ll = list_from_array_with_cycle([3, 2, 0, -4], 1)

    sol = Solution()
    f1 = sol.detect_cycle(ll)
    print(f"There is a cycle where tail connects to the {f1} node")


def test_case_2():
    ll = list_from_array_with_cycle([1, 2], 0)

    sol = Solution()
    f1 = sol.detect_cycle(ll)
    print(f"There is a cycle where tail connects to the {f1} node")


def test_case_3():
    ll = list_from_array([1])

    sol = Solution()
    f1 = sol.detect_cycle(ll)
    print(f"There is a cycle where tail connects to the {f1} node")


if __name__ == "__main__":
    test_case_1()
    test_case_2()
    test_case_3()
