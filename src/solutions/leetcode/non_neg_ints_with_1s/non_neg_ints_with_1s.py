"""
Given a positive integer n, return the number of the integers in the range [0, n] whose binary representations do not contain consecutive ones.

Example 1:

Input: n = 5
Output: 5
Explanation:
Here are the non-negative integers <= 5 with their corresponding binary representations:
0 : 0
1 : 1
2 : 10
3 : 11
4 : 100
5 : 101
Among them, only integer 3 disobeys the rule (two consecutive ones) and the other 5 satisfy the rule.
Example 2:

Input: n = 1
Output: 2
Example 3:

Input: n = 2
Output: 3

Constraints:

1 <= n <= 109
"""


class Solution:
    def findIntegers(self, n: int) -> int:
        non_ones = n + 1
        for i in range(0, n + 1):
            binary = bin(i)[2:]
            if "11" in binary:
                non_ones -= 1

        return non_ones

    def findIntegers2(self, n: int) -> int:
        num_ones = n + 1
        # for i in range(0, n+1):
        while n != 0:
            b = n
            last = 0
            while b:
                j = b % 2
                if j == 1 and last == 1:
                    num_ones -= 1
                    break
                last = j
                b = b // 2
            n -= 1

        return num_ones

        #
        # non_ones = n+1
        # for i in range(0, n+1):
        #     binary = bin(i)[2:]
        #     if '11' in binary:
        #         non_ones -= 1
        #
        # return non_ones


if __name__ == "__main__":
    num = 20
    s = Solution()
    print(s.findIntegers2(num))
