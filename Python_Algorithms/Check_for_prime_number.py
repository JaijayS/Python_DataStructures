# noinspection PyShadowingNames
def is_1_number_prime(n):
    # n < 1 cannot be prime
    if n <= 1:
        return 'Not Prime'

    # 2 is only even prime
    if n == 2:
        return 'Prime'

    # Anything // 2 is not prime
    if n % 2 == 0:
        return 'Not Prime'

    # Start: i = 3, stop sqrt(n) + 1, iterate by 2
    # Base tests eliminate 1 and 2 so start at 3
    # No need to go above 1/2 of n. Start + 1 due to indexing
    # Iterate by 2 because you are starting with odd number. No need to test even numbers
    for i in range(3, int(n**0.5) + 1, 2):

        # Remainder of 0 between n and i indicates, n is divisible by i.. Not prime
        if n % i == 0:
            return 'Not Prime'

    # If iteration completes,  n is prime
    return 'Prime'


def numbers_in_range_prime(start, end):

    # define empty list to return
    indices = []

    # Iterate through range (start -> finish + 1)
    for i in range(start, end + 1):

        # i < 1 cannot be prime
        if i <= 1:
            continue

        # 2 is only even prime
        if i == 2:
            indices.append(i)

        # Anything // 2 is not prime
        if i % 2 == 0:
            continue

        # Start: j = 3, stop sqrt(n) + 1, iterate by 2
        # Base tests eliminate 1 and 2 so start at 3
        # No need to go above 1/2 of n. Start + 1 due to indexing
        # Iterate by 2 because you are starting with odd number. No need to test even numbers
        is_prime = True
        for j in range(3, int(i**0.5) + 1, 2):

            # Remainder of 0 between n and j indicates, n is divisible by j.. Not prime
            if i % j == 0:
                is_prime = False
                break

        # If iteration completes,  append i to indices
        if is_prime:
            indices.append(i)

    # Return list
    return indices


n = 31
# print(is_1_number_prime(n))

start = 10
end = 20
print(numbers_in_range_prime(start, end))
