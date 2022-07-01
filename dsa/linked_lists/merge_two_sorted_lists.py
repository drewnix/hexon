
"""

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

l1
[2]->[4]


tmp = l1
l1 = l1.next

tmp = [1]


tmp.next = l2.next
l2.next = tmp

l2.next =


[2]->[4]

 v
[1]->[1]->[3]->[4]













[1]->[1]->[2]->[3]->[4]->[4]


"""

class ListNode:
    def __init__(self, val=None):
        self.next = None
        self.val = val



#  1
# [3]->[6]
#  2
# [1]->[2]->[4]->[5]->[8]
#
# curr = [1]

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        head.next = l2

        while l2 is not None:
            if l1 is None:
                return head.next
            if l2.val <= l1.val:
                if l1.val <= l2.next.val:
                    # save current l1 node
                    curr = l1
                    # advance l1 reference
                    l1 = l1.next
                    # combine and l2
                    curr.next = l2.next
                    # change l2 reference to include curr
                    l2.next = curr
                else:
                    l2 = l2.next
            if l2.val > l1.val:
                curr = l1
                l1 = l1.next
                curr.next = l2
                l2 = curr


list1 = ListNode(val=1)
list1.next = ListNode(val=2)
list1.next.next = ListNode(val=4)

list2 = ListNode(val=1)
list2.next = ListNode(val=5)
list2.next.next = ListNode(val=8)


sol = Solution()
print(sol.mergeTwoLists(list1, list2))
