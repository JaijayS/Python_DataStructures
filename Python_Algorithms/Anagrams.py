import re


def anagrams_method_1(word1, word2):

    indices_word1 = {}
    indices_word2 = {}
    word1 = re.sub(r'[^a-z]', '', word1.lower())
    word2 = re.sub(r'[^a-z]', '', word2.lower())

    if len(word1) != len(word2):
        return False

    for i in word1:
        if i in indices_word1:
            indices_word1[i] += 1
        else:
            indices_word1[i] = 1

    for i in word2:
        if i in indices_word2:
            indices_word2[i] += 1
        else:
            indices_word2[i] = 1

    if indices_word1 == indices_word2:
        return True
    return False


def anagrams_method_2(word1, word2):

    word1 = re.sub(r'[^a-z]', '', word1.lower())
    word2 = re.sub(r'[^a-z]', '', word2.lower())

    if len(word1) != len(word2):
        return False

    return sorted(word1) == sorted(word2)


def anagrams_method_3(word1, word2):

    word1 = re.sub(r'[^a-z]', '', word1.lower())
    word2 = re.sub(r'[^a-z]', '', word2.lower())

    if len(word1) != len(word2):
        return False

    words = [list(word1), list(word2)]

    for idx in range(len(words)):
        word = words[idx]

        for i in range(len(word) - 1):
            swapped = False

            # Adjust the range to reduce iterations
            for j in range(len(word) - 1 - i):
                if word[j] > word[j + 1]:
                    # Swap the elements
                    word[j], word[j + 1] = word[j + 1], word[j]
                    swapped = True
            # If no swaps were made, the list is sorted
            if not swapped:
                break

        # Convert the list back to a string
        words[idx] = ''.join(word)

    return words[0] == words[1]


str1 = "hello"
str2 = "world"

str3 = "Astronomer"
str4 = "Moon starer"

print(anagrams_method_1(str1, str2))
print(anagrams_method_1(str3, str4))
print("*" * 40)
print(anagrams_method_2(str1, str2))
print(anagrams_method_2(str3, str4))
print("*" * 40)
print(anagrams_method_3(str1, str2))
print(anagrams_method_3(str3, str4))