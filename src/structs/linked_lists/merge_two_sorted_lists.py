"""

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

list1
[2]->[4]


tmp = list1
list1 = list1.next

tmp = [1]


tmp.next = list2.next
list2.next = tmp

list2.next =


[2]->[4]

 v
[1]->[1]->[3]->[4]

[1]->[1]->[2]->[3]->[4]->[4]


"""


#  1
# [3]->[6]
#  2
# [1]->[2]->[4]->[5]->[8]
#
# curr = [1]
from algo.utils.linked_list import ListNode, display_list, list_from_array, validate_list


class Solution:
    def __init__(self):
        pass

    @staticmethod
    def merge_two_lists(list1: ListNode, list2: ListNode) -> ListNode:
        head = ListNode(0)
        tail = head

        while True:
            if list1 is None:
                tail.next = list2
                break
            elif list2 is None:
                tail.next = list1
                break

            if list2.val <= list1.val:
                tail.next = list2
                list2 = list2.next
            else:
                tail.next = list1
                list1 = list1.next

            tail = tail.next

        return head.next


def test_case_1():
    l1 = list_from_array([1, 2, 4])
    l2 = list_from_array([1, 5, 8])

    sol = Solution()
    display_list(l2)
    f1 = sol.merge_two_lists(l1, l2)
    display_list(f1)
    validate_list(f1, [1, 1, 2, 4, 5, 8])


def test_case_2():
    l1 = ListNode(val=1)
    l2 = None

    sol = Solution()
    display_list(l2)
    f1 = sol.merge_two_lists(l1, l2)
    display_list(f1)
    validate_list(f1, [1])


def test_case_3():
    l1 = ListNode(val=2)
    l2 = ListNode(val=1)

    sol = Solution()
    f1 = sol.merge_two_lists(l1, l2)
    display_list(f1)
    validate_list(f1, [1, 2])


if __name__ == "__main__":
    # display_list(list_from_array([1, 2, 3]))
    # test_case_1()
    # test_case_2()
    test_case_3()
