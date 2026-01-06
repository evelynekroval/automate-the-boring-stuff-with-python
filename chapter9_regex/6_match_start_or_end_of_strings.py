"""
Demonstrates regex anchors and word boundaries for pattern matching.
This module shows how to use special regex characters to match patterns at specific
positions in strings:
- ^ (caret): Matches at the beginning of the string
- $ (dollar): Matches at the end of the string
- ^...$: Matches if the entire string matches the pattern
- \\b: Matches at word boundaries (start or end of words)
- \\B: Matches at positions that are NOT word boundaries
Examples:
    Match strings beginning with 'Hello':
        >>> begins_with_hello = re.compile(r'^Hello')
        >>> begins_with_hello.search('Hello, world!')
        <re.Match object; span=(0, 5), match='Hello'>
    Match strings ending with a digit:
        >>> ends_with_number = re.compile(r'\\d$')
        >>> ends_with_number.search('Your number is 42')
        <re.Match object; span=(16, 17), match='2'>
    Match entire string of digits:
        >>> whole_string_is_num = re.compile(r'^\\d+$')
        >>> whole_string_is_num.search('1234567890')
        <re.Match object; span=(0, 10), match='1234567890'>
    Match words starting with 'cat':
        >>> word_pattern = re.compile(r'\\bcat.*?\\b')
        >>> word_pattern.findall('The cat found a catapult')
        ['cat', 'catapult']
    Match 'cat' only when NOT at word boundaries:
        >>> no_word_pattern = re.compile(r'\\Bcat\\B')
        >>> no_word_pattern.findall('certificate')
        ['cat']
"""
import re


# You can use the caret (^) at start of regex to indicate that match 
# must occur at beginning of searched text

begins_with_hello = re.compile(r'^Hello')
print(begins_with_hello.search('Hello, world!'))
# Outputs <re.Match object; span=(0, 5), match='Hello'>

print(begins_with_hello.search('He said "Hello."') == None)
# Outputs True - because 'Hello' is not at the beginning


# You can use a dollar sign ($) at end of regex to indicate that match
# must end with the regex pattern
ends_with_number = re.compile(r'\d$')
print(ends_with_number.search('Your number is 42'))
# Outputs <re.Match object; span=(16, 17), match='2'>

print(ends_with_number.search('Your number is forty two.') == None)
# Outputs True - because there is no [0-9] occurring at the end of the str


# You can use ^ and $ to indicate that the entire str must match regex
# i.e. it's insufficient to match on some subset of the str
whole_string_is_num = re.compile(r'^\d+$')
print(whole_string_is_num.search('1234567890'))
# Outputs <re.Match object; span=(0, 10), match='1234567890'>

print(whole_string_is_num.search('12345xyz67890') == None)
# Outputs True - because the str is not [0-9] the whole way through as requested


# You can also narrow down to start or end of a word with \b

# Beginning with 'cat', anything in the middle, but must basically end as a word (due to closing \b)
word_pattern = re.compile(r'\bcat.*?\b')
print(word_pattern.findall('The cat found a catapult catalog in the catacombs.'))
# Outputs ['cat', 'catapult', 'catalog', 'catacombs']

# \B syntax matches anything that is not a word boundary:
# Useful when you're trying to find things inside words
no_word_pattern = re.compile(r'\Bcat\B')
print(no_word_pattern.findall('certificate')) # Match
# Outputs ['cat']

print(no_word_pattern.findall('catastrophe')) # No Match
# Outputs []