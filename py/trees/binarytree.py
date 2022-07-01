from typing import List


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root_val):
        self.root = TreeNode(root_val)

    def root_insert(self, val):
        return self.insert(self.root, val)

    def insert(self, root, val):
        if root is None:
            return TreeNode(val)
        else:
            if root.val == val:
                return root
            elif root.val < val:
                root.right = self.insert(root.right, val)
            else:
                root.left = self.insert(root.left, val)

        return root

    def preorder_traversal(self) -> List[int]:
        # time: O(N) N = # of nodes, space: O(N)
        if self.root is None:
            return []

        stack, output = [
            self.root,
        ], []
        while stack:
            root = stack.pop()
            if root is not None:
                output.append(root.val)
                if root.right is not None:
                    stack.append(root.right)
                if root.left is not None:
                    stack.append(root.left)

        return output

    def inorder_traversal(self) -> List[int]:
        # time: O(N) N = # of nodes, space: O(N)
        if self.root is None:
            return []

        stack, output = [
            self.root,
        ], []
        while stack:
            root = stack.pop()
            if root is not None:
                if root.right is not None:
                    stack.append(root.right)
                output.append(root.val)
                if root.left is not None:
                    stack.append(root.left)

        return output


if __name__ == "__main__":
    # bt = BinaryTree(32)
    # bt.root_insert(5)
    # bt.root_insert(100)
    # bt.root_insert(31)
    # bt.root_insert(77)
    # bt.root_insert(90)
    # bt.root_insert(22)
    # bt.root_insert(1000)
    # bt.root_insert(54)
    bt = BinaryTree(1)
    bt.root_insert(2)
    bt.root_insert(3)

    print(bt.preorder_traversal())
