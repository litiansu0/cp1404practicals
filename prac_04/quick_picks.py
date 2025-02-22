import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45

def main():
    """Quick picks program - choose sets of random numbers."""
    number_of_quick_picks = int(input("How many quick picks? "))
    while number_of_quick_picks < 0:
        print("That makes no sense!")
        number_of_quick_picks = int(input("How many quick picks? "))

    for _ in range(number_of_quick_picks):
        quick_pick = []
        while len(quick_pick) < NUMBERS_PER_LINE:
            number = random.randint(MINIMUM, MAXIMUM)
            if number not in quick_pick:
                quick_pick.append(number)
        quick_pick.sort()
        # use a generator expression to format each number to 2 digits wide, ensuring alignment
        print(" ".join(f"{number:2}" for number in quick_pick))

if __name__ == "__main__":
    main()