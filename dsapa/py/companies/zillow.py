import random
import timeit
from datetime import timedelta


def find_longest_subsequence(input_list):  # [1, 1, 0, 1]
    if not input_list:
        return None

    if len(input_list) < 2:
        return input_list[0]

    found_item = None
    max_seen = 0

    for i in input_list:  # O(N)
        tally, j = 1, i + 1
        current_item = input_list[i]
        while input_list[j] == current_item:
            tally += 1
            j += 1

        if tally >= max_seen:
            found_item = current_item
        max_seen = max(max_seen, tally)

    return found_item, max_seen


if __name__ == "__main__":
    sequence = [random.randint(0, 9) for i in range(0, 10000000)]
    start = timeit.timeit()
    print(find_longest_subsequence(sequence))
    end = timeit.timeit()
    print(timedelta(seconds=end-start))

