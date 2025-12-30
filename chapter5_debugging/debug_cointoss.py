import random
guess: int | str = '' 

while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    if guess == "heads":
        guess = 1
        break
    elif guess == "tails":
        guess = 0
        break
    else:
        continue

toss = random.randint(0, 1)  # 0 is tails, 1 is heads
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if guess == "heads":
        guess = 1
    elif guess == "tails":
        guess = 0
        
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')