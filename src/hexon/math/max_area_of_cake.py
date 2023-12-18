
"""

"""

from typing import List


class Solution:
    def __init__(self):
        pass

    @staticmethod
    def max_area(h: int, w: int, horizontal_cuts: List[int],
                 vertical_cuts: List[int]) -> int:
        h_arr = [0] + sorted(horizontal_cuts) + [h]
        v_arr = [0] + sorted(vertical_cuts) + [w]
        max_h, max_v = 0, 0

        for i in range(1, len(h_arr)):
            sz = h_arr[i] - h_arr[i - 1]
            if sz > max_h:
                max_h = sz

        for i in range(1, len(v_arr)):
            sz = v_arr[i] - v_arr[i - 1]
            if sz > max_v:
                max_v = sz

        return (max_h * max_v) % (10**9 + 7)


def test_case_1():
    sol = Solution()
    f1 = sol.max_area(5, 4, [1, 2, 4], [1, 3])
    print(f"max_area: {f1}")


def test_case_2():
    sol = Solution()
    f1 = sol.max_area(1000000000, 1000000000, [2], [2])
    print(f"max_area: {f1}")


if __name__ == "__main__":
    test_case_1()
    test_case_2()
