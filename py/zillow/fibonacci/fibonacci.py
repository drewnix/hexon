memo = {}


def fib(num):
    if num < 0:
        raise Exception("num must be >= 0")
    if num == 0:
        return 0
    if num == 1:
        return 1

    if num not in memo:
        memo[num] = fib(num - 1) + fib(num - 2)

    return memo[num]


if __name__ == "__main__":
    print(fib(17))
