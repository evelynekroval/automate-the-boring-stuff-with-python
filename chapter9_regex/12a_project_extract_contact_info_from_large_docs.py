"""
Phone Number and Email Address Extractor

Extracts phone numbers and email addresses from file text.

High-level plan:
1. Get text from file
2. Find all phone numbers and email addresses
3. Paste results to new file

Implementation steps:
- Use os module for file operations
- Create regex patterns for phone numbers and email addresses
- Find all matches (not just first)
- Format matched strings
- Display message if no matches found
"""

# Step 1: Create regex for phone numbers

import re, os

old_file_path = "12b_first_text.txt"
new_file_path = "12c_new_text.txt"

phone_re = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  # Area code
    (\s|-|\.)?  # Separator
    (\d{3})  # First three digits
    (\s|-|\.)  # Separator
    (\d{4})  # Last four digits
    (\s*(ext|x|ext\.)\s*(\d{2,5}))?  # Extension
    )''', re.VERBOSE)

# Step 2: Create email regex.
email_re = re.compile(r'''(
                      [a-zA-Z0-9._%+-]+  # Username
                      @  # @ symbol
                      [a-zA-Z0-9.-]+  # Domain name
                    (\.[a-zA-Z]{2,4})  # Dot-something
    )''', re.VERBOSE)

# Step 3: Find matches in file text.
with open(old_file_path, 'r') as file:
    text = file.read()

matches = []

for groups in phone_re.findall(text):
    phone_num = '-'.join([groups[1], groups[3], groups[5]])
    if groups[6] != '':
        phone_num += ' x' + groups[6]
    matches.append(phone_num)

for groups in email_re.findall(text):
    matches.append(groups[0])
# Step 4: Copy results to the file.
if len(matches) > 0:
    with open(new_file_path, 'w') as new_file:
        new_file.write("\n".join(matches))
        print(f"Added to file: {new_file_path}")
        print("\n".join(matches))
else:
    print("No phone numbers or email addresses found.")