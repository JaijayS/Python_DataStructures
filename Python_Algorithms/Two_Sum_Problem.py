def two_Sum(array: list, target_num: int) -> list:
    """

    
    """
    # Declare a for easier us
    a = array
    # Initialize empty list

    # Loop through a with index i
    for i in range(0, len(a)):
        # Loop through j with index j
        for j in range(len(a)):
            # If sum of a[i] and a[j] = target number, and they are not the same indices return i, j
            # Without checking i != j, it will compare the same index of the list with index i, j
            if a[i] + a[j] == target_num and i != j:

                # Return indices i, j
                return [i, j]

    # Return empty list if no target sums are found
    return []


nums = [2, 7, 11, 15]
target = 9
print(two_Sum(nums, target))
# Output: [0,1]

print("*" * 40)
nums = [-3, 4, 3, 90]
target = 0
print(two_Sum(nums, target))
# Output: [0,2]

print("*" * 40)
nums = [1, 2, 3, 4, 5]
target = 10
print(two_Sum(nums, target))
# Output: []

print("*" * 40)
nums = [1, 4]
target = 5
print(two_Sum(nums, target))
# Output: [0, 1]
