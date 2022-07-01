from functools import reduce

# TimeComplexity wiki
# https://wiki.python.org/moin/TimeComplexity


def array_of_array_products_brute(ary: list) -> list:
    res: list = list()
    arr_len = len(ary)

    if arr_len == 0 or arr_len == 1:
        return []

    for i in range(0, len(ary)):
        product = 1
        for j in range(0, len(ary)):
            if i == j:
                continue
            else:
                product *= ary[j]

        res.append(product)

    return res


def array_of_array_products_div(ary: list) -> list:
    res = list()
    arr_len = len(ary)

    if arr_len == 0 or arr_len == 1:
        return []

    product: int = reduce(lambda x, y: x * y, ary)

    for i in ary:
        res.append(product // i)

    return res


def array_of_array_products_calc(ary: list) -> list:
    product_arr = []
    arr_len = len(ary)

    if arr_len == 0 or arr_len == 1:
        return []

    product = 1
    for i in range(0, arr_len):
        product_arr.append(product)
        product *= arr[i]

    product = 1
    for i in range(arr_len - 1, -1, -1):
        product_arr[i] *= product
        product *= arr[i]

    return product_arr


if __name__ == "__main__":
    # arr: list = [8, 10, 2]
    arr: list = [2, 7, 3, 4]
    # result = array_of_array_products_div(arr)
    result = array_of_array_products_calc(arr)
    print(result)
