"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 5
MAX_LENGTH = 15
IS_SPECIAL_CHARACTER_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^*()_+-=,./{[]}<>?\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if IS_SPECIAL_CHARACTER_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)}-character password is valid: {password}")


def is_valid_password(password):
    """Determine if the provided password is valid."""
    # First check password length
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    # Initialize counters for each type of character
    number_of_lower = 0
    number_of_upper = 0
    number_of_digit = 0
    number_of_special = 0

    # Loop through the string once and count all types of characters
    for character in password:
        # First check for lowercase
        if character.islower():
            number_of_lower += 1
        # Then check for uppercase
        elif character.isupper():
            number_of_upper += 1
        # Then check for digits
        elif character.isdigit():
            number_of_digit += 1
        # Finally check for special characters
        elif character in SPECIAL_CHARACTERS:
            number_of_special += 1

    # Check if we have at least one of each required type
    if number_of_lower == 0:
        return False
    if number_of_upper == 0:
        return False
    if number_of_digit == 0:
        return False
    
    # Check special characters only if required
    if IS_SPECIAL_CHARACTER_REQUIRED and number_of_special == 0:
        return False

    # If we get here, the password must be valid
    return True


main()