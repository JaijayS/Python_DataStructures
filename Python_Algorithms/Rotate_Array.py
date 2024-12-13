

def rotate_array(a: list, n: int) -> list:
    """
    Rotate an array by n steps to the right.
    -
    :param a:Array to be rotated
    :param n: Iterations of rotation
    :return: Array after rotation
    """

    # Array rotated
    a_r = []

    # N rotations in case n > len(a). Add one for n to be n elements from right. In this case 5. for 1,2,3,4,5,6,7
    n = (n % len(a)) + 1

    # Iterate through a starting at index n
    for i in range(n, len(a)):
        # Add a[i] to a_r
        a_r.append(a[i])
    # Iterate through a until reach n. Get values before rotation
    for j in range(n):
        # Add a[j] to a_r
        a_r.append(a[j])

    # Return rotated array
    return a_r


arr = [1, 2, 3, 4, 5, 6, 7]
rotate = 3
print(rotate_array(arr, rotate))


