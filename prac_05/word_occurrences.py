"""
CP1404/CP5632 Practical - Word Occurrences
Estimate: 30 minutes
Actual: 45 minutes
"""

text = input("Text: ").strip()  # Get user input and remove leading/trailing spaces
while not text:  # Ensure input is not empty
    print("Input cannot be empty.")  
    text = input("Text: ").strip()

words = text.split()  # Split the text into words using spaces as delimiters
word_counts = {}  # Initialize an empty dictionary to store word frequencies

# Count word occurrences using the dictionary's get method for simplicity
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

# Get a sorted list of unique words
sorted_words = sorted(word_counts.keys())

# Calculate the length of the longest word for alignment (set to 0 if the list is empty)
max_length = max(len(word) for word in sorted_words) if sorted_words else 0

# Format and print the word count results
for word in sorted_words:
    print(f"{word:{max_length}} : {word_counts[word]}")
