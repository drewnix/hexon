from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:  # nums = [1,7,3,6,5,6]
        left, right = 0, sum(nums[1:])
        print(f"left: {left}, right: {right}")

        if left == right:
            return 0

        for i in range(1, len(nums)):
            left += nums[i - 1]
            right -= nums[i]
            print(f"left: {left}, right: {right}")

            if left == right:
                return i
            # elif abs(left) > abs(right):
            #     return -1

        return -1

    # def pivotBinary(self, nums: List[int]) -> int:  # nums = [1,7,3,6,5,6]
    #     def search(ary, p, l, r):
    #         if l < r:
    #
    #         elif l > r:
    #
    #     # split the array len(nums)/2
    #     mid = len(nums) // 2
    #
    #     left = sum(nums[:mid])
    #     right = sum(nums[mid+1:])
    #
    #     if left


s = Solution()
print(s.pivotIndex([1, 7, 3, 6, 5, 6]))
# print(s.pivotIndex([-1,-1,-1,-1,-1,0]))
# print(s.pivotIndex([1,2,3]))
# print(s.pivotIndex([2,1,-1]))
