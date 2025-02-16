"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

# try:
#     numerator = int(input("Enter the numerator: "))
#     denominator = int(input("Enter the denominator: "))
#     fraction = numerator / denominator
#     print(fraction)
# except ValueError:
#     print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# print("Finished.")


# 1. When will a ValueError occur?
# When the user enters a value that cannot be converted to an integer (for example, a text input such as "xyz" or a decimal such as "3.14"), a ValueError is triggered regardless of whether it is the numerator or the denominator
# 2. When will a ZeroDivisionError occur?
# When the denominator entered by the user is 0, a ZeroDivisionError is triggered
# 3. Could you change the code to avoid the possibility of a ZeroDivisionError?
# Yes. Use input validation to ensure that the denominator is not zero to avoid triggering this error

try:
    numerator = int(input("Enter the numerator: "))
    while True:
        denominator = int(input("Enter the denominator: "))
        if denominator != 0:
            break
        print("Denominator cannot be zero. Please try again.")
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")