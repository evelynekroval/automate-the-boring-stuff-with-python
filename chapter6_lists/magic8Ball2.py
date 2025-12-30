"""
Magic 8-Ball program that provides random answers to yes/no questions.

It's the same, but rewritten much more compactly, than chapter 4's magic8Ball.py

This script demonstrates two methods of selecting random items from a list:
1. Using random.randint() with list indexing (manual approach) - interesting and worth reading
2. Using random.choice() (built-in convenience method)

The program prompts the user for a yes/no question and returns a random
fortune-teller style response from a predefined list of messages.

Logging is configured to track which method was used for each random selection.

"""

import random
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']



print('Ask a yes or no question:')
input('> ')
print(messages[random.randint(0, len(messages) - 1)])
logging.debug("This was from the complicated indexation by randint")

# What's clever about this is that it's using
# `random.randint(0, len(messages)-1)` 
# as a way to generate the index to `messages`, hence the []
# within which it exists.

# But why `len(messages)-1`?
# Think about it this way:
# say list = [1, 2, 3, 4, 5, 7]
# len(list) is 7
# but the index runs 0-6
# hence why for the purposes of index you do len(list)-1

# Although picking an item randomly from a list is so common in 
# python at this point that you could just do:
print(random.choice(messages))
logging.debug("This was by just random.choice(list).")
