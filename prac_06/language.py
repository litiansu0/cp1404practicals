"""
Programming Languages Demo

This program demonstrates the use of the ProgrammingLanguage class by creating
instances of different programming languages and using their methods.

Estimate: 40 minutes
Actual: 30 minutes
"""

from programming_language import ProgrammingLanguage

def main():
    # Create instances of programming languages
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    # Print python instance to test __str__ method
    print(python)

    # Create a list containing all language objects
    languages = [python, ruby, visual_basic]

    # Loop through and print the names of all dynamically typed languages
    print("\nThe dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

if __name__ == "__main__":
    main()
    