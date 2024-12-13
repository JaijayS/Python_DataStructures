def fibonacci_iterative(n):
    # Handle the base cases
    if n <= 0:
        return 0
    elif n <= 1:
        return 1

    prev1, prev2 = 1, 0

    for i in range(2, n+1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
    return prev1


def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    return fibonacci_recursive(n-1) + fibonacci_recursive(n - 2)
# Test the function
n = 6


print(f"Fibonacci of {n} (iterative): {fibonacci_iterative(n)}")  # Output: 8
print(f"Fibonacci of {n} (recursive): {fibonacci_recursive(n)}")  # Output: 8