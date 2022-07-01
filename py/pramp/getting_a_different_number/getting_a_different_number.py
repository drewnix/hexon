"""
get smallest non-negative NOT in array

Tests:
arr = [0, 1, 2, 3] -> 4
arr = [0, 2, 3, 4] -> 1
arr = [4, 2, 7, 8, 3, 0, 19, 1] -> 5

i = 5
arr[i] = 7
arr = [0, 1, 2, 3, 4, 7, 8, 19]

# if position does not match number in sorted list, then we have a gap
# time: O(N*log(N)), space: O(N)
arr_copy = arr.copy()
arr_copy.sort()
for i, item in enumerate(arr_copy):
    if arr[i] != i:
        return i
return len(arr)+1


i = 5
arr = [4, 2, 7, 8, 3, 0, 19, 1]
nums = {0, 1, 2, 3, 4, 7, 8, 19}
return 5

# use a set to do lookup
# time: O(N), space: O(N)
n = len(arr)
nums = set(arr)

for i in range(0, n-1):
    if i not in nums:
        return arr[i]


n = 7

i = 5
arr[i] = 0
tmp = 0

               i
0 1 2 3 4 5 6  7
               t = 7
0 1 2 3 4 5 19 7

[3, 7, 2, 8, 4, 0, 19, 1] -> 5

# look at index location
# make index location match index by swap
# loop thru and return first item not matching expected

for i in range(0, n-1):
    tmp = arr[i]
    while (tmp < n and arr[tmp] != tmp):
        arr[i], arr[tmp] = arr[tmp], arr[i]

for i in range(0, n-1):
    if arr[i] != i:
        return i

return n

"""


def getting_a_different_number_sort_copy(ary: list) -> int:
    # time: O(N*log(N)) space: O(N)
    n = len(ary)
    ary_copy = ary.copy()
    ary_copy.sort()
    for i in range(0, n - 1):
        if ary_copy[i] != i:
            return i
    return n


def getting_a_different_number_set(ary: list) -> int:
    # time: O(N) space: O(N)
    n = len(ary)
    nums = set(ary)

    for i in range(0, n - 1):
        if i not in nums:
            return i

    return n


def getting_a_different_number_in_place(ary: list) -> int:
    # time: O(N) space: O(1)
    n = len(ary)

    for i in range(0, n - 1):
        tmp = ary[i]
        while n > tmp != ary[tmp]:
            ary[i], ary[tmp] = ary[tmp], ary[i]

    for i in range(0, n - 1):
        if ary[i] != i:
            return i

    return n


if __name__ == "__main__":
    test = [3, 7, 2, 8, 4, 0, 19, 1]
    r = getting_a_different_number_sort_copy(test)
    x = 5
    if r != 5:
        print("error! didn't match, r=%d" % (r))
    else:
        print("matched!")
