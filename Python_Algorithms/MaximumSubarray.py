def maxSubarraySum(arr):

    # Initialize result
    res = arr[0]

    # Outer loop, keeps track of starting point
    # Each iteration will make next index starting point.
    for i in range(len(arr)):
        # Initialize current sum
        currSum = 0

        # Inner loop, takes starting point and adds next index to sum.
        # If currSum is greater than res, currSum = res
        for j in range(i, len(arr)):
            currSum += arr[j]

            res = max(res, currSum)

    return res


if __name__ == "__main__":
    arr = [2, 3, -8, 7, -1, 2, 3]
    print(maxSubarraySum(arr))  # Calls the function and prints the result
