# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
# Example: create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

# Check that 10 numbers were entered between 0-9
# Format first 3 digits inside () + " "
# Format following 7 with - after 3rd digit
# return as string


def create_phone_number(n):
    if len(n) != 10:
        return False

    # checks if all elements in array are numbers, returns True or False
    # print(all([isinstance(item, int) for item in n]))

    num = "".join(str(h)for h in n)
    return f"({num[0:3]}) {num[3:6]}-{num[6:]}"


print((create_phone_number([7, 5, 7, 2, 4, 0, 9, 4, 0, 2])))
