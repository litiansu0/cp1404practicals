"""
ProgrammingLanguage Class

This module defines a class for representing programming languages with their properties
such as typing system, reflection capability, and year of first appearance.

Estimate: 15 minutes
Actual: 20 minutes
"""

class ProgrammingLanguage:
    """
    Class to represent a programming language and its properties.
    
    Attributes:
        name (str): Name of the programming language
        typing (str): Type system of the language (Static or Dynamic)
        reflection (bool): Whether the language supports reflection
        year (int): Year when the language first appeared
    """
    
    def __init__(self, name, typing, reflection, year):
        """
        Initialize a new ProgrammingLanguage instance.
        
        Args:
            name (str): Name of the programming language
            typing (str): Type system of the language (Static or Dynamic)
            reflection (bool): Whether the language supports reflection
            year (int): Year when the language first appeared
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
    
    def is_dynamic(self):
        """
        Check if the programming language is dynamically typed.
        
        Returns:
            bool: True if the language is dynamically typed, False otherwise
        """
        return self.typing.lower() == "dynamic"
    
    def __str__(self):
        """
        Return a string representation of the programming language.
        
        Returns:
            str: String containing the language details
        """
        reflection_text = "True" if self.reflection else "False"
        return f"{self.name}, {self.typing} Typing, Reflection={reflection_text}, First appeared in {self.year}"