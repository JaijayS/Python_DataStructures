from typing import Set, Any


def find_common_method1(list1: list, list2: list) -> set[Any] | int:

    common_elements = set(list1).intersection(set(list2))
    if common_elements:
        return common_elements
    else:
        return -1


def find_common_method2(list1: list, list2: list) -> set[Any]:

    # Simplified by naming convention list1 = a and list2 = b
    a = list1
    b = list2

    # Initialize set c to take like element
    c = set()

    # Iterate through each element in i
    for i in a:
        # if i in b, add to c.
        if i in b:
            c.add(i)

    # Return set
    return c


list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [3, 4, 5, 6, 7, 8, 9]

# print(find_common_method1(list1, list2))
print(find_common_method2(list1, list2))