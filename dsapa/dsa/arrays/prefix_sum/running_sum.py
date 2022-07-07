"""

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
 
Constraints:

1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6

"""


from typing import List
from timeit import timeit


class Solution:
    @staticmethod
    def runningSum(self, nums: List[int]) -> List[int]:
        acc = 0

        def sumify(n):
            nonlocal acc
            acc += n
            return acc

        return list(map(sumify, nums))

    @staticmethod
    def runningSumSpace(nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            try:
                res.append(res[-1] + i)
            except IndexError:
                res.append(i)

        return res

    @staticmethod
    def runningSumInput(nums: List[int]) -> List[int]:
        """ time complexity = O(n), space complexity = O(1) """
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]

        return nums


s = Solution()
print(s.runningSumInput([1, 2, 3, 4]))
