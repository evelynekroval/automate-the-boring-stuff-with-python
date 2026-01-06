"""
Demonstrates the Humre library for creating more readable regular expressions.
This module shows how to use Humre as a higher-level interface for building regex
patterns that are easier to read and maintain than raw regex strings. Humre provides
human-readable functions that generate standard regex patterns.
The key advantage of Humre is readability - instead of writing cryptic regex syntax,
you can use descriptive function calls like `exactly(3, DIGIT)` which is more
self-documenting than `\\d{3}`.
Examples:
    Creating a phone number pattern with Humre:
        >>> from humre import *
        >>> phone_regex = exactly(3, DIGIT) + '-' + exactly(3, DIGIT) + '-' + exactly(4, DIGIT)
        >>> str(phone_regex)
        '\\d{3}-\\d{3}-\\d{4}'
    Using the Humre pattern with re.compile():
        >>> pattern = re.compile(phone_regex)
        >>> pattern.search('My number is 415-555-4242')
        <re.Match object; span=(13, 25), match='415-555-4242'>
Note:
    Humre does not replace the re module - it generates regex strings that are
    passed to standard re functions like re.compile(). This makes it compatible
    with existing regex-based code while improving pattern readability.
Reference:
    Full Humre documentation: https://pypi.org/project/Humre/
"""

import re
from humre import *

# If we go back to the r'\d{3}-\d{3}-\d{4} example, Humre allows a more readable option:
phone_regex = exactly(3, DIGIT) + '-' + exactly(3,DIGIT) + '-' + exactly(4, DIGIT)
print(type(phone_regex))
# Output: \d{3}-\d{3}-\d{4}

# Humre doesn’t replace the re module. Rather, it produces regex strings that can be passed to re.compile():

pattern = re.compile(phone_regex)
print(type(pattern))
print(pattern.search('My number is 415-555-4242'))
# Output: <re.Match object; span=(13, 25), match='415-555-4242'>


# You can read the Humre full reference here: https://pypi.org/project/Humre/.