"""
Guitar Class

This module defines a Guitar class for storing and working with guitar information
including name, year of manufacture, and cost.

Estimate: 30 minutes
Actual: 45 minutes
"""

from datetime import datetime


class Guitar:
    """Represent a Guitar object with its attributes and behaviors."""
    
    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar instance with name, year, and cost.
        
        Args:
            name (str): The name/model of the guitar
            year (int): The year the guitar was manufactured
            cost (float): The cost of the guitar in dollars
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return formatted string representation of the guitar.
        
        Returns:
            str: Formatted string in the format: Name (Year) : $Cost
                 Example: Gibson L-5 CES (1922) : $16,035.40
        """
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Calculate and return the guitar's age in years.
        
        Returns:
            int: The age of the guitar (current year - manufacture year)
        """
        current_year = datetime.now().year
        return current_year - self.year

    def is_vintage(self):
        """Determine if the guitar is considered vintage (≥50 years old).
        
        Returns:
            bool: True if guitar age is 50+ years, False otherwise
        """
        return self.get_age() >= 50


# Test code
if __name__ == "__main__":
    # Create test instances
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Fender Stratocaster", 2015, 1200.99)

    # Test string representation
    print(guitar1)  # Expected: Gibson L-5 CES (1922) : $16,035.40
    print(guitar2)  # Expected: Fender Stratocaster (2015) : $1,200.99

    # Test age calculation (assuming current year is 2023)
    print(f"{guitar1.name} age: {guitar1.get_age()} years")  # Expected: 101 years
    print(f"Is vintage? {guitar1.is_vintage()}")             # Expected: True

    print(f"{guitar2.name} age: {guitar2.get_age()} years")  # Expected: 8 years
    print(f"Is vintage? {guitar2.is_vintage()}")             # Expected: False