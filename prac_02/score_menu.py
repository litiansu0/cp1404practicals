def main():
    """Run the main program using the standard menu pattern."""
    print("Welcome to the Score Program")
    score = get_valid_score()
    
    choice = ''
    while choice != 'Q':
        print_menu()
        choice = input(">>> ").upper()
        
        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            result = determine_score_status(score)
            print(f"The score {score} is {result}")
        elif choice == 'S':
            print_stars(score)
        elif choice == 'Q':
            print("Farewell!")
        else:
            print("Invalid choice")

def print_menu():
    """Display the menu options."""
    print("\nMain Menu:")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")

def get_valid_score():
    """Get a valid score between 0 and 100 from the user."""
    while True:
        try:
            score = float(input("Enter score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Score must be between 0 and 100")
        except ValueError:
            print("Invalid input; enter a valid number")

def determine_score_status(score):
    """Determine the status of a score between 0 and 100."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def print_stars(score):
    """Print as many stars as the score value."""
    stars = int(score) * '*'
    print(stars)

if __name__ == "__main__":
    main()