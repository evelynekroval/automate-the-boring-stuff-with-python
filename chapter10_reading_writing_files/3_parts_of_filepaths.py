"""The parts of a filepath include the following:

- The **anchor**, which is the root folder of the filesystem
- On Windows, the **drive**, which is the single letter that often denotes 
        a physical hard drive or other storage device
- The **parent**, which is the folder that contains the file
- The **name&& of the file, made up of the **stem** (or base name) and the **suffix** (or extension)

These are all extensions """

from pathlib import Path

p = Path('C:/Users/Evelyne.Kroval1/example.txt')

PARTS_OF_FILEPATH = f"""
Given {p},

The anchor is {p.anchor},
The parent is {p.parent},
The name is {p.name},
The stem is {p.stem}, 
with suffix {p.suffix}.
This is in drive {p.drive}. 

"""

print(PARTS_OF_FILEPATH)


print(f"You can get the parts as a tuple of strings with p.parts: {p.parts}")

# The `parents` attribute (which is different from the `parent` attribute)
# evaluates to the ancestor folders of a Path object with an integer index:

PARENTS = f"""
The current working directory is: {Path.cwd()}.

Parents[0] is: {Path.cwd().parents[0]}
Parents[1] is: {Path.cwd().parents[1]}
Parents[2] is: {Path.cwd().parents[2]}

Note that it works 'backwards' towards root folder"""

print(PARENTS)