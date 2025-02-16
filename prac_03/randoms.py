# import random
# dir(random)

import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3


# What did you see on line 1? 
# Observed value range: 5 to 20, inclusive.
# What was the smallest number you could have seen, what was the largest?
# Minimum possible value: 5 and Maximum possible value: 20

# What did you see on line 2?
# Observed value range: 3, 5, 7, 9 (in steps of 2)
# What was the smallest number you could have seen, what was the largest?
# Minimum possible value: 3 and Maximum possible value: 9
# Could line 2 have produced a 4?
# Since the step size is 2, 4 cannot be generated

# What did you see on line 3?
# Observed value range: 2.5 to 5.5 (inclusive, but floating point)
# What was the smallest number you could have seen, what was the largest?
# Minimum possible value: close to 2.5 and Maximum possible value: close to 5.5

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
random_number = random.randint(1, 100)
print(random_number)

