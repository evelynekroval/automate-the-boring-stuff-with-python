"""
Write a program that opens all .txt files in a folder 
and searches for any line that matches a user-supplied regular expression, 
then prints the results to the screen.
"""

import os
from pathlib import Path
import re
import pprint

# Open all txt files in a folder

def directory_navigator():
    """Navigates to user-selected directory - requires absolute path of an existing directory.
    Then navigates to selected directory. Returns the path of new current directory."""
    is_Valid = False
    while not is_Valid:
        p = Path(input("Please input absolute path of folder containing txts.\n> "))
        if p.exists() and p.is_dir() and p.is_absolute():
            print("Thank you for the valid path.")
            os.chdir(p)
            print(f"We are now inside {Path.cwd()}.")
            is_Valid = True
        else:
            print("Ensure this is a valid absolute path to an existing directory.")
    return p


# Search for anything the user asks.

def txt_chunk_selector():
    """Asks user to input the string they are looking for.
    Compiles input to a Regex, and returns the Regex search pattern for further use."""
    search_chunk = input("What text chunk are you searching for? Type freely, no quotation marks required.\n> ")
    print(f"Searching for: {search_chunk}")
    search_pattern = re.compile(search_chunk)
    return search_pattern


# Run search using phrase

def txt_searcher():
    search_results = []
    directory = directory_navigator()
    search = txt_chunk_selector()


    for file in directory.glob("*.txt"):
        with open(file, "r") as individual_file:
            content = individual_file.read()
            individual_result = search.findall(content)
            if individual_result:
                search_results.append(file.name)
                print(f"Query found in: {file.name}.")
            else:
                continue
    print(f"Found {len(search_results)} matches for your query.")

txt_searcher()
