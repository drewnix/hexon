from typing import List
from collections import deque

"""
Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: []
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.


"hit"
"hot"
"dot"
"dog"
"cog"



"""

class Solution:
    @staticmethod
    def findNeighbors(word_str: str, word_set: set) -> List[str]:
        word = list(word_str)
        neighbors = []
        for i in range(len(word)):
            old_char = word[i]
            for c in range(ord('a'), ord('z')):
                word[i] = chr(c)
                new_word = ''.join(word)

                if chr(c) == old_char or new_word not in word_set:
                    continue

                print(new_word)
                neighbors.append(new_word)
            word[i] = old_char

        return neighbors

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        """

        :param str beginWord:
        :param str endWord:
        :param List wordList:
        :rtype: List[List[str]]
        """
        edges = set(wordList)
        visited = []
        adj_list = []
        q = deque([beginWord])

        if beginWord in wordList:
            wordList.remove(beginWord)

        while q:
            curr_word = q.popleft()

        print("hello")
        return []


if __name__ == "__main__":
    s = Solution()
    word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
    # wordSet = set(wordList)
    # print(s.findNeighbors("hit", wordSet))
    print(s.findLadders("hit", "cog", wordList=word_list))
