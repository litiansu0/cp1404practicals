import random

def determine_score_status(score):
    """
    Determine the status of a score between 0 and 100.
    
    Args:
        score (float): The score to evaluate
        
    Returns:
        str: The status of the score ("Invalid score", "Excellent", "Passable", or "Bad")
    """
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def main():
    # Get user input
    score = float(input("Enter score: "))
    result = determine_score_status(score)
    print(result)
    
    # Generate and evaluate random score
    random_score = random.randint(0, 100)
    print(f"\nRandom score is: {random_score}")
    random_result = determine_score_status(random_score)
    print(random_result)

if __name__ == "__main__":
    main()