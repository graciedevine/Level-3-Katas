# Instructions: If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

# Additionally, if the number is negative, return 0 (for languages that do have them).

# Steps:
# count+1 x 3 = multiple < 10
# Empty counter to store numbers as they increase
# Check that input is a number
# loop through all numbers in the range
#   if divisible by 3 or 5 and within range
# add to the counter variable
# return the sum of the answers
# If -n return 0


def solution(n):
    total_sum = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            total_sum += i

    return total_sum


print(solution(10))
