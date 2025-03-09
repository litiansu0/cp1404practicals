"""
Guitar Testing Program

This program tests the Guitar class methods to ensure they work as expected. 
It displays expected vs. actual values.

Estimate: 20 minutes
Actual: 30 minutes
"""

from guitar import Guitar
from datetime import datetime

def run_tests():
    """Run tests for the Guitar class."""
    current_year = datetime.now().year  # Get the current year to dynamically compute the expected age

    # Create test instances of Guitar
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013, 899.99)

    # Test get_age() method
    # The expected value is computed dynamically
    expected_age_guitar1 = current_year - 1922
    actual_age_guitar1 = guitar1.get_age()
    print(f"{guitar1.name} get_age() - Expected {expected_age_guitar1}. Got {actual_age_guitar1}")

    expected_age_guitar2 = current_year - 2013
    actual_age_guitar2 = guitar2.get_age()
    print(f"{guitar2.name} get_age() - Expected {expected_age_guitar2}. Got {actual_age_guitar2}")

    # Test is_vintage() method
    # The standard for a vintage guitar is an age >= 50
    vintage_expected_guitar1 = (current_year - 1922) >= 50
    vintage_actual_guitar1 = guitar1.is_vintage()
    print(f"{guitar1.name} is_vintage() - Expected {vintage_expected_guitar1}. Got {vintage_actual_guitar1}")

    vintage_expected_guitar2 = (current_year - 2013) >= 50
    vintage_actual_guitar2 = guitar2.is_vintage()
    print(f"{guitar2.name} is_vintage() - Expected {vintage_expected_guitar2}. Got {vintage_actual_guitar2}")

if __name__ == "__main__":
    run_tests()
