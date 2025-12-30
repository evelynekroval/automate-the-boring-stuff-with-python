"""
Lesson: When you pass a list to a function, the function can change the original list.
But when you pass a tuple or string, the function can't change it!

Why? Variables in Python point to values in memory (like name tags on boxes).
Lists are like erasable whiteboards inside boxes—anyone can erase and rewrite.
Tuples and strings are like permanent markers—you can't erase what's written.

Code: The eggs() function tries to add 'Hello' to whatever you give it.
It works for lists (mutable), but fails for tuples/strings (immutable).

Main Takeaways:
  • Mutable objects (lists, dicts) change when passed to functions
  • Immutable objects (tuples, strings, ints) can't be changed
  • Both types share the same reference, but immutable ones reject modifications
"""

# Remember that a list is a mutable object
# For the purposes of references, this means that `eggs` 
# modifies in place the real value ([1, 2, 3]) to which `spam` points
# NB! `spam` doesn't "store" the variable; 
# it's merely a reference to the value stored in memory, which is the list itself
spam = [1, 2, 3]

def eggs(some_parameter):
    try:
        # If the object is mutable
        some_parameter.append('Hello')
    except Exception as e:
        # If the object isn't mutable
        print(f"Error: {e}. Probably can't use `.append` on it, queen.") 
        
    

eggs(spam)
print(spam)  # Prints [1, 2, 3, 'Hello']


# But what if the object were immutable?
spam_tuple = (1, 2, 3)
spam_string= "123"
eggs(spam_tuple) 
eggs(spam_string)
