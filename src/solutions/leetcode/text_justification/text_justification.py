"""
[x] Determine number of words per line
    [x] How many words can fit within a maxWidth line with a single space?
    [x] tally len(word)
[x] Get amount of whitespace needed (space_needed = maxWidth-chars_length)
[] Identify the number of breaks in the sentance
[] Space per break = space_needed / # of breaks
[] If a line is a single word or this is the last line of text, print all spaces at end

"""
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        n = len(words)
        tally = 0
        result_text = [[]]
        result_index = 0
        for index, word in enumerate(words):
            tally += len(word) + 1
            result_text[result_index].append(word)

            if index < n - 1 and tally + len(words[index + 1]) > maxWidth:
                result_index += 1
                result_text.append([])
                tally = 0
                continue

        for line in result_text:
            needed = sum([len(word) for word in line])
            spaces_needed = maxWidth - needed
            num_breaks = len(line) - 1
            space_per_break = spaces_needed // num_breaks

            print((" " * space_per_break).join(line))

            print(spaces_needed)
            print(num_breaks)
            print(space_per_break)

        print(result_text)


if __name__ == "__main__":
    s = Solution()
    s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
