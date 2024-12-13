
def binary_search(a: list, num: int) -> int:

    # Sort array
    a.sort()
    # Initialize low and high
    low = 0
    # High = length of array - 1
    high = len(a)-1

    # While low is less than or equal to high
    while low <= high:
        # Establish mid
        mid = low + (high - low) // 2
        # If current mid is equal to num return num
        if a[mid] == num:
            return mid
        # If mid is greater than target number
        elif a[mid] < num:
            # Adjust low to be mid + 1
            low = mid + 1
        # If mid is less than target number
        elif a[mid] > num:
            # Adjust high to be mid - 1
            high = mid - 1
    # Return if not found
    return -1


def binary_search_recursive(a: list, num: int, low: int, high: int):
    # Sort array
    a.sort()
    # Base case
    if low > high:
        return -1
    # Define mid
    mid = low + (high - low) // 2

    # if mid == num return mid
    if a[mid] == num:
        return mid

    # If value at mid is greater than number, low stays same, high becomes mid - 1
    elif a[mid] > num:
        return binary_search_recursive(a, num, low, mid - 1)

    # If value at mid is less than number, low becomes mid + 1, high stays same
    else:
        return binary_search_recursive(a, num, mid + 1, high)


nums = [-1, 0, 3, 5, 9, 12]
target = 9

print(binary_search(nums, target))
print(binary_search_recursive(nums, target, 0, len(nums) - 1))
