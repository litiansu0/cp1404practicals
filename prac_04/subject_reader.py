"""
CP1404/CP5632 Practical
Data file -> lists program
"""

# FILENAME = "subject_data.txt"


# def main():
#     data = load_data()
#     print(data)


# def load_data():
#     """Read data from file formatted like: subject,lecturer,number of students."""
#     input_file = open(FILENAME)
#     for line in input_file:
#         print(line)  # See what a line looks like
#         print(repr(line))  # See what a line really looks like
#         line = line.strip()  # Remove the \n
#         parts = line.split(',')  # Separate the data into its parts
#         print(parts)  # See what the parts look like (notice the integer is a string)
#         parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
#         print(parts)  # See if that worked
#         print("----------")
#     input_file.close()


# main()


FILENAME = "subject_data.txt"

def main():
    """Read subject data and display it in a formatted way."""
    data = load_data()
    display_subject_details(data)

def load_data():
    """Read data from file formatted like: subject,lecturer,number of students.
    Return a list of lists where inner lists contain [subject, lecturer, number]."""
    input_file = open(FILENAME)
    subjects = []  # Create empty list to store all subjects
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Convert the number of students to an integer
        subjects.append(parts)  # Add this subject list to our list of subjects
    input_file.close()
    return subjects

def display_subject_details(subjects):
    """Display subject details in a nicely formatted way."""
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")

main()