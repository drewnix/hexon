from typing import List


def list_to_bin(lst: List[int]) -> int:
    num = 0
    for b in lst:
        num = 2 * num + b
    return num


# [1, 0, 1, 0, 1]
def three_equal_parts(arr: List[int]) -> List[int]:
    n = len(arr)  # 5
    indexes = [i for i in range(n) if arr[i] == 1]  # [0, 2, 4]
    m = len(indexes)

    if m == 0:
        return [0, 2]
    if m % 3 != 0:
        return [-1, -1]

    p1, p2 = indexes[0], indexes[m // 3 - 1]  # p1 = 0, p2 = 0
    p3, p4 = indexes[m // 3], indexes[2 * m // 3 - 1]  # p3 = 2, p4 = 2
    p5, p6 = indexes[2 * m // 3], indexes[-1]  # p5 = 2, p6 = 4
    part1, part2, part3 = arr[p1:p2 + 1], arr[p3:p4 + 1], arr[p5:p6 + 1]

    if part1 != part2 or part2 != part3:
        return [-1, -1]

    l1 = p3 - p2 - 1
    l2 = p5 - p4 - 1
    l3 = n - p6 - 1

    if l3 > l2 or l3 > l1:
        return [-1, -1]

    return [p2 + l3, p4 + l3 + 1]


if __name__ == "__main__":
    print(three_equal_parts([1, 0, 1, 0, 1]))
