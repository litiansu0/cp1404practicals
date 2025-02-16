# Program 1: Write name to file
def write_name():
    """Write user's name to name.txt file."""
    name = input("Enter your name: ")
    out_file = open('name.txt', 'w')
    out_file.write(name)
    out_file.close()


# Program 2: Read name from file and print greeting
def read_name():
    """Read name from name.txt and print greeting."""
    in_file = open('name.txt', 'r')
    name = in_file.read().strip()
    in_file.close()
    print(f"Hi {name}!")


# Program 3: Read and sum first two numbers
def sum_first_two():
    """Read and sum first two numbers from numbers.txt."""
    with open('numbers.txt', 'r') as in_file:
        number1 = int(in_file.readline())
        number2 = int(in_file.readline())
        print(number1 + number2)


# Program 4: Sum all numbers in file
def sum_all():
    """Sum all numbers from numbers.txt."""
    with open('numbers.txt', 'r') as in_file:
        total = 0
        for line in in_file:
            total += int(line)
        print(total)


# Main program to demonstrate all functions
def main():
    print("Program 1: Writing name to file")
    write_name()
    
    print("\nProgram 2: Reading name from file")
    read_name()
    
    print("\nProgram 3: Sum of first two numbers")
    sum_first_two()
    
    print("\nProgram 4: Sum of all numbers")
    sum_all()


if __name__ == "__main__":
    main()