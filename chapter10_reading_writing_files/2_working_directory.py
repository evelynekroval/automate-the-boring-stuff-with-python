
from pathlib import Path
"""
Demonstrates working with directories using pathlib and os modules.
This module covers essential directory operations in Python:
- Getting the current working directory with Path.cwd()
- Changing directories with os.chdir() (no pathlib equivalent exists)
- Accessing the user's home directory with Path.home()
- Understanding absolute vs relative paths
- Converting between absolute and relative paths
- Creating new directories with os.makedirs()
Key Concepts:
- Absolute paths start from the root folder (e.g., C:\ on Windows, / on Unix)
- Relative paths are relative to the current working directory
- Single dot (.) represents the current directory
- Double dot (..) represents the parent directory
- Use Path.absolute() or Path.cwd() / relative_path to convert relative to absolute
Examples:
    Get current directory:
        >>> Path.cwd()
        WindowsPath('C:/Users/Username/project')
    Change directory:
        >>> os.chdir('../')
        >>> Path.cwd()
        WindowsPath('C:/Users/Username')
    Check if path is absolute:
        >>> Path.cwd().is_absolute()
        True
        >>> Path('spam/bacon/eggs').is_absolute()
        False
    Convert relative to absolute:
        >>> Path('my/relative/path').absolute()
        WindowsPath('C:/Users/Username/my/relative/path')
    Create nested directories:
        >>> os.makedirs(Path('parent/child/grandchild'))
Note:
    os.chdir() is required for changing directories as pathlib doesn't provide
    this functionality. For creating directories, use os.makedirs() with Path objects
    for cross-platform compatibility.
"""
import os


# You can get the current working directory as a str with Path.cwd()
print(f"Your current directory is: {Path.cwd()}") 

# You can change it with os.chdir(). 
# There is no pathlib function for changing the working directory. You must use os.chdir().
os.chdir("../")

print(f"Your new directory is: {Path.cwd()}")

############################
# Accessing home directory #
############################
print(f"Your home directory: {Path.home()}")

###############################
# Absolute and Relative Paths #
###############################

# Absolute always begins with root folder

# Whereas relative are in relation to current working directory
# A single period (dot) for a folder name is shorthand for this folder. 
# Two periods (dot-dot) means the parent folder.

print("Checking if the directory you're in (with .cwd()) is an absolute path:",
      Path.cwd().is_absolute(),
      "And now whether Path('spam/bacon/eggs') is absolute:",
      Path('spam/bacon/eggs').is_absolute(),
      sep="\n")

# To get an absolute path from your relative path,
# You can put `Path.cwd() /`` in front of it
# Or you can just Path('what/ever').absolute()

print("The relative path looks like:",
      Path('my/relative/path'),
      "And now if we add it with .cwd() /",
      Path.cwd() / Path('my/relative/path'),
      "You could've achieved the same with .absolute() on Path('my/relative/path')",
      Path('my/relative/path').absolute(),
      sep="\n")

########################
# Creating New Folders #
########################
# os.makedirs(Path(r"C:\Users\Evelyne.Kroval1\Repos\automate-the-boring-stuff-with-python\chapter10_reading_writing_files\2_testDir\2_1_TestDir2"))
# print("You've now created 2 subfolders in this chapter's folder.")