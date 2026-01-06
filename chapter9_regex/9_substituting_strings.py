"""
Demonstrates string substitution using regular expressions in Python.
This module shows how to use the .sub() method of regex `Pattern` objects to
replace matched text in strings. It covers two approaches:
1. Simple substitution: Replacing all matches with a fixed string
2. Back references: Using captured groups from the match in the replacement
The .sub() method accepts two arguments:
    - A replacement string (which may contain back references like \1, \2)
    - The string to search and replace in
Examples:
    Simple substitution - replace all agent names with 'CENSORED':
        >>> agent_pattern = re.compile(r'Agent \w+')
        >>> agent_pattern.sub('CENSORED', 'Agent Alice contacted Agent Bob')
        'CENSORED contacted CENSORED.'
    Using back references - keep only the first letter of agent names:
        >>> initial_pattern = re.compile(r'Agent (\w)\w*')
        >>> initial_pattern.sub(r'\1****', 'Agent Alice contacted Agent Bob.')
        'A**** contacted B****.'
Note:
    Back references (\1, \2, etc.) refer to captured groups in the regex pattern.
    Use raw strings (r'...') for the replacement to properly handle backslashes.
"""

import re

# Regex are not purely for finding text
# You can substitute too
# Enter: .sub() method for Pattern object, which accepts 2 args:
    # a str that should replace any matches
    # str of the regex
# Returns str with subs applied

agent_pattern = re.compile(r'Agent \w+')
print(agent_pattern.sub('CENSORED', 'Agent Alice contacted Agent Bob'))
#Outputs 'CENSORED contacted CENSORED.'

# Sometimes you wanna use the matched text itself as part of the sub
# In the 1st arg to sub() you can include \1, \2 etc., making ref to the groups!
# Called BACK REFERENCE
# So you need to group...
initial_pattern = re.compile(r'Agent (\w)\w*')
print(initial_pattern.sub(r'\1****', 'Agent Alice contacted Agent Bob.'))
# Outputs 'A**** contacted B****.'