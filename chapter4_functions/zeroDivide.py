def spam(divide_by):
    try:
        # Any code in this block that causes ZeroDivisionError won't crash the program:
        return 42 / divide_by
    except Exception as e:
        # If ZeroDivisionError happened, the code in this block runs:
        print(f'Error: {e}. Try again.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))