"""
Lesson: Pig Latin is a word game where you move consonants around and add 'ay' to the end.
Like "hello" becomes "ello-hay" (move the 'h' to the end, add 'ay').

Code: This program takes English words and converts them to Pig Latin by:
1. Stripping away punctuation marks at the start and end
2. Finding consonants at the beginning of each word
3. Moving those consonants to the end and adding 'ay'
4. Keeping uppercase/title case formatting intact

Main Takeaways:
  • String slicing (word[0], word[1:], word[-1]) lets you grab parts of words
  • While loops help you peel away characters one-by-one from the edges
  • Case tracking (isupper(), istitle()) preserves the original word's formatting
"""

# Ask the user to type in a message
print('Enter the English message to translate into pig latin:')
message = input()

# Create a tuple of vowels (a, e, i, o, u, and sometimes y)
VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

# Create an empty list to store each word after it's converted to pig latin
pig_latin = []

# Loop through each word in the message (split() breaks it into individual words)
for word in message.split():
    # Create a string to hold any punctuation/symbols at the START of the word
    # (like if someone typed "...hello" the "..." gets stored here)
    prefix_non_letters = ''
    
    # Keep checking: if the word has characters AND the first character isn't a letter
    while len(word) > 0 and not word[0].isalpha():
        # Add that non-letter character to our prefix_non_letters string
        prefix_non_letters += word[0]
        # Remove it from the word (word[1:] means "everything except the first character")
        word = word[1:]
    
    # If we stripped away ALL the characters and nothing's left (like if input was "...")
    if len(word) == 0:
        # Just add the punctuation back and skip to the next word
        pig_latin.append(prefix_non_letters)
        continue

    # Now do the same thing but for the END of the word (like "hello!" → the "!")
    suffix_non_letters = ''
    
    # Keep checking: if the last character isn't a letter
    while not word[-1].isalpha():
        # Add it to the START of suffix_non_letters (that's why we do word[-1] + suffix...)
        suffix_non_letters = word[-1] + suffix_non_letters
        # Remove it from the end of the word (word[:-1] means "everything except the last character")
        word = word[:-1]

    # Check if the original word was ALL uppercase (like "HELLO")
    was_upper = word.isupper()
    
    # Check if the original word was Title Case (like "Hello")
    was_title = word.istitle()

    # Convert the word to all lowercase so we can translate it consistently
    word = word.lower()

    # Create a string to hold consonants at the BEGINNING of the word
    # (like "hello" → the "h" goes here)
    prefix_consonants = ''
    
    # Keep checking: if the word has characters AND the first character is NOT a vowel
    while len(word) > 0 and not word[0] in VOWELS:
        # Add that consonant to prefix_consonants
        prefix_consonants += word[0]
        # Remove it from the word
        word = word[1:]

    # Now add the pig latin ending:
    # If there WERE consonants at the start (like "hello" had "h")
    if prefix_consonants != '':
        # Add those consonants to the end + "ay" (hello → ello → ellohay)
        word += prefix_consonants + 'ay'
    else:
        # If the word STARTED with a vowel (like "apple")
        # Just add "yay" to the end (apple → appleyay)
        word += 'yay'

    # Restore the original case (ALL CAPS or Title Case)
    if was_upper:
        word = word.upper()
    if was_title:
        word = word.title()

    # Put the punctuation back at the start and end, then add to our list
    # (like if it was "...hello!" → now it becomes "...ellohay!")
    pig_latin.append(prefix_non_letters + word + suffix_non_letters)

# Join all the pig latin words back together with spaces between them
# Then print the final result
print(' '.join(pig_latin))