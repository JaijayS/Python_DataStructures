def findMissingNumber(a: list) -> int:
    """Find the missing element in an array by defining max(a). max(a) multiplied by max(n) + 1 // 2 will provide
     expected sum for array of length max(a). Compare this to sum of actual (a) and find the difference provides the
     missing element

     :arg a: an array or list
     :return: the missing number in array"""
    b = max(a)
    c = (b * (b + 1) // 2)
    d = sum(a)

    missing_number = c - d
    return missing_number


def findMissingNumberXOR(a: list) -> int:
    """ Find the missing element via XOR, which is a binary operation that compares two bits.
    The function compares the expected array based on max(a) and compares it to actual (a).

    - This method is independent of order
    - Runs O(n) because each iteration only has to run once
    - Only works with 1 number missing with no extra numbers outside expected range.

    :arg a: The expected array.
    :return b: The missing element."""

    # Define the array with missing element without max (another method)
    # Length of a = max value - 1, so add one element for what it should be
    n = len(a) + 1

    # Initialize xor_expected & xor_actual
    xor_expected = 0
    xor_actual = 0

    # Iterate through array. Calculate XOR
    for i in range(1, n + 1):
        xor_expected ^= i

    # Initialize XOR Actual = 0
    xor_actual = 0
    for i in a:
        xor_actual ^= i

    missing_number = xor_expected ^ xor_actual

    return missing_number


# Test example
arr = [1, 2, 3, 4, 6, 7, 8]

print(f'Missing Number: {findMissingNumber(arr)}')
print(f'Missing Number XOR: {findMissingNumberXOR(arr)}')
