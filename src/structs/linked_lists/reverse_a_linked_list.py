"""


"""


from typing import Optional

from algo.utils.linked_list import ListNode, display_list, list_from_array, validate_list


class Solution:
    def __init__(self):
        pass

    @staticmethod
    def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev


def test_case_1():
    ll = list_from_array([1, 2, 3, 4, 5])

    sol = Solution()
    f1 = sol.reverse_list(ll)
    display_list(f1)
    validate_list(f1, [5, 4, 3, 2, 1])


if __name__ == "__main__":
    display_list(list_from_array([1, 2, 3]))
    test_case_1()
