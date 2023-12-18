from typing import List


def get_max_additional_diners_count(N: int, K: int, M: int, S: List[int]) -> int:
    # Write your code here
    num_seats = 0
    for i in range(1, N):
        can_sit = True
        for j in S:
            if j - K <= i <= j + K:
                can_sit = False
        if can_sit:
            num_seats += 1
            S.append(i)

    return num_seats


if __name__ == "__main__":
    print(get_max_additional_diners_count(10, 1, 2, [2, 6]))