"""



Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false



"abc"


  v vv
"ahbadc"

[ a b c ]




what about aece?

"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:  # "acb", "ahbgdc"
        s_len, t_len = len(s), len(t)
        if t_len < s_len:
            return False
        elif t_len == s_len:
            if t == s:
                return True
            else:
                return False
        elif s == "":
            return True

        s_pos = 0
        for i, c in enumerate(t):
            if s_pos > len(s) - 1:
                return True
            elif c == s[s_pos]:
                s_pos += 1

        if s_pos < len(s):
            return False
        else:
            return True


sol = Solution()
print(sol.isSubsequence("abc", "ahbgdc"))
print(sol.isSubsequence("axc", "ahbgdc"))
print(sol.isSubsequence("", "poop"))
print(sol.isSubsequence("a", "b"))
print(sol.isSubsequence("acb", "ahbgdc"))
print(sol.isSubsequence("b", "abc"))
