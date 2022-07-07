"""


if node.children = []:
   return node.cost

lowest_seen = float("inf")

for i in range(0, node.children-1):
   child_cost = get_cheapest_cost(node)
   if child_cost < lowest_seen:
      loowest_seen = child_cost

return node.cost+lowest_seen


"""


def get_cheapest_cost(node):
    if len(node.children) == 0:
        return node.cost

    lowest_seen = float("inf")

    for i in range(0, len(node.children)):
        child_cost = get_cheapest_cost(node.children[i])
        if child_cost < lowest_seen:
            lowest_seen = child_cost

    return node.cost + lowest_seen


##########################################
# Use the helper code below to implement #
# and test your function above           #
##########################################

# A node
class Node:

    # Constructor to create a new node
    def __init__(self, cost):
        self.cost = cost
        self.children = []
        self.parent = None


if __name__ == "__main__":
    root = Node(0)
    root.children.extend([Node(5), Node(3), Node(6)])
    root.children[0].children.append(Node(4))
    root.children[1].children.extend([Node(2), Node(0)])
    root.children[2].children.extend([Node(1), Node(5)])
    root.children[1].children[0].children.append(Node(1))
    root.children[1].children[1].children.append(Node(10))
    root.children[1].children[0].children[0].children.append(Node(1))

    cost = get_cheapest_cost(root)
    print(cost)
