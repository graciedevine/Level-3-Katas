# Count the number of divisors of a positive integer n

# How to find divisors:
# 12 --> 6 (1, 2, 3, 4, 6, 12)
# Divide by every number < n
# Count how many numbers divisible by n

# Take n as input parameter
# store in counter (divisor_count)
# n % m == 0
# count length of divisors in divisor_count
# return length of divisor_count


def divisors(n):
    divisor_count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            divisor_count += 1
    return divisor_count


print(divisors(12))
