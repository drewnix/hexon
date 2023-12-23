"""
1. Problem

1a. Think of Questions

1b. Constraints

1c. Test Cases

2. Approach

2a. Identify Approaches and Data Structures

2b. Think of Big-O Complexity for each approach

2c. Identify Base Case

3. Implementation

4. Code walk through (by hand)

5. Try different inputs and talk through big-O complexity

"""

from typing import List


def number_of_islands(vals: List[int]):
    return vals


"""
m = length(grid) # ylen
n = length(grid[0]) # xlen
visited = [[False]*n]*m
iterate through grid 
if item has been visited 
    continue
if item is not in visited and == 1
    add an "island"
    BFS (or DFS) through grid connected to the "1" 
        for all directions ((0, 1), (1, 0), (-1, 0), (0, -1))
        mark all 4-way connected in visited


Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

    -1
^ -1 * +1 
y   +1
 x >
"""
import numpy as np


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        mlen = len(grid)
        nlen = len(grid[0])
        islands = 0
        visited = np.array([[False] * nlen] * mlen)
        for m in range(0, mlen - 1):
            for n in range(0, nlen - 1):
                print(f"me = grid[{m}][{n}] = {grid[m][n]} visited = {visited[m][n]}")
                if visited[m][n] == True:
                    continue
                if grid[m][n] == "1" and visited[m][n] == False:
                    print(f"new island starting at grid[{m}][{n}]")
                    islands += 1
                    queue = [(m, n)]
                    while queue:
                        i, j = queue.pop()
                        visited[i][j] = True
                        for y, x in ((i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)):
                            if 0 < y < mlen and 0 < x < nlen and grid[y][x] == "1" and visited[y][x] == False:
                                print(f"neighbor grid[{y}][{x}] == {grid[y][x]}")

                                queue.append((y, x))
                                print(queue)
                    print(grid)
                    print(visited)
                    print(islands)
        return islands
