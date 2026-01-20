"""
Create a Mad Libs program that reads in text files 
and lets the user add their own text anywhere 
the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file. 

For example, a text file may look like this:

<The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
    unaffected by these events.>

The program would match these occurrences and prompt the user to replace them:

>>> Enter an adjective:
    silly
>>> Enter a noun:
    chandelier
>>> Enter a verb:
    screamed
>>> Enter a noun:
    pickup truck

    
It would then create the following text file:

<The silly panda walked to the chandelier and then screamed. A nearby
    pickup truck was unaffected by these events.>

The program should print the results to the screen in addition to saving them to a new text file.
"""
from pathlib import Path
import re

# 1 Reads text from a file

file_location = Path(r"C:\Users\Evelyne.Kroval1\Repos\automate-the-boring-stuff-with-python\chapter10_reading_writing_files\10_mad_libs_files")

with open(file_location / "example_text.txt", "r", encoding="UTF-8") as file_obj:
    content = file_obj.read()

# 2 Finds ADJECTIVE, NOUN, ADVERB, VERB in text file

pattern = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')
matches = re.findall(pattern, content)

# 3 Asks users for different adjective, noun, verb etc. based on number of found placeholders
saved_replacements = []

for match in matches:
    if match == "ADJECTIVE":
        saved_replacements.append(input("Enter an adjective\n"))
        continue
    elif match == "NOUN":
        saved_replacements.append(input("Enter a noun\n"))
        continue
    elif match == "ADVERB":
        saved_replacements.append(input("Enter an adverb\n"))
        continue
    else:
        saved_replacements.append(input("Enter a verb\n"))
        continue

# 5 Make the replacement
new_text = content

for index, item in enumerate(matches):
    new_text = pattern.sub(saved_replacements[index], new_text, count=1)



# 4 Print the output
print(new_text)

# 5 Create new file with updated output
with open(file_location / "new_text.txt", "w") as file:
    file.write(new_text)
    print("Your file this this content has been created and saved.")

