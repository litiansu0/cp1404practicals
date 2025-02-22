"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


# def main():
#     """Display income report for incomes over a given number of months."""
#     incomes = []
#     months = int(input("How many months? "))

#     for month in range(1, months + 1):
#         income = float(input("Enter income for month " + str(month) + ": "))
#         incomes.append(income)

#     print("\nIncome Report\n-------------")
#     total = 0
#     for month in range(1, months + 1):
#         income = incomes[month - 1]
#         total += income
#         print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


# main()



def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))  # refactored from 'months' to 'number_of_months'

    for month in range(1, number_of_months + 1):
        # changed to f-string from string concatenation
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_report(incomes)  # moved report printing to separate function


def print_report(incomes):
    """Print income report showing monthly incomes and running total."""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, len(incomes) + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()