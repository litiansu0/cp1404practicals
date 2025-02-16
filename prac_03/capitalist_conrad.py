"""
CP1404/CP5632 - Practical
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is
a 50% chance it increases by 0 to 10%, and
a 50% chance that it decreases by 0 to 5%.
If the price rises above $1000, or falls below $0.01, the program should end.
The price should be displayed to the nearest cent (e.g. $33.59, not $33.5918232901)
"""
import random

# Constants
MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05   # 5%
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
FILENAME = "stock_prices.txt"

# Initialize variables
price = INITIAL_PRICE
number_of_days = 0

# Open output file
out_file = open(FILENAME, 'w')

# Write starting price
out_file.write(f"Starting price: ${price:,.2f}\n")

# Simulate daily price changes
while MIN_PRICE <= price <= MAX_PRICE:
    number_of_days += 1
    
    # Determine price change
    if random.randint(1, 2) == 1:
        # Generate random increase between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # Generate random decrease between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)
    
    # Apply price change
    price *= (1 + price_change)
    
    # Write daily price to file
    out_file.write(f"On day {number_of_days} price is: ${price:,.2f}\n")

# Write final summary
if price < MIN_PRICE:
    out_file.write(f"\nOn day {number_of_days}, price fell below ${MIN_PRICE:.2f}")
elif price > MAX_PRICE:
    out_file.write(f"\nOn day {number_of_days}, price exceeded ${MAX_PRICE:.2f}")

# Close the output file
out_file.close()