import re


# The below is a character class (in [])
# equivalent of r'a|e|i|o|u|A|E|I|O|U'

vowel_pattern = re.compile(r'[aeiouAEIOU]')

found_vowel_pattern = vowel_pattern.findall('RoboCop eats BABY FOOD.')

print(found_vowel_pattern)


# You can include ranges of letters or numbers with a hyphen, e.g.
# [a-zA-Z0-9] will match all lowercase & uppercase letters as well as numbers
alnum_pattern = re.compile(r'[a-zA-Z0-9]')

# Escape characters are unnecessary in character classes
# This will literally look for parentheses
paren_pattern = re.compile(r'[()]')


# To make a negative char class, just add a caret (^) just after opening brackets of char class
negative_pattern = re.compile(r'[^aeiouAEIOU]')

#Prints: ['R', 'b', 'C', 'p', ' ', 't', 's', ' ', 'B', 'B', 'Y', ' ', 'F', 'D', '.']
print(negative_pattern.findall('RoboCop eats BABY FOOD.'))


# You can use the shorthands \d for all 0-9, 
# \w for alnum and _ (including accented letters and other alphabets),
#  and \s for tab, space, newlines
# \D, \W, \S are 'everything but...' their lowercase counterparts
# There's no shorthand for just letters, nor something to include non-Roman alphabet letters

numbered_things = re.compile(r'\d+\s\w+')

# Outputs: ['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids',
#  '7 swans', '6 geese', '5 rings', '4 birds', '3 hens', '2 doves', '1 partridge']
print(numbered_things.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, \
                              7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))

# Any shorthand with '+' means 'one or more', e.g.
# \d+ = one or more numeric digits


# You also have . (or dot) which matches any char except newline, e.g.
at_re = re.compile(r'.at')
# Outputs: ['cat', 'hat', 'sat', 'lat', 'mat']
print(at_re.findall('The cat in the hat sat on the flat mat.'))

# To match actual full stops, \.