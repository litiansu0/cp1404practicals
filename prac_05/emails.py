#!/usr/bin/env python3
"""
CP1404/CP5632 Practical - Emails
Estimate: 40 minutes
Actual: 60 minutes
"""

def extract_name_from_email(email):
    """
    Extract a potential name from an email address.
    
    Args:
        email (str): An email address
        
    Returns:
        str: A potential name extracted from the email
    """
    # Remove the domain part
    username = email.split('@')[0]
    
    # Replace dots, underscores, dashes, etc. with spaces
    for char in ['.', '_', '-']:
        username = username.replace(char, ' ')
    
    # Capitalize each word
    name_parts = username.split()
    name = ' '.join([part.title() for part in name_parts])
    
    return name

def main():
    """
    Main function to collect emails and names and store them in a dictionary.
    """
    # Initialize an empty dictionary to store email-name pairs
    email_to_name = {}
    
    print("Enter emails (leave blank to finish):")
    
    while True:
        # Get email input
        email = input("Email: ").strip()
        
        # Break the loop if the email is blank
        if not email:
            break
        
        # Extract a potential name from the email
        suggested_name = extract_name_from_email(email)
        
        # Ask for confirmation or a different name
        response = input(f"Is your name {suggested_name}? (Y/n) ").strip()
        
        # If user presses Enter or types 'Y' or 'y', accept the suggested name
        if not response or response.lower() == 'y':
            email_to_name[email] = suggested_name
        else:
            # Ask for the correct name
            name = input("Name: ").strip()
            email_to_name[email] = name
    
    # Print all collected emails and names
    print("\nCollected Information:")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")

if __name__ == "__main__":
    main()