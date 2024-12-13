

def sumOfDigits(n):

    n = abs(n)

    sum = 0

    for i in range(len(n)):
        sum += int(n[i])

    return sum


if __name__ == '__main__':
    n = str(input())
    print(sumOfDigits(n))
