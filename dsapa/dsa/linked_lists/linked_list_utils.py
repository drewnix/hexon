from typing import List


class ListNode:
    def __init__(self, val=None):
        self.next = None
        self.val = val


def display_list(node: ListNode) -> None:
    while node is not None:
        if node.next is None:
            print(f"[{node.val}]")
        else:
            print(f"[{node.val}]->", end="")

        node = node.next


def validate_list(list_node: ListNode, ary):
    i = 0

    while list_node is not None:
        if list_node.val != ary[i]:
            print(f"Error: values did not match expected, got: {list_node.val}, expected: {ary[i]}")

        i += 1
        list_node = list_node.next


def list_from_array(ary: List[int]):
    head = ListNode()
    curr = head

    for i in range(len(ary)):
        node = ListNode(val=ary[i])
        curr.next = node
        curr = curr.next

    return head.next