import re
from humre import *

# If we go back to the r'\d{3}-\d{3}-\d{4} example, Humre allows a more readable option:
phone_regex = exactly(3, DIGIT) + '-' + exactly(3,DIGIT) + '-' + exactly(4, DIGIT)
print(phone_regex)