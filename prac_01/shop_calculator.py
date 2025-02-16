# 1. get valid input for number of items
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

# 2. get prices for each item and accumulate the total
total_price = 0
for _ in range(number_of_items):
    price = float(input("Price of item: "))
    total_price += price

# 3. apply 10% discount if total is more than $100
if total_price > 100:
    total_price *=0.9

# 4. display the result formatted to 2 decimal places
print(f"Total price for {number_of_items} items is ${total_price:.2f}")