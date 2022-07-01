from typing import List


def trapping_rainwater(heights: List[int]):
    total_water = 0
    max_left, max_right = 0, 0
    i = 0
    j = len(heights)-1

    while i < j:
        if heights[i] <= heights[j]:
            if heights[i] > max_left:
                max_left = heights[i]
            elif heights[i] < max_left:
                total_water += max_left-heights[i]
            i += 1
        elif heights[i] >= heights[j]:
            if heights[j] > max_right:
                max_right = heights[j]
            elif heights[j] < max_right:
                total_water += max_right-heights[j]
            j -= 1

    return total_water


def trapping_rainwater_brute(heights: List[int]):
    total_water = 0
    for i in range(0, len(heights)-1):
        max_r = 0
        max_l = 0
        for left in range(i-1, 0, -1):
            max_l = max(max_l, heights[left])

        for right in range(i, len(heights)):
            max_r = max(max_r, heights[right])

        current_water = min(max_r, max_l)-heights[i]
        if current_water > 0:
            total_water += current_water

    return total_water


"""
 0  1  2  3  4  5  6  7  8  9  10
                   lr i
[0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]

       
if R >= L : a bucket is found
if end of array and 
L will move to location of R
Trapped Water (area) = min(L, R)*(R-L+1)-sum(L+1:R)
Current Water = min(L, R)-arr[i]

2*3=6-2=4


"""

if __name__ == "__main__":
    arr = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]
    # arr = [0, 1, 3, 1, 0, 1, 2, 3, 4, 0]
    print(trapping_rainwater(arr))

