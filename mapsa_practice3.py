'''
We receive a number "n" as input.
Between the two numbers in the range of "1" to "n", Greatest Common Divisor or the same GCD we get.
What is the largest GCD among all GCDs obtained?
'''

# n = int(input("Please enter an integer: "))
n = int(input())


def gcd(num1, num2):
    m = min(num1, num2)
    M = max(num1, num2)

    divisors = list()
    for b in range(1, m + 1):
        if m % b == 0 and M % b == 0:
            divisors.append(b)

    return max(divisors)


GCDs = list()
for i in range(1, n):
    for j in range(1, i):
        GCDs.append(gcd(i, j))

print(max(GCDs))


# by Shervin Hasanzadeh
