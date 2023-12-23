# https://leetcode.com/problems/sort-colors/
# https://youtu.be/oaVa-9wmpns

"""
Dutch National Flag Algorithm:
Use 3 pointers named low, mid, and high to move 0s to the left and 
2s to the right and 1s in the middle of the array and hence the array will be sorted.

iterate thru array, if curr = 0

[1, 2, 0, 0, 2, 1, 0, 2, 0, 1, 0, 2] 

low = 0
mid = 1
high = 10

    v                          h
[0, 1, 0, 2, 1, 0, 2, 0, 1, 0, 2, 2] 
 0  1  2  3  4  5  6  7  8  9 10 11

"""

from typing import Int, List

array = [0, 1, 2, 0, 2, 1, 0, 2, 0, 1, 0, 2]


def sort_array_0_to_2(arr: List[Int]) -> None:
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1

        elif arr[mid] == 2:
            arr[high], arr[mid] = arr[mid], arr[high]
            arr.insert(high, 2)
            high -= 1

        else:
            mid += 1
