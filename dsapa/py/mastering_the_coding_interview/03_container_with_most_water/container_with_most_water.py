

def container_with_most_water(ary):
    i, max_num, j = 0, 0, len(ary)-1

    while i < j:
        res = min(ary[i], ary[j])*(j-i)
        max_num = max(max_num, res)
        if ary[i] <= ary[j]:
            i += 1
        else:
            j -= 1

    return max_num


def container_with_most_water_brute(ary):
    max_num = 0

    for i in range(0, len(ary)):
        for j in range(i+1, len(ary)):
            res = min(ary[i], ary[j])*(j-i)
            max_num = max(max_num, res)

    return max_num


if __name__ == "__main__":
    arr = [4, 8, 1, 2, 3, 9]
    print(container_with_most_water(arr))

