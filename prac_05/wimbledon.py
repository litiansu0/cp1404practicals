#!/usr/bin/env python3
"""
CP1404/CP5632 Practical - Wimbledon Champions Analysis
Estimate: 90 minutes
Actual: 60 minutes
"""


def read_wimbledon_data(filename):
    """
    Read the Wimbledon data from a CSV file.
    
    Args:
        filename (str): Path to the CSV file
        
    Returns:
        list: List of records, each containing data for one year
    """
    records = []
    
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        # Skip header line
        next(in_file)
        
        for line in in_file:
            # Strip newline and split by comma
            fields = line.strip().split(',')
            records.append(fields)
    
    return records


def get_champion_stats(records):
    """
    Process the records to get statistics about champions.
    
    Args:
        records (list): List of Wimbledon records
        
    Returns:
        dict: Dictionary with champions as keys and their win counts as values
    """
    champion_wins = {}
    
    for record in records:
        champion = record[2]  # Champion's name is at index 2
        
        if champion in champion_wins:
            champion_wins[champion] += 1
        else:
            champion_wins[champion] = 1
    
    return champion_wins


def get_champion_countries(records):
    """
    Extract the unique countries of champions in alphabetical order.
    
    Args:
        records (list): List of Wimbledon records
        
    Returns:
        list: Sorted list of unique countries
    """
    # Use a set to store unique countries
    countries = set()
    
    for record in records:
        country = record[1]  # Champion's country is at index 1
        countries.add(country)
    
    # Convert set to sorted list
    return sorted(list(countries))


def display_results(champion_wins, countries):
    """
    Display the processed information in the required format.
    
    Args:
        champion_wins (dict): Dictionary with champions and their win counts
        countries (list): List of countries in alphabetical order
    """
    print("Wimbledon Champions:")
    for champion, wins in champion_wins.items():
        print(f"{champion} {wins}")
    
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


def main():
    """
    Main function to coordinate the program execution.
    """
    # Read the data
    records = read_wimbledon_data("prac_05/wimbledon.csv")
    
    # Process the data
    champion_wins = get_champion_stats(records)
    countries = get_champion_countries(records)
    
    # Display the results
    display_results(champion_wins, countries)


if __name__ == "__main__":
    main()
