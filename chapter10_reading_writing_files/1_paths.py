""""""
"""
Demonstrates basic usage of the pathlib.Path class for cross-platform file path handling.
This module shows how to create and manipulate file paths in a platform-independent way
using Python's pathlib module. The Path class automatically handles differences between
Windows, macOS, and Linux path separators.
Key concepts demonstrated:
- Creating Path objects with multiple path components
- Iterating over filenames and joining them with base paths
- Using the / operator to join paths (replaces os.path.join())
- Path objects work consistently across different operating systems
Examples:
    Creating a simple path:
        >>> Path('spam', 'bacon', 'eggs')
        WindowsPath('spam/bacon/eggs')  # or PosixPath on Unix systems
    Joining paths with existing directory:
        >>> for filename in ['accounts.txt', 'details.csv']:
        ...     print(Path(r'C:\Users\Evie', filename))
        C:\Users\Evie\accounts.txt
        C:\Users\Evie\details.csv
    Using the / operator for path concatenation:
        >>> Path('spam') / 'bacon' / 'eggs'
        WindowsPath('spam/bacon/eggs')
Note:
    The / operator only works when the left operand is a Path object.
    This approach is preferred over os.path.join() in modern Python code.
"""

from pathlib import Path


# To create a file path, independent of system (MacOS, Windows, Linux...)
print("Creating a file path:",
      Path('spam', 'bacon', 'eggs'),
      type(Path('spam', 'bacon', 'eggs')),
      sep="\n")

# The WindowsPath or POSIX or whatever need never appear in source code, you can just rely on Path()
my_files = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in my_files:
    print(Path(r'C:\Users\\Evie', filename))


# As long as you have a Path() on the left, you can join strs or other Path()s with the / operator
# This replaces the older os.path.join()

print("Joining paths:",
      (Path('spam') / 'bacon' / 'eggs'),
      (Path('spam') / Path('bacon/eggs')),
      (Path('spam') / Path('bacon', 'eggs')),
      sep="\n"
      )