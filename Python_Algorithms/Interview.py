def find_substring(s):

    seen = set()
    start = 0
    max_len = 0

    print(set(s))
    if len(s) < 1:
        return -1

    if len(s) == 1:
        return 1

    if len(set(s)) == 1:
        return 1

    for i in range(len(s)):

        while s[i] in seen:
            seen.remove(s[start])
            start += 1

        seen.add(s[i])

        max_len = max(max_len, i - start + 1)
    print(seen)
    return max_len


input_string = "abcabcbb"
print(find_substring(input_string))
input_string = "abcdef"
print(find_substring(input_string))
input_string = "bbbbb"
print(find_substring(input_string))
input_string = "pwwkew"
print(find_substring(input_string))