"""
Demonstrates the difference between default regex matching and DOTALL mode.
This module shows how the dot (.) metacharacter behaves differently with and
without the re.DOTALL flag when matching strings containing newline characters.
By default, the dot (.) matches any character except newline (\n). When the
re.DOTALL flag is used, the dot matches all characters including newlines.
Examples:
    Without re.DOTALL:
        - Pattern '.*' matches only up to the first newline
        - Result: 'Serve the public trust.'
    With re.DOTALL:
        - Pattern '.*' matches across newlines
        - Result: 'Serve the public trust.\nProtect the innocent. \nUphold the law.'
"""

import re
# .* matches everything except newline

no_newline_re = re.compile('.*')

# Outputs 'Serve the public trust.'

print(no_newline_re.search('Serve the public trust.\nProtect the innocent. \nUphold the law.').group())

# passing re.DOTALL as the 2nd argument to re.compile() can make the dot match ALL chars

newline_re = re.compile('.*', re.DOTALL)

# Outputs 'Serve the public trust.\nProtect the innocent.\nUphold the law.'
print(newline_re.search('Serve the public trust.\nProtect the innocent. \nUphold the law.').group())