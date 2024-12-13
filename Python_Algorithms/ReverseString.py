s = str(input("Enter a string: "))
rs = ""

# Method 1: 0(n^2)
for i in range(len(s) - 1, -1, -1):
    rs += s[i]

# Method 2: Slicing O(n)
rss = s[::-1]

print(f'{s} = {rs}')
print(f'{s} = {rss}')
