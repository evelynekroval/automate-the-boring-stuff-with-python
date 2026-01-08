"""Project: Regex Version of the strip() Method

Write a function that takes a string and does the same thing as the strip() string method. 
If no other arguments are passed other than the string to strip, 
then the function should remove whitespace characters from the beginning and end of the string. 

Otherwise, the function should remove the characters specified in the second argument to the function."""

import re
import logging
logging.disable(logging.INFO)

# Adding logging for more visibility...

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def strip_replacement(string: str, thing_to_strip: str=None):
    if not thing_to_strip:
        logging.debug("No 2nd argument pathway.")
        start_spaces = re.compile(r'^\s+')
        end_spaces=re.compile(r'\b\s+')
        substituted_no_spaces = start_spaces.sub("", string)
        substituted_no_spaces = end_spaces.sub("", substituted_no_spaces)
        return(substituted_no_spaces)
    else:
        replacement_str = re.compile(thing_to_strip)
        logging.debug("2nd argument pathway.")
        replaced_text = replacement_str.sub("", string)
        return replaced_text

while True:
    test_string = input("Input a string: \n> ")
    remove_test = input("And character to remove: (You can press ENTER to skip argument)\n> ")
    print(f"You said: '{test_string}'")
    no_spaces_string = strip_replacement(test_string, remove_test)
    print(f"Your string is now: '{no_spaces_string}'")


