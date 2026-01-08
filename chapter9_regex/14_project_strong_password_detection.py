"""
Project: Strong Password Detection
Write a function that uses regular expressions to make sure the password string it is passed is strong. 
A strong password has several rules: it must:
- be at least eight characters long, 
- contain both uppercase and lowercase characters, and 
- have at least one digit. 
Hint: It’s easier to test the string against multiple regex patterns 
than to try to come up with a single regex that can validate all the rules."""

import logging

# Adding logging for more visibility...

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# And disabling at the end...

import re

# 1: Creating functions for each regex:

# Length regex
def password_length_test(text: str):
    length_regex = re.compile(r'.{8,}')
    logging.debug("bool(length_regex.search(text)) is %s" % bool(length_regex.search(text)))
    logging.debug("length_regex.search(text): %s" % length_regex)
    return bool(length_regex.search(text))


# Upper and lower chars regex
def password_upper_lower_test(text:str):
    lower_regex = re.compile(r'[a-z]+')
    upper_regex = re.compile(r'[A-Z]+')
    logging.debug("lower_regex.search(text) is %s" % lower_regex.search(text))
    logging.debug("upper_regex.search(text) is %s" % upper_regex.search(text))
    if lower_regex.search(text):
        if upper_regex.search(text):
            return True

# At least 1 number regex
def password_one_num_test(text:str):
    decimal_regex = re.compile(r'\d+')
    logging.debug("decimal_regex is %s" % bool(decimal_regex.search(text)))
    return bool(decimal_regex.search(text))


# The main function which runs them all in logical order
def strong_password_detector(text: str):
    try:

        if not password_length_test(text):
           return "Your password is too short."
            
        else:
            if password_upper_lower_test(text) and password_one_num_test(text):
                return "Congratulations! Your password is strong enough."
            else:
                return "Your password requires upper and lower characters, and at least one number."
             
                
       
    except Exception as e:
        print(f"ERROR: {e}.")

# print(password_length_test("aBca"))
# Testing the function
while True:
    password_test = str(input("Input a password: \n> "))
    if strong_password_detector(password_test) == "Congratulations! Your password is strong enough.":
        print(strong_password_detector(password_test))
        break
    else:
        print(strong_password_detector(password_test))
        continue
# password_test = "aBcas3dgaass"
# strong_password_detector(password_test)
