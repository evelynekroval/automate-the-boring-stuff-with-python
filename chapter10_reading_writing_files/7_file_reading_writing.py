from pathlib import Path

###################
# 1 Reading Files #
###################

hello_file = open(Path.cwd() / "7_hello.txt", "r", encoding='UTF-8') 
# By default you get an ASCII encoding that doesn't look great, so specifying UTF-8 renders better results
# Default access mode is read_plaintext, i.e. "r", though we can specify too as 2nd arg

hello_content = hello_file.read()
print(hello_content)
# Output: the entire text in a whole string.

sonnet_file = open(Path.cwd() / "7_sonnet29.txt", "r", encoding="UTF-8")
print(sonnet_file.readlines())
# Output: a list of strings for each new line - recommended when dealing with larger files?

###################
# 2 Writing Files #
###################

# You can pass "w" for "write_plaintext" mode, or "a" for "append_plaintext" mode
# "w" overwrites
# "a" adds to end of file

bacon_file = open('7_bacon.txt', 'w', encoding='UTF-8') 
bacon_file.write('Hello, world!\n')
bacon_file.close()
bacon_file = open('7_bacon.txt', encoding='UTF-8')
content = bacon_file.read()
print(content)

bacon_file = open('7_bacon.txt', 'a', encoding='UTF-8') 
bacon_file.write('Bacon is not a vegetable.')
bacon_file.close()

bacon_file = open('7_bacon.txt', encoding='UTF-8')
content = bacon_file.read()
bacon_file.close()
print(content)

#######################
# 3 `with` Statements #
#######################

# `with` creates a 'context manager' manages resources
# e.g. files, network connections, or segments of memory, 
    # which often have setup and teardown steps 
    # during which the resource is allocated and later released so that other programs can make use of it. 
# Most commonly you'll see `with open()`

# Without `with`:
file_obj = open('7_without_with.txt', 'w', encoding='utf-8')
file_obj.write('Hello, world!')
file_obj.close()
file_obj = open('7_without_with', encoding='utf-8')
content = file_obj.read()
file_obj.close()

# With `with`:
with open('7_with_with.txt', 'w', encoding='UTF-8') as file_obj:
    file_obj.write('Hello, world!')
with open('7_with_with.txt', encoding='UTF-8') as file_obj:
    content = file_obj.read()

# Notice no close() as `with` automatically calls it when program execution leaves code block