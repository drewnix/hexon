#!/usr/bin/python3
'''
1, 2, 3, 4

* what if characters are not in order i.e.
aaabcca -> = 4a's?

* is adding chars appropriate?
-> no

* if # of chars > then 

aaabbbcc
12312312

a=3
b=3
c=2

algo #1:
if you sort the array then as you iterate over the array you can assign
the end count to a position in an array, i.e. count[3] -> 

       v
aaabbbcc

a = 3
b = 2
c = 1

accum = 2

aaabbc

Time complexity
sort = O(n log(n))
iterate = n

Space complexity
array = size of # uniques
dictionary = size of uniques
Space = O(n^2)


Example 1:

Input: s = "aab"
Output: 0
Explanation: s is already good.
Example 2:

Input: s = "aaabbbcc"
Output: 2
Explanation: You can delete two 'b's resulting in the good string "aaabcc".
Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".
Example 3:

Input: s = "ceabaacb"
Output: 2
Explanation: You can delete both 'c's resulting in the good string "eabaab".
Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).


s = "aaabbbcccc"

'''

from typing import Tuple


class Solution:

    # s -> 'ceabaacb'
    def minDeletions(self, s: str) -> int:
        chars = ''.join(sorted(s)) # -> 'aaabbbccc'
        seen = set() # -> seen = {2, 3}
        char = chars[0] # char -> 'c'
        accum = 0 # 1
        count = 0 # 2

        #         v
        # aaabbbccc

        for i, c in enumerate(chars):
            if c == char:
                count += 1
                if i == len(chars):
                    to_add, not_seen = self.check_backwards(count, seen)
                    print(f"end call char: {c}, char: {char}, to_add: {to_add}, not_seen: {not_seen}, seen: {seen}")
                    accum += to_add
                    seen.add(not_seen)
            else:
                # reached end of list of this set of chars
                if count in seen: # True
                    to_add, not_seen = self.check_backwards(count, seen)
                    print(f"mid call char: {c}, char: {char}, to_add: {to_add}, not_seen: {not_seen}, seen: {seen}")
                    accum += to_add
                    seen.add(not_seen)
                else:
                    seen.add(count)
                    count = 1
                    char = c
        return accum 
    
    def check_backwards(self, num: int, check_set: set) -> Tuple[int, int]:
        to_add = 0
        
        for n in range(num-1, 0, -1):
            to_add += 1
            if n > 0 and n not in check_set:
                return (to_add, n)
        
        return (to_add, 0)

        # for i in range(0, len(chars)+1): # i = 8
        #     print(char)
        #     if chars[i-1] == char and i < len(chars): # True
        #         count += 1
        #     else:
        #         print("count: ", count)
        #         if count in seen: # True
        #             for n in range(count-1, 0, -1):
        #                 accum += 1
        #                 if n > 0 and n not in seen:
        #                     print("num = ", n)
        #                     seen.add(n)
        #                     count = 1
        #                     char = chars[i-1]
        #                     break
        #         else:
        #             seen.add(count)
        #             count = 1
        #             char = chars[i-1]
        # return accum
                
s = Solution()
# print(s.minDeletions('aaabbbc'))
print(s.minDeletions('aaabbbccc'))

