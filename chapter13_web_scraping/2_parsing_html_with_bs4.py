

# Beautiful Soup is a package for extracting information from an HTML page. 
"""
Demonstrates parsing HTML content using Beautiful Soup 4 library.
This module shows two methods of creating BeautifulSoup objects:
1. Parsing HTML from a web URL using the requests library
2. Parsing HTML from a local file
It also demonstrates how to:
- Select elements using CSS selectors (e.g., by ID with '#author')
- Work with ResultSet and Tag objects returned by select()
- Extract text content from Tag objects using get_text()
- Access element attributes via the attrs property
- Convert Tag objects to strings
Example:
    The code fetches HTML from 'https://autbor.com/example3.html' and 
    'example3.html' file, then searches for elements with id='author' and 
    extracts their text content and attributes.
Note:
    Requires the beautifulsoup4 and requests packages to be installed.
"""
# You’ll use the name beautifulsoup4 to install the package 
# but the shorter module name bs4 to import it. 
# 
# In this section, we’ll use Beautiful Soup to parse 
# (that is, analyze and extract the parts of) 
# the HTML file at https://autbor.com/example3.html.

import requests, bs4

res = requests.get('https://autbor.com/example3.html')

res.raise_for_status()

example_soup = bs4.BeautifulSoup(res.text, 'html.parser')

type(example_soup)
# Produces a bs4.BeautifulSoup object!

# You can also load an HTML file from your hard drive 
# by passing a File object to bs4.BeautifulSoup(). 
#  Enter the following into the interactive shell 
# (after making sure the example3.html file is in the working directory):
with open('example3.html') as example_file:
    example_soup2 = bs4.BeautifulSoup(example_file.read(), 'html.parser')
    
type(example_soup2)

elems = example_soup2.select('#author')

type(elems)
# # elems is a list of Tag objects.
# <class 'bs4.element.ResultSet'>

# Tell us how many matches there were to our #author search
len(elems)
# It's 1, so:

type(elems[0])
# <class 'bs4.element.Tag'>

# You can pass Tag objects to str() to see their content
str(elems[0])
# '<span id="author">Al Sweigart</span>'

elems[0].get_text()  # The inner text of the element
# 'Al Sweigart'

elems[0].attrs
# {'id': 'author'}