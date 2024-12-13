import re


def isPalindrome(word):

    word = re.sub(r'[^a-z]', '', word.lower())
    return word == word[::-1]


if __name__ == '__main__':
    word = input()
    result = isPalindrome(word)
    print(result)
