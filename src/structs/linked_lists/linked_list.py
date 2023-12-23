class ListNode:
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.val = val


class LinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = ListNode(0)
        self.tail = self.head
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1

        curr = self.head
        for _ in range(index + 1):
            curr = curr.next
        return curr.val

    def add_at_head(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.add_at_index(0, val)

    def add_at_tail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.add_at_index(self.size, val)

    def add_at_index(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.size:
            return

        if index < 0:
            index = 0

        self.size += 1

        node = self.head
        for _ in range(index):
            node = node.next

        to_add = ListNode(val)
        to_add.next = node.next
        node.next = to_add

    def delete_at_index(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """

        if index < 0 or index >= self.size:
            return

        self.size -= 1
        # find predecessor of the node to be deleted
        pred = self.head
        for _ in range(index):
            pred = pred.next

        # delete pred.next
        pred.next = pred.next.next

    def has_cycle(self) -> bool:
        node, runner = self.head, self.head
        run_steps = 2
        while node is not None and runner is not None:
            for _ in range(0, run_steps):
                runner = runner.next
                if runner is None:
                    # we don't have a cycle
                    return False
                if runner is node:
                    # we have a cycle
                    return True
            # move node after runner moves
            node = node.next
        return False

    def detect_cycle_location(self):
        # uses single pointer + set, we can find cycle by tracking all seen in set
        node = self.head
        seen = set()

        while node is not None:
            if node in seen:
                # we've seen this one before... return it
                return node

            seen.add(node)
            node = node.next

        # we've reached end of list, there is no cycle
        return None

    @staticmethod
    def get_intersection_set(head_a, head_b):
        # iterate thru both simultaneously, add both to set
        # when ever either side hits a node that is in the set, that is the solution
        node_a = head_a
        node_b = head_b
        seen = set()

        while node_b is not None:
            seen.add(node_b)
            node_b = node_b.next

        while node_a is not None:
            if node_a in seen:
                return node_a
            node_a = node_a.next

        return None

    def remove_nth_from_end(self, n):
        # this iterates over list to get length first and to calc what to remove
        dummy = ListNode(0)
        dummy.next = self.head
        node = self.head
        length = 0
        while node is not None:
            length += 1
            node = node.next

        length -= n

        node = dummy
        while length > 0:
            length -= 1
            node = node.next

        node.next = node.next.next
        return dummy.next

    def remove_nth_from_end_use_n_step(self, n: int) -> ListNode:
        # time complexity: 0(N), space complexity: O(1)
        # iterate first pointer n steps, then start with second pointer to get to exact location
        dummy = ListNode(0)
        dummy.next = self.head

        step = n
        first = dummy.next
        second = dummy.next

        while step > 0:
            first = first.next
            step -= 1

        while first is not None:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummy.next

    def reverse_list(self):
        if self.head is None:
            return None
        node = self.head
        tail = self.head
        nxt = node.next
        while nxt is not None:
            prev = node
            node = nxt
            nxt = node.next
            node.next = prev

        tail.next = None
        self.head = node
        return self.head

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def odd_even_list(self):
        if self.head is None:
            return None
        head = self.head
        odd, even, even_head = head, head.next, head.next

        while even is not None and even.next is not None:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head
        return head


if __name__ == "__main__":
    l_list = LinkedList()
    l_list.add_at_head(1)
    l_list.add_at_head(12)
    l_list.add_at_head(4)
    l_list.add_at_head(9)

    print(l_list.has_cycle())
    print(l_list.detect_cycle_location())

    # l_list.print()
