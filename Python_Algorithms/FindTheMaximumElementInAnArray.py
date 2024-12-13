arr = [1, 22, 3, 43, 51, 6, 7]

# Using Built-in function
print("Python Built-in Function")
print(f'Max number: {max(arr)}')

print("Python Custom Method")
# Initialize maxNum to first index
maxNum = arr[0]

# Iterate through all elements
for i in range(1, len(arr)):
    # If current index > maxNum, maxNum = currentIndex
    if arr[i] > maxNum:
        maxNum = arr[i]

print(f'Max number: {maxNum}')
