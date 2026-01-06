"""
Phone Number Detection Module
This module provides functionality to detect phone numbers in text using a basic
pattern matching approach without regular expressions.
Functions
---------
is_phone_number(text: str) -> bool
    Validates whether a given text string matches the phone number format XXX-XXX-XXXX,
    where X represents a decimal digit.
    Parameters:
        text (str): The string to validate as a phone number.
    Returns:
        bool: True if the text matches the phone number format, False otherwise.
    Format Requirements:
        - Exactly 12 characters long
        - First 3 characters: digits (area code)
        - 4th character: dash (-)
        - Next 3 characters: digits (exchange code)
        - 8th character: dash (-)
        - Last 4 characters: digits (subscriber number)
    Example:
        >>> is_phone_number('415-555-1011')
        True
        >>> is_phone_number('415-5551011')
        False
Example Usage
-------------
The module demonstrates finding phone numbers in a message string by iterating
through all possible 12-character segments and validating each one.
"""

def is_phone_number(text):
    if len(text) != 12:  # Phone numbers have exactly 12 characters.
        return False
    for i in range(0, 3):  # The first three characters must be numbers.
        if not text[i].isdecimal():
            return False
    if text[3] != '-':  # The fourth character must be a dash.
        return False
    for i in range(4, 7): # The next three characters must be numbers.
        if not text[i].isdecimal():
            return False
    if text[7] != '-':  # The eighth character must be a dash.
        return False
    for i in range(8, 12):  # The next four characters must be numbers.
        if not text[i].isdecimal():
            return False
    return True

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    segment = message[i:i+12]
    if is_phone_number(segment):
        print('Phone number found: ' + segment)
print('Done')