"""
Demonstrates the use of greedy and lazy matching with regular expressions in Python.
This module shows how to use the dot-star (.* and .*?) patterns in regex:
- The dot (.) matches any character except newline
- The asterisk (*) matches zero or more of the preceding character
- Greedy matching (.*) finds the longest possible match
- Lazy matching (.*?) finds the shortest possible match
Examples:
    Extracting first and last names from a formatted string:
        >>> name_pattern = re.compile(r'First Name: (.*) Last Name: (.*)')
        >>> name_match = name_pattern.search('First Name: Al Last Name: Sweigart')
        >>> name_match.group(1)
        'Al'
        >>> name_match.group(2)
        'Sweigart'
    Lazy matching finds the shortest match between angle brackets:
        >>> lazy_pattern = re.compile(r'<.*?>')
        >>> lazy_pattern.search('<To serve man> for dinner.>').group()
        '<To serve man>'
    Greedy matching finds the longest match between angle brackets:
        >>> greedy_re = re.compile(r'<.*>')
        >>> greedy_re.search('<To serve man> for dinner.>').group()
        '<To serve man> for dinner.>'
"""

import re


# You can use .*
# . = 'anything except newline'
# * = 'zero or more of the preceding char'
name_pattern = re.compile(r'First Name: (.*) Last Name: (.*)')

name_match = name_pattern.search('First Name: Al Last Name: Sweigart')

# Outputs 'Al'
print(name_match.group(1))

# Outputs 'Sweigart'
print(name_match.group(2))

# This uses the 'greedy mode', i.e. finds the longest string match
# To do it the 'lazy way', use dot, star, then question mark (.*?)
# Like when used with {}

# Outputs <To serve man>
lazy_pattern = re.compile(r'<.*?>')
match1 = lazy_pattern.search('<To serve man> for dinner.>')
print(match1.group())


# Outputs <To serve man> for dinner.>
greedy_re = re.compile(r'<.*>')
match2 = greedy_re.search('<To serve man> for dinner.>')
print(match2.group())