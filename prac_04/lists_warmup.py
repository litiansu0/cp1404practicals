# list
numbers = [3, 1, 4, 1, 5, 9, 2]


# Predictions
# numbers[0]    -> 3    (first element)
# numbers[-1]   -> 2    (last element)
# numbers[3]    -> 1    (4th element)
# numbers[:-1]  -> [3, 1, 4, 1, 5, 9]   (all except last)
# numbers[3:4]  -> [1]  (single element slice)
# 5 in numbers  -> True (5 exists in list)
# 7 in numbers  -> Fales    (7 doesn't exist)
# "3" in numbers    -> Fales    (string "3" not in list)
# numbers + [6, 5, 3]   -> [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# specific practice
print("numbers[0] =", numbers[0])
print("numbers[-1] =", numbers[-1])
print("numbers[3] =", numbers[3])
print("numbers[:-1] =", numbers[:-1])
print("numbers[3:4] =", numbers[3:4])
print("5 in numbers =", 5 in numbers)
print("7 in numbers =", 7 in numbers)
print("'3' in numbers =", "3" in numbers)
print("numbers + [6, 5, 3] =", numbers + [6, 5, 3])

# modifying the list as requested:
numbers[0] = "ten"  # Change first element to string "10"
numbers[-1] = 1     # Change last element to 1

# print all elements except first two
print("All elements except first two:", numbers[2:])

# cheak if 9 is in numbers
print("Is 9 in numbers?", 9 in numbers)




