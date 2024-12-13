def merge_sorted_arrays(
        arr1, arr2):
    # Initialize point for arr1 and arr2
    i = 0
    j = 0

    # Initialize new list for merging
    mergeSort = []

    while i < len(arr1) and j < len(arr2):
        # While index in arr1 is less than index arr2 add it to merge list. Increase index of i
        if arr1[i] < arr2[j]:
            mergeSort.append(arr1[i])
            i += 1
        # If i > j append j to merge list
        else:
            mergeSort.append(arr2[j])
            j += 1
    # If there are values left in list of i. Add them till list is done.
    while i < len(arr1):
        mergeSort.append(arr1[i])
        i += 1
    # If there are values lef tin list of j. Add them till list is done
    while j < len(arr2):
        mergeSort.append(arr2[j])
        j += 1

    # Return new list
    return mergeSort


arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
result = merge_sorted_arrays(arr1, arr2)
print(result)
