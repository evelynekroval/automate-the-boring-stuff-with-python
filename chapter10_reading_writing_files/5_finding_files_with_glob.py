"""The * and ? characters can be used to match folder names and filenames in what are called glob patterns. 
Glob patterns are like a simplified regex language: 
- the * character matches any text, and 
- the ? character matches exactly one character. 


For example, look at these glob patterns:
- '*.txt' matches all files that end with .txt.
- 'project?.txt' matches 'project1.txt', 'project2.txt', or 'projectX.txt'.
- '*project?.*' matches 'catproject5.txt' or 'secret_project7.docx'.
- '*' matches all filenames.

Path objects of folders have a glob() method for listing any content in the folder that matches the glob pattern. 
"""

from pathlib import Path


# The glob() method returns a generator object that you’ll need to pass to list()
p = Path('C:/Users/Evelyne.Kroval1/Downloads')

print(list(p.glob('*')))

# Or better yet, iterate with a for loop the generator object

for name in p.glob('*'):
    print(name)