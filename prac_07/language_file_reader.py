"""
CP1404/CP5632 Practical
File and class example - opens/reads a file, stores in objects of custom class
(contains multiple versions for demonstration: using csv and namedtuple)
"""

import csv
from collections import namedtuple

from programming_language import ProgrammingLanguage


def main():
    """Read file of programming language details, save as objects, display."""
    languages = []
    # Open the file for reading
    in_file = open('languages.csv', 'r')
    # File format is: Language,Typing,Reflection,Year,PointerArithmetic
    in_file.readline()  # Skip header
    for line in in_file:
        parts = line.strip().split(',')
        # Convert reflection and pointer_arithmetic to booleans
        reflection = parts[2] == "Yes"
        pointer_arithmetic = parts[4] == "Yes"  # New field
        # Create object with 5 parameters
        language = ProgrammingLanguage(
            name=parts[0],
            typing=parts[1],
            reflection=reflection,
            year=int(parts[3]),
            pointer_arithmetic=pointer_arithmetic
        )
        languages.append(language)
    in_file.close()

    # Display all languages
    for language in languages:
        print(language)


if __name__ == "__main__":
    main()


def using_csv():
    """Language file reader version using the csv module."""
    in_file = open('languages.csv', 'r', newline='')
    in_file.readline()  # Skip header
    reader = csv.reader(in_file)
    for row in reader:
        # Convert fields (including new PointerArithmetic)
        reflection = row[2] == "Yes"
        pointer_arithmetic = row[4] == "Yes"
        language = ProgrammingLanguage(
            row[0], row[1], reflection, int(row[3]), pointer_arithmetic
        )
        print(language)
    in_file.close()


def using_namedtuple():
    """Language file reader version using a named tuple."""
    in_file = open('languages.csv', 'r', newline='')
    header = in_file.readline().strip().split(',')
    # Update namedtuple to include PointerArithmetic
    Language = namedtuple('Language', 'name, typing, reflection, year, pointer_arithmetic')
    reader = csv.reader(in_file)
    for row in reader:
        # Convert boolean fields
        row[2] = row[2] == "Yes"
        row[4] = row[4] == "Yes"
        row[3] = int(row[3])
        language = Language._make(row)
        print(f"{language.name}: PA={language.pointer_arithmetic}")


def using_csv_namedtuple():
    """Language file reader version using both csv module and named tuple."""
    # Update namedtuple definition
    Language = namedtuple('Language', 'name, typing, reflection, year, pointer_arithmetic')
    in_file = open("languages.csv", "r")
    in_file.readline()  # Skip header
    for row in csv.reader(in_file):
        # Convert fields
        row[2] = row[2] == "Yes"
        row[4] = row[4] == "Yes"
        row[3] = int(row[3])
        language = Language._make(row)
        print(f"{language.name} ({language.year}) - Pointer Arithmetic: {language.pointer_arithmetic}")