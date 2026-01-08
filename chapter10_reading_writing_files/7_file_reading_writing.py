"""
Demonstrates file reading and writing operations in Python using pathlib and built-in file methods.
This module covers three main aspects of working with files:
1. Reading files - extracting text content from existing files
2. Writing files - creating new files or modifying existing ones
3. Using 'with' statements - proper resource management for file operations
Key Concepts:
Reading Files:
- Use open() with 'r' mode (read mode - this is the default)
- Always specify encoding='UTF-8' for proper character rendering
- .read() returns the entire file as one string
- .readlines() returns a list where each line is a separate string (better for large files)
Writing Files:
- Use 'w' mode to write (overwrites existing content completely)
- Use 'a' mode to append (adds to the end of existing content)
- Always call .close() when done to save changes and free up system resources
- Remember to specify encoding='UTF-8' when writing too
The 'with' Statement (Context Manager):
- Automatically handles opening AND closing files
- Prevents resource leaks if your code crashes
- Cleaner syntax - no need to remember .close()
- The file automatically closes when the indented block ends
- This is the RECOMMENDED way to work with files in modern Python
Examples:
    Reading entire file as string:
        >>> with open('example.txt', encoding='UTF-8') as f:
        ...     content = f.read()
        ...     print(content)
        Hello, world!
    Reading file line by line:
        >>> with open('poem.txt', encoding='UTF-8') as f:
        ...     lines = f.readlines()
        ...     for line in lines:
        ...         print(line.strip())
        Roses are red
        Violets are blue
    Writing to a new file:
        >>> with open('output.txt', 'w', encoding='UTF-8') as f:
        ...     f.write('This is new content')
    Appending to existing file:
        >>> with open('log.txt', 'a', encoding='UTF-8') as f:
        ...     f.write('New log entry\n')
Common Mistakes to Avoid:
- Forgetting to close files (use 'with' to avoid this!)
- Not specifying encoding (can cause weird character issues)
- Using 'w' mode when you meant 'a' (you'll lose all existing content!)
- Trying to read a file that doesn't exist (causes FileNotFoundError)
Note:
    The 'with' statement is Python's way of guaranteeing cleanup operations happen,
    even if something goes wrong. It's like having a responsible friend who always
    turns off the lights when leaving a room, no matter how you exit!
"""

from pathlib import Path


###################
# 1 Reading Files #
###################

hello_file = open(Path.cwd() / "7_hello.txt", "r", encoding='UTF-8') 
# By default you get an ASCII encoding that doesn't look great, so specifying UTF-8 renders better results
# Default access mode is read_plaintext, i.e. "r", though we can specify too as 2nd arg

hello_content = hello_file.read()
print(hello_content)
# Output: the entire text in a whole string.

sonnet_file = open(Path.cwd() / "7_sonnet29.txt", "r", encoding="UTF-8")
print(sonnet_file.readlines())
# Output: a list of strings for each new line - recommended when dealing with larger files?

###################
# 2 Writing Files #
###################

# You can pass "w" for "write_plaintext" mode, or "a" for "append_plaintext" mode
# "w" overwrites
# "a" adds to end of file

bacon_file = open('7_bacon.txt', 'w', encoding='UTF-8') 
bacon_file.write('Hello, world!\n')
bacon_file.close()
bacon_file = open('7_bacon.txt', encoding='UTF-8')
content = bacon_file.read()
print(content)

bacon_file = open('7_bacon.txt', 'a', encoding='UTF-8') 
bacon_file.write('Bacon is not a vegetable.')
bacon_file.close()

bacon_file = open('7_bacon.txt', encoding='UTF-8')
content = bacon_file.read()
bacon_file.close()
print(content)

#######################
# 3 `with` Statements #
#######################

# `with` creates a 'context manager' manages resources
# e.g. files, network connections, or segments of memory, 
    # which often have setup and teardown steps 
    # during which the resource is allocated and later released so that other programs can make use of it. 
# Most commonly you'll see `with open()`

# Without `with`:
file_obj = open('7_without_with.txt', 'w', encoding='utf-8')
file_obj.write('Hello, world!')
file_obj.close()
file_obj = open('7_without_with', encoding='utf-8')
content = file_obj.read()
file_obj.close()

# With `with`:
with open('7_with_with.txt', 'w', encoding='UTF-8') as file_obj:
    file_obj.write('Hello, world!')
with open('7_with_with.txt', encoding='UTF-8') as file_obj:
    content = file_obj.read()

# Notice no close() as `with` automatically calls it when program execution leaves code block