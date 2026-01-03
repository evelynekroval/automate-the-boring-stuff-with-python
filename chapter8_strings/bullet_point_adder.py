#import pyperclip
#text = pyperclip.paste()

# e.g. text 
text_example = '''Lists of animals\nLists of aquarium life\nLists of biologists by author abbreviation\nLists of cultivars'''

# TODO: Separate lines and add stars.

def separate_lines_to_add_stars(text: str) -> None:
    '''When a single line of text with newlines is input, 
    the output is a print statement of a str 
    which now has bullet points alongside the new lines.'''
    
    lines = text.split('\n') # produces list[str]
    
    for i in range(len(lines)):
        lines[i] = '* '+ lines[i]
    
    text = '\n'.join(lines)
    
    print(text)

separate_lines_to_add_stars(text_example)

# pyperclip.copy(text)