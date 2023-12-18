
"""
1. Problem

1a. Think of Questions

* Can tree have cycles? -> no
* Is it a well formed tree -> yes
* how to keep track at each level?

1b. Constraints

* The number of nodes in the tree is in the range [0, 2000].
* -1000 <= Node.val <= 1000

1c. Test Cases

TestCase #1:
  Input: root = [3,9,20,null,null,15,7]
  Output: [[3],[9,20],[15,7]]

TestCase #2
  Input: root = [1]
  Output: [[1]]

Test Case #3: Empty input
  Input: root = []
  Output: []

2. Approach

2a. Identify Approaches and Data Structures

* Breadth-first search seems appropriate

* Use a deque to store items -> O(1) time complexity for append
     and pop operations vs. O(N) for list

2b. Think of Big-O Complexity for each approach

2c. Identify Base Case

* If empty, just return []

3. Implementation

4. Code walk through (by hand)

5. Try different inputs and talk through big-O complexity


[3,9,20,null,null,15,7] -> [[3], [9,20], [15, 7]]

level = 0

    (3)
   /  \
 (9)  (20)
      /  \
    (15) (7)

[3, 9, 20]

"""

from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#  v
# [3,9,20,null,null,15,7]
# queue = [(0, root)]
# visited = []


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    visited = [[]]  # [[root]]
    q = deque([(0, root)])   # [(1, node_left), (1, node_right]

    for (level, node) in q.popleft():  # level = 0, node = root
        if len(visited)-1 != level:   # False
            visited.append([])

        visited[level].append(node)
        q.extend([(level+1, node.left), (level+1, node.right)])

    return visited


