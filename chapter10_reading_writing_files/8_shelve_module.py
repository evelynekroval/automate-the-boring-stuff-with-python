"""
You can save variables in your Python programs to binary shelf files using the `shelve` module. 
This lets your program restore that data to the variables the next time it is run. 
You could use this technique to add Save and Open features to your program; 
for example, if you ran a program and entered some configuration settings, 
you could save those settings to a shelf file 
and then have the program load the settings the next time it is run.
"""

import shelve
shelf_file = shelve.open('8_mydata')
shelf_file['cats'] = ['Zophie', 'Pooka', 'Simon']
# You can make changes to the shelf value as if it were a dict
shelf_file.close()

# Shelf values don’t have to be opened in read or write mode; they allow both reading and writing once opened. 


# Just like dicts, shelf values have keys() and values() methods 
# that will return list-like values of the keys and values in the shelf. 
# Because these return values are not true lists, 
# you should pass them to the list() function to get them in list form.

shelf_file = shelve.open('8_mydata')
print(list(shelf_file.keys()),
      list(shelf_file.values()),
      sep="\n"
)
shelf_file.close()

# Plaintext is useful for creating files that you’ll read in a text editor such as Notepad or TextEdit, 
# but if you want to save data from your Python programs, use the shelve module.