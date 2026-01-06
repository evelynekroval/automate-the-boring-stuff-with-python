"""
Demonstrates verbose mode in regular expressions for improved readability.
This module shows how to use the re.VERBOSE flag to write more maintainable regex
patterns by allowing multi-line formatting, whitespace, and inline comments.
Regular expressions can become difficult to read when matching complex patterns.
The re.VERBOSE flag (or re.X) allows you to:
- Break the pattern across multiple lines
- Add whitespace for visual grouping (which will be ignored)
- Include inline comments to explain each part of the pattern
Example:
    Complex phone number pattern without verbose mode:
        >>> pattern = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext\.)\s*\d{2,5})?)')
    Same pattern with verbose mode for clarity:
        >>> pattern = re.compile(r'''(
        ...     (\d{3}|\(\d{3}\))?            # Area code (optional)
        ...     (\s|-|\.)?                     # Separator (space, dash, or dot)
        ...     \d{3}                          # First three digits
        ...     (\s|-|\.)                      # Separator
        ...     \d{4}                          # Last four digits
        ...     (\s*(ext|x|ext\.)\s*\d{2,5})? # Extension (optional)
        ...     )''', re.VERBOSE)
Note:
    The verbose pattern matches phone numbers like:
    - 415-555-1234
    - (415) 555-1234
    - 415.555.1234 ext 12345
"""

import re


# Regex is straightforward when looking for a simple pattern
# Sometimes, you may be looking for something very specific and lengthy

# E.g. this is hard to read:
unforgiving_pattern = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext\.)\s*\d{2,5})?)')

# You can spread this out by using multiline r-str (r''') and also passing as 2nd arg re.VERBOSE:
# This ignores whitespaces and comments
better_pattern = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  # Area code
    (\s|-|\.)?  # Separator
    \d{3}  # First three digits
    (\s|-|\.)  # Separator
    \d{4}  # Last four digits
    (\s*(ext|x|ext\.)\s*\d{2,5})?  # Extension
    )''', re.VERBOSE)

# Although tbh it's best to used the Humre module...