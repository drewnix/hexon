"""

Use a runner to step twice as many steps, when runner hits end, our walker
should be halfway there.


[1, 2, 3, 4, 5]

[1, 2, 3, 4, 5, 6]


ary=
[1, 2, 3, 4, 5]

"""


from typing import Optional

from algo.utils.linked_list import ListNode, display_list, list_from_array, validate_list


class Solution:
    def __init__(self):
        pass

    @staticmethod
    def middle_of_list_runner(head: Optional[ListNode]) -> Optional[ListNode]:
        # time complexity = O(N)
        # space complexity = O(1)
        walker = runner = head

        while runner and runner.next is not None:
            walker = walker.next
            runner = runner.next.next

        return walker

    @staticmethod
    def middle_of_list_array(head: Optional[ListNode]) -> Optional[ListNode]:
        # time complexity = O(N)
        # space complexity = O(N)
        ary = [head]

        while ary[-1].next:
            ary.append(ary[-1].next)

        return ary[len(ary) // 2]


def test_case_1():
    ll = list_from_array([1, 2, 3, 4, 5])

    sol = Solution()
    f1 = sol.middle_of_list_array(ll)
    display_list(f1)
    validate_list(f1, [3, 4, 5])


def test_case_2():
    ll = list_from_array([1, 2, 3, 4, 5, 6])

    sol = Solution()
    f1 = sol.middle_of_list_array(ll)
    display_list(f1)
    validate_list(f1, [4, 5, 6])


if __name__ == "__main__":
    test_case_1()
    test_case_2()
