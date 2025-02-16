# 1. get the name
name = input("Enter name: ")

# 2. define and display the menu
MENU = """(H)ello
(G)oodbye
(Q)uit
"""
print(MENU)

# 3. get the user's choice
choice = input(">>>").upper() # easier checks

# 4. looping until the user chooses Q (quit)
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye  {name}")
    else:
        print("Invalid choice")

    # Re‐display menu and get another choice
    print(MENU)
    choice = input(">>>").upper()
    
# 5. after "Q" entered, display a finished message
print("Finished.")