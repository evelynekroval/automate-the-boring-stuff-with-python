"""
Demonstrates combining multiple regex flags using the bitwise OR operator.
This module shows how to apply multiple regex compilation flags simultaneously
by using the bitwise OR operator (|) to combine them. Since re.compile() accepts
only a single value as its second argument, multiple flags must be combined using
the pipe character.
Examples:
    Combining IGNORECASE and DOTALL flags:
        >>> some_regex = re.compile('foo', re.I | re.DOTALL)
        >>> # Matches 'foo' case-insensitively and allows dot to match newlines
    Combining all three common flags:
        >>> another_regex = re.compile('huh', re.IGNORECASE | re.DOTALL | re.VERBOSE)
        >>> # Case-insensitive, dot matches newlines, and verbose mode enabled
Note:
    The following flag combinations are equivalent:
    - re.I is the same as re.IGNORECASE
    - re.S is the same as re.DOTALL
    - re.X is the same as re.VERBOSE
"""

import re


# Unfortunately, re.compile() accepts only a single value as its 2nd arg

# So use the **bitwise or operator** (|, the pipe char)

# Lo a case-sensitive regex which includes newlines:

some_regex = re.compile('foo', re.I | re.DOTALL)

# or with all 3 options:

another_regex = re.compile('huh', re.IGNORECASE | re.DOTALL | re.VERBOSE)