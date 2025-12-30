while True:
    number = int(input("Enter an integer:\n"))
    
    if number == 0:
        break
    elif number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz!")
    elif number % 3 == 0:
        print("Fizz!")
    elif number % 5 == 0:
        print("Buzz!")
    else:
        print(number)