"""




"""


def check_is_valid(ary, s):
    is_valid = True

    for i in ary:
        if i not in s:
            is_valid = False

    return is_valid


def get_shortest_unique_substring(ary, s):
    m_len = float("inf")
    m_str = ""
    i = 0
    j = 1

    while i <= len(s) and j <= len(s):
        is_valid = check_is_valid(ary, s[i:j])
        if is_valid:
            if len(s[i:j]) < m_len:
                m_str = s[i:j]
                m_len = len(s[i:j])
            i += 1
        else:
            j += 1

    return "".join(m_str), m_len


if __name__ == "__main__":
    arr = ["x", "y", "z"]
    mys = "xyyzyzyx"

    min_str, min_len = get_shortest_unique_substring(arr, mys)
    print(f"min_str: {min_str}, min_len: {min_len}")
