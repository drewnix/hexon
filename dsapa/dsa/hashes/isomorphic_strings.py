"""

if strings are different lengths, return false

smap = []
lmap = []
for i in range(0, len(s)):


chr = 97


Input: s = "egg", t = "add"
Output: true


"egg" -> "011"
"add" -> "011"


   v
"foo" -> "011"
"bar" -> "012"

"paper" -> "01023"
"title" -> "01023"

 v
"paper"
"title"

{
 'p' -> 0
}
{
 't' -> 0
}

"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_len, t_len = len(s), len(t)
        if s_len != t_len:
            return False
        smap, tmap = {}, {}
        map_val = 0
        for i in range(0, s_len):
            if s[i] not in smap and t[i] not in tmap:
                smap[s[i]] = map_val
                tmap[t[i]] = map_val
                map_val += 1

            elif s[i] in smap and t[i] in tmap:
                if smap[s[i]] != tmap[t[i]]:
                    return False
                else:
                    continue

            else:
                return False

        return True

    def isIso(self, s: str, t: str) -> bool:  # "foo", "baraa"
        map_s_t = {}  # s_t = {'f': 'b'}
        map_t_s = {}  # t_s = {}

        for c1, c2 in zip(s, t):   # c1 = 'f', c2 = 'b'
            mc2 = map_s_t.setdefault(c1, c2)
            mc1 = map_t_s.setdefault(c2, c1)
            if mc2 != c2 or mc1 != c1:
                return False
            else:
                continue

        return True


s = Solution()
print(s.isIso("egg", "add"))
print(s.isIso("foo", "bar"))
