#########################################################
# CODE INSTRUCTIONS:                                    #
# 1) The method findInOrderSuccessor you're asked      #
#    to implement is located at line 30.                #
# 2) Use the helper code below to implement it.         #
# 3) In a nutshell, the helper code allows you to       #
#    to build a Binary Search Tree.                     #
# 4) Jump to line 88 to see an example for how the      #
#    helper code is used to test findInOrderSuccessor.  #
#########################################################


# A node
class Node:
    # Constructor to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


# A binary search tree
class BinarySearchTree:
    # Constructor to create a new BST
    def __init__(self):
        self.root = None

    @staticmethod
    def find_in_order_successor(input_node):
        if input_node.right is not None:
            node = input_node.right
            while node is not None:
                if node.left is None:
                    return node

                node = node.left

        if input_node.right is None:
            node = input_node
            while node is not None:
                prev = node
                node = node.parent
                if node.left == prev:
                    return node

            return None

    # Given a binary search tree and a number, inserts a
    # new node with the given number in the correct place
    # in the tree. Returns the new root pointer which the
    # caller should then use(the standard trick to avoid
    # using reference parameters)
    def insert(self, key):
        # 1) If tree is empty, create the root
        if self.root is None:
            self.root = Node(key)
            return

        # 2) Otherwise, create a node with the key
        #    and traverse down the tree to find where to
        #    to insert the new node
        current_node = self.root
        new_node = Node(key)
        while current_node is not None:
            if key < current_node.key:
                if current_node.left is None:
                    current_node.left = new_node
                    new_node.parent = current_node
                    break
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = new_node
                    new_node.parent = current_node
                    break
                else:
                    current_node = current_node.right

    # Return a reference to a node in the BST by its key.
    # Use this method when you need a node to test your
    # findInOrderSuccessor function on
    def get_node_by_key(self, key):
        current_node = self.root
        while current_node is not None:
            if key == current_node.key:
                return current_node

            if key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right

        return None


if __name__ == "__main__":
    #########################################
    # Driver program to test above function #
    #########################################

    # Create a Binary Search Tree
    bst = BinarySearchTree()
    bst.insert(20)
    bst.insert(9)
    bst.insert(25)
    bst.insert(5)
    bst.insert(12)
    bst.insert(11)
    bst.insert(14)

    # Get a reference to the node whose key is 9
    # test = bst.get_node_by_key(9)
    test = bst.get_node_by_key(14)

    # Find the in order successor of test
    successor = bst.find_in_order_successor(test)

    # Print the key of the successor node
    if successor is not None:
        print("\nInorder Successor of %d is %d " % (test.key, successor.key))
    else:
        print("\nInorder Successor doesn't exist")
