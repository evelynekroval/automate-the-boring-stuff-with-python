# Copilot Instructions for automate-the-boring-stuff-with-python

## Overview
This repository contains practice code and examples from "Automate the Boring Stuff with Python." The goal is to learn Python fundamentals through hands-on coding exercises.

## Primary Instruction: Simplify Docstrings to ELI5 Format

When asked to improve or add docstrings to any file in this repository, **simplify and shorten them into an ELI5 (Explain Like I'm 5) format** that covers three key sections:

### Required Sections:
1. **Lesson**: What the concept being taught is, in simple terms
2. **Code**: What the code does and how it works
3. **Main Takeaways**: 2-3 bullet points with the key learnings

### Style Guidelines:
- Use plain language, avoid jargon
- Use analogies and metaphors when helpful (e.g., "name tags on boxes," "erasable whiteboards")
- Keep the total docstring concise (10-15 lines)
- Remove redundant information and examples that don't add clarity
- Make it memorable and accessible to beginners

### Example:
```python
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
```

## General Guidelines

- **Keep code educational**: Comments should explain the "why," not just the "what"
- **Be consistent**: Follow the ELI5 format across all files for consistency
- **Test your code**: Ensure examples in docstrings actually work
- **Target beginners**: Remember the audience is learning Python fundamentals

---

Last Updated: December 30, 2025
