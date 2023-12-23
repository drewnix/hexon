"""

input:  x = 7, n = 3
output: 1.913

input:  x = 9, n = 2
output: 3

3**2
1.193**3
3+3+3=9
3 root of 9
0.5 *0.5 = 0.25
0, 1 = nth < number
number > 1 - numbner > nth
x = 1
n = 2
[0, 1, 2, 3, 4, 5, 6, 7, 8 9] = target = nth root of 9
 L                         R
n = 2
x = 9
nth root = 3


[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
 L                          R
https://www.geeksforgeeks.org/n-th-root-number/
"""


def root(x, n):
    if x == 0:
        return 1

    start = 0
    end = max(1, x)
    approx = (end + start) / 2

    while approx - start >= 0.001:
        if approx**n > x:
            e = approx
        elif approx**n < x:
            s = approx
        else:
            break

        approx = (end + start) / 2

    return approx


if __name__ == "__main__":
    r = root(9, 2)
    print(r)
