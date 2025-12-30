import sys

def collatz(number: int):
    if number % 2 == 0:
        collatzed_number=number // 2
    else:
        collatzed_number=3 * number + 1
    return collatzed_number
while True:
    try:
        try:
            number = int(input("\nEnter number:\n>"))
            while number != 1:
                number = collatz(number)
                print(number, end= " ")
        except ValueError:
            print("You must enter an integer.")
    except:
        sys.exit()
