def binary_search_recursive(ary, low, high, num):
    pass


def binary_search(ary, num):
    low = 0
    high = len(ary)
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if ary[mid] < num:
            low = mid + 1

        elif ary[mid] > num:
            high = mid - 1

        else:
            return mid

    return -1


if __name__ == "__main__":
    nums = [1, 3, 4, 5, 7, 9, 10, 17, 25, 35, 50, 61, 73, 88, 89, 90, 92, 100, 124, 126, 130]

    print(binary_search(nums, 33))
