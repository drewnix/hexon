"""

* median of the two sorted arrays

T=O(log (m+n))

binary search?
combine the two arrays
median = middle value think you must combine them 
but if you know the length you can just pull len()/2 right?

nums1 = [1,3,4,6,7,9,10,14,58,|90,102,115,134,154] (13)
nums2 =          [2,7,9,11,55,|89,101] (7)

13+7=20 median would be 10 when ordered


X X X|X X X
  Y Y|Y Y

rShort = 2
mid = 10 / 2 = 5
rLong = 5 - 2 = 3


X X X|X X X
  Y Y|Y Y
"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def get_val(arr, i):
            if i <= -1:
                return float("-inf")
            if i >= len(arr):
                return float("inf")
            else:
                return arr[int(i)]

        def get_indices(partition_short, list_short, list_long):
            mid = (len(list_short) + len(list_long)) / 2
            partition_long = mid - partition_short
            return partition_short - 1, partition_short, partition_long - 1, partition_long

        def get_direction(left_short, right_short, left_long, right_long, list_short, list_long):
            if get_val(list_short, left_short) > get_val(list_long, right_long):
                return -1
            elif get_val(list_long, left_long) > get_val(list_short, right_short):
                return 1
            else:
                return 0

        def get_result(left_short, right_short, left_long, right_long, list_short, list_long):
            odd = (len(list_short) + len(list_long)) % 2
            if odd:
                return min(get_val(list_long, right_long), get_val(list_short, right_short))
            else:
                return (max(get_val(list_short, left_short), get_val(list_long, left_long)) +
                        min(get_val(list_short, right_short), get_val(list_long, right_long))) / 2.0

        a_long = nums1
        a_short = nums2

        if len(nums2) > len(nums1):
            a_long = nums2
            a_short = nums1

        l_short = r_short = l_long = r_long = d = 1
        l = 0
        r = len(a_short)

        while d != 0:
            m = l + (r - l) / 2
            l_short, r_short, l_long, r_long = get_indices(m, a_short, a_long)
            d = get_direction(l_short, r_short, l_long, r_long, a_short, a_long)
            if d < 0:
                r = m - 1
            elif d > 0:
                l = m + 1

        return get_result(l_short, r_short, l_long, r_long, a_short, a_long)


if __name__ == "__main__":
    s = Solution()
    # n1 = [1, 3, 4, 6, 7, 9, 10, 14, 58, 90, 102, 115, 134, 154]
    # n2 = [2, 7, 9, 11, 55, 89, 101]

    # failing cases...
    n1 = [1, 2, 2]
    n2 = [1, 2, 3]
    print(s.findMedianSortedArrays(n1, n2))
