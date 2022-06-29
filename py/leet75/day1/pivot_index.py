from typing import List

"""

 v
[1,7,3,6,5,6]

l = 0
r = 28

l = 1+p
r = 27-p

if l == r return


[2,1,-1]

l = 0
r = 0 

return



left = [1]
right = [6]


"""


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:  # nums = [1,7,3,6,5,6]
        left = 0  # 11
        right = sum(nums)  # 17

        for i in range(len(nums)):  # 0..6 -> 3
            if left == right:
                return i
            else:
                left += nums[i]
                right -= nums[i]


s = Solution()
print(s.pivotIndex([1,7,3,6,5,6]))
# print(s.pivotIndex([1,2,3]))
# print(s.pivotIndex([2,1,-1]))
