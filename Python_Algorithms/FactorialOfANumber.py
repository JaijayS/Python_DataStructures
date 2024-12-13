
def factorial_iteration(n):

    # Define the sum
    result = 1
    # Create a loop, starting at 1 until n + 1: 5
    for i in range(1, n+1):
        # Calculate sum each iteration
        result *= i
    # Return the calculated sum
    return result


# Recursive factorial stacks each function, reaches base case, and unwinds back to n
def factorial_recursive(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    else:
        # Else recursive multiple n * recursive function n -1

        return n * factorial_recursive(n-1)


n = 5
print(f'Factorial Iteration: {factorial_iteration(n)}')
print(f'Factorial Recursive: {factorial_recursive(n)}')
