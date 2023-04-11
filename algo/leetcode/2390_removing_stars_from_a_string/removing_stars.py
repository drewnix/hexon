#!/usr/bin/env python


class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] == '*':
                stack.pop()
                continue
            else:
                stack.append(s[i])

        return str("".join(stack))


if __name__ == "__main__":
    s = Solution()
    print(f"removeStars('leet**cod*e'): {s.removeStars('leet**cod*e')}")
    print(f"removeStars('erase*****'): {s.removeStars('erase*****')}")



