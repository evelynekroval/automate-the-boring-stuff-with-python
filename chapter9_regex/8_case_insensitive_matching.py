
"""
Demonstrates case-insensitive regex matching using the re.IGNORECASE flag.
This module shows how to perform case-insensitive pattern matching by passing
re.IGNORECASE (or re.I) as a flag to re.compile(). The example searches for
the word 'robocop' in strings with different capitalizations (RoboCop, ROBOCOP,
and robocop) and successfully matches all variations.
Example:
    The pattern matches 'robocop' regardless of case:
    - 'RoboCop' matches
    - 'ROBOCOP' matches
    - 'robocop' matches
"""
import re

# Normally regex are case-sensitive, e.g. 'RoboCop' != "ROBOCOP" etc.

# If you want case-insensitive search, pass re.IGNORECASE or re.I as an arg to re.compile()
pattern = re.compile(r'robocop', re.I)

# The below return 'RoboCop', 'ROBOCOP', and 'robocop' respectively
print(pattern.search('RoboCop is part man, part machine, all cop.').group())
print(pattern.search('ROBOCOP protects the innocent.').group())
print(pattern.search('Have you seen robocop?').group())

