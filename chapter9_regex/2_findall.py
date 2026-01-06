"""
Demonstrates the difference between findall() with grouped and ungrouped regex patterns.
This module shows how the re.findall() method behaves differently depending on
whether the regex pattern contains groups (parentheses) or not:
- Without groups: Returns a list of strings, where each string is a complete match.
- With groups: Returns a list of tuples, where each tuple contains the captured
    groups from a single match.
Examples:
        Ungrouped pattern r'\d{3}-\d{3}-\d{4}':
                ['415-555-9999', '212-555-0000']
        Grouped pattern r'(\d{3})-(\d{3})-(\d{4})':
                [('415', '555', '9999'), ('212', '555', '0000')]
"""
import re

pattern = re.compile(r'\d{3}-\d{3}-\d{4}') # This regex has no groups.
ungrouped_pattern = pattern.findall('Cell: 415-555-9999 Work: 212-555-0000')

print(f"This is what an ungrouped regex with the .findall() method looks like: \n {ungrouped_pattern}")

# This returns
# ['415-555-9999', '212-555-0000']
# i.e. a list of strs if no grouping in regex


# Meanwhile
pattern2 = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
grouped_pattern = pattern2.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(f"Meanwhile, this is what a grouped () regex with .findall() method looks like: \n {grouped_pattern}")

# This returns
# [('415', '555', '9999'), ('212', '555', '0000')]
# i.e. a list of tuples 
# where each tuple is a match, and 
# contains the strs for each grouping of regex