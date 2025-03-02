"""
CP1404/CP5632 Practical
State names in a dictionary
Reformatted and improved with EAFP
"""

CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia"
}

# Task 4: Format and output all states
for code, name in CODE_TO_NAME.items():
    print(f"{code} is {name}")

# Task 3: Allow lowercase input (add .upper() in two places)
state_code = input("Enter short state: ").upper()
while state_code != "":
    # Task 5: Switch to EAFP exception handling
    try:
        print(f"{state_code} is {CODE_TO_NAME[state_code]}")
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()