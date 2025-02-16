"""
Program to calculate and display a user's bonus based on sales.  
If sales are under $1,000, the user gets a 10% bonus.  
If sales are $1,000 or over, the bonus is 15%.  
"""

#---------------Version 1 (without loop)---------------

# sales = float(input("Enter sales: $"))
# if sales < 1000:
#     bonus = 0.1 * sales
# else:
#     bonus = 0.15 * sales
# print(f"Bonus: ${bonus:.2f}")



#---------------Version 2 (with loop)---------------

sales = float(input("Enter sales: $"))
while sales >= 0: # It repeatedly asks for the user's sales and prints the bonus until they enter a negative number
    if sales < 1000:
        bonus = 0.1 * sales
    else:
        bonus = 0.15 * sales
    print(f"Bonus: ${bonus:.2f}")
    
    # Ask for the next sales amount (this will end the loop if negative)
    sales = float(input("Enter sales: $"))
    