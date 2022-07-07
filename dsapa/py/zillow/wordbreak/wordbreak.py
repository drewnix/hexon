from typing import List


class Solution:
    def word_break(self, s: str, word_dict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        s_len = len(s)
        dp[len(s)] = True

        for i in range(len(s)-1, -1, -1):
            for word in word_dict:
                w_len = len(word)
                if i+w_len <= s_len and s[i:i+w_len] == word:
                    dp[i] = dp[i+w_len]
                if dp[i]:
                    break

        return dp[0]


if __name__ == "__main__":
    sol = Solution()
    test_str = "neetcode"
    test_dict = ["neetc", "neet", "leet", "code"]
    print(sol.word_break(s=test_str, word_dict=test_dict))