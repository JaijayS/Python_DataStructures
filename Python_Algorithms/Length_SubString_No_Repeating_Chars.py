"""
Problem Statement: Find the Length of the Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring that does not contain any repeating characters.
Input:

    A single string s of length nn, where 0≤n≤1050≤n≤105.
    The string may contain letters, digits, symbols, and spaces.

Output:

    An integer representing the length of the longest substring of s that has no repeating characters.

Examples:

    Input: "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", which has a length of 3.

    Input: "bbbbb"
    Output: 1
    Explanation: The answer is "b", which has a length of 1.

    Input: "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with a length of 3. Note that the answer must be a substring, so "pwke" is not valid.

    Input: ""
    Output: 0
    Explanation: The string is empty, so the result is 0.

Constraints:

    The function should handle edge cases such as:
        Empty string.
        A string with all unique characters.
        A string with all identical characters.
        Long strings for performance evaluation.

Goal:

Design an efficient algorithm with a time complexity of O(n)O(n) to solve the problem for large inputs.
"""


def find_substring(s: str) -> int:
    """
    Problem Statement: Find the Length of the Longest Substring Without Repeating Character.
    - Design an efficient algorithm with a time complexity of O(n).
    1. Define set(), start pointer (start of substring) , max_length of substring
    2. Iterate through s
    3. While s[index] found in set(), shift window right, start shifts right
    4. Else, add s[index] to seen
    5. Compare max_len to index - start.
    6. Return max_length

    :param s: String to be evaluated
    :return: Largest substring of s
    """
    # Initialize set, which creates window for only unique characters
    seen = set()

    # Initialize start pointer and max_length(sub-string length)
    start = 0
    max_len = 0

    # Iterate until end of string
    for end in range(len(s)):

        # If current index is already within the window of seen.
        while s[end] in seen:
            # Remove start until duplicate element is removed
            seen.remove(s[start])
            # Start is +1 index
            start += 1
        # If current index is not already within window, add to seen
        seen.add(s[start])

        # Calculate substring length by comparing max_len to end index - start of substring + 1
        # If longer, the new substring becomes max length
        max_len = max(max_len, end - start + 1)

    # Return max_len
    return max_len

# Test case 1: Regular string with repeating characters
print("Test Case 1: 'abcabcbb'")
print(find_substring("abcabcbb"))

# Test case 2: All unique characters
print("\nTest Case 2: 'abcdef'")
print(find_substring("abcdef"))

# Test case 3: Single character string
print("\nTest Case 3: 'a'")
print(find_substring("a"))

# Test case 4: Empty string
print("\nTest Case 4: ''")
print(find_substring(""))

# Test case 5: String with all repeating characters
print("\nTest Case 5: 'aaaaa'")
print(find_substring("aaaa"))
