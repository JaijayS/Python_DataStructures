
# Due to the loop, both functions have 0(n) time, based on they each have to iterate through the whole array.
# After one iteration, the dictionary will count all numbers within the array, meaning future queries with be O(1)
# versus Iterative approach where it will be O(n) every query.
def countElements(arr: list, num: int) -> int:

    # Initialize count = 0
    count = 0

    # Iterate through array
    for i in arr:
        # If i == target number, count + 1
        if i == num:
            count += 1
    # Return count at end of loop
    return count


# Use Dict function
def countElementsUsingDict(arr: list, num: int) -> int:
    # Create an empty dictionary to store the counts
    element_counts = {}

    # Loop through the array and count occurrences
    for i in arr:
        if i in element_counts:
            element_counts[i] += 1
        else:
            element_counts[i] = 1

    # Return the count of the target number, or 0 if it's not found
    return element_counts.get(num, 0)


# Test lists
arr1 = [1, 2, 3, 4, 2, 2, 5]
arr2 = [10, 20, 30, 40, 50]

# Target numbers
target1 = 2
target2 = 25


# Built-in Test cases:
print(f'Built-in test - Total {target1} in arr1: {arr1.count(target1)}')
print(f'Built-in test - Total {target2} in arr2: {arr2.count(target2)}')

# Function Test cases:
print(f'Function test- Total {target1} in arr1: {countElements(arr1, target1)}')
print(f'Function test-Total {target2} in arr2: {countElements(arr2, target2)}')

# Dict Function Test
print(f'Function test (Dict) - Total {target1} in arr1: {countElementsUsingDict(arr1, target1)}')
print(f'Function test (Dict) - Total {target2} in arr2: {countElementsUsingDict(arr2, target2)}')