from typing import List


def findIndexOfElement(arr: list, element: int | str) -> list | int | str:

    return_elements = []
    for i in range(len(arr)):
        if arr[i] == element:
            return_elements.append(i)

    return return_elements if return_elements else -1


def findIndexOfElementEnumerate(arr: list, element: int | str) -> list:
    return_elements = [i for i, num in enumerate(arr) if num == element]
    return return_elements if return_elements else -1


L = ['a', 'b', 'c', 'a']
T = 'a'

print(f'Index of element {T}: {findIndexOfElement(L, T)}')
print(f'Index of element {T}: {findIndexOfElementEnumerate(L, T)}')