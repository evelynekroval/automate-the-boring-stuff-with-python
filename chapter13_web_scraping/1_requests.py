
# Yay we finally get to look at web scraping and such
"""
Module demonstrating basic use of the requests library to retrieve web content
and save it to disk.

This script shows:
- Performing HTTP GET requests with requests.get(url).
- Verifying success via response.status_code or response.raise_for_status().
- Accessing text content via response.text and checking its length.
- Handling failed requests gracefully with try/except around raise_for_status().
- Saving a response to a file by opening a file in binary mode ('wb') and
    writing bytes from response.iter_content(chunk_size) in a loop to preserve
    encoding and handle large responses incrementally.

Typical workflow:
1. response = requests.get(url)
2. response.raise_for_status()  # or check response.status_code
3. inspect response.text or len(response.text)
4. with open(filename, 'wb') as f: for chunk in response.iter_content(chunk_size): f.write(chunk)

Notes:
- Always open the output file in binary mode when writing response.iter_content()
    to avoid encoding issues.
- Choose a sensible chunk_size (e.g., 100000) to balance memory and I/O.
"""

import requests

# You use the .get() method for the link
# You also probably wanna save the thing in a variable
response = requests.get('https://automatetheboringstuff.com/files/rj.txt')

# If you check the type
type(response)
# You'll see it's a Response object:
# <class 'requests.models.Response'>

# You can validate the request went through via
response.status_code == requests.codes.ok

# Or by using the .raise.for.status() method, which
# Will raise an exception if no content received, 
# or any other problems
response.raise_for_status()

# To check the length of what you've received, you can 
# access the .text attribute like so
len(response.text)

# If we print the text up to the 211th char from the beginning, 
# we see this was the Romeo & Juliet text...
print(response.text[:210])


# The raise_for_status() method is 
# an easy way to ensure that a program halts 
# if a bad download occurs. 
# Generally, you’ll want your program to stop 
# as soon as some unexpected error happens. 
# If a failed download isn’t a deal breaker, 
# you can wrap the raise_for_status() line 
# with try and except statements to handle this error 
# case without crashing:

response = requests.get('https://inventwithpython.com/page_that_does_not_exist')
try:
    response.raise_for_status()
except Exception as exc:
    print(f'There was a problem: {exc}')


# Once page is retrieved, you can save file to hard drive
# with the standard open() and .write() - but you must
# open in `write binary`i.e. 'wb'
# Even if plaintext, you need to write binary data instead
# of text data to maintain Unicode encoding of text

# To write the web page to a file, you can use a for loop
# with the Response object's .iter_content() method:
with open('RomeoAndJuliet.txt', 'wb') as play_file:
    for chunk in response.iter_content(100000):
        play_file.write(chunk)

# The iter_content() method returns “chunks” 
# of the content on each iteration through the loop. 
# Each chunk is of the bytes data type, a
# nd you get to specify how many bytes each chunk will contain. 
# One hundred thousand bytes is generally a good size, 
# so pass 100000 as the argument to iter_content().