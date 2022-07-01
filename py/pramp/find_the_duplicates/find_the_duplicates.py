import math


def find_the_duplicates_brute(ary1, ary2):
    # time: O(N*M) space: O(N) where N <= M
    dupes = list()

    for i in range(0, len(ary1)):
        for j in range(0, len(ary2)):
            if ary1[i] == ary2[j]:
                dupes.append(ary1[i])

    return dupes


def binary_search(arr, num):
    begin = 0
    end = len(arr) - 1

    while begin <= end:
        mid = begin + math.floor((end - begin) / 2)
        if arr[mid] < num:
            begin = mid + 1
        elif arr[mid] == num:
            return mid
        else:
            end = mid - 1

    return None


def find_the_duplicates_binary_search(ary1, ary2):
    # time: O(N⋅log(N)), space: O(N) where N <= M
    dupes = list()

    for number in ary1:
        if binary_search(ary2, number) is not None:
            dupes.append(number)

    return dupes


def find_the_duplicates(ary1: list, ary2: list) -> list:
    # time: O(N+M) space: O(N) where N <= M
    i = 0
    j = 0
    dupes = list()

    while i < len(ary1) and j < len(ary2):
        if ary1[i] < ary2[j]:
            i += 1
        elif ary2[j] < ary1[i]:
            j += 1
        elif ary1[i] == ary2[j]:
            dupes.append(ary1[i])
            i += 1
            j += 1

    return dupes


if __name__ == "__main__":
    arr1, arr2 = [1, 2, 3, 5, 6, 7], [3, 6, 7, 8, 20]
    print(find_the_duplicates_binary_search(arr1, arr2))
