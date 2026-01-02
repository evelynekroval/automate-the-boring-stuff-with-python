import random
import logging

logging.basicConfig(filename="./coinflip_test.txt",
                    level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

number_of_streaks = 0
h_streak = ['H'] * 6
t_streak = ['T'] * 6

logging.debug("h_streak is: %s", h_streak)
logging.debug("t_streak is: %s", t_streak)

for experiment_number in range(10000):
    logging.debug("Experiment number: %s", experiment_number)

    # Code to run the 100 experiments
    coin_flip_results = []
     
    for coin_flip in range(100):
        coin_flip_results.append(random.choice(['H','T']))
        
    logging.debug("The coin_flip_results now has %s items", len(coin_flip_results))
    
    # Code to check for 6 heads or tails in a row
    for i in range((100)-5):
        logging.debug("Checking round: %s", i)
        checking_list = coin_flip_results[i:(i+6)]
        if h_streak == checking_list or t_streak == checking_list:
            logging.debug("Checking h_streak against slice: %s", checking_list)
            number_of_streaks += 1
            logging.debug("Number of streaks now: %s", number_of_streaks)
        else:
            logging.debug("Condition false.")
            continue
    logging.debug(f"As of experiment number {experiment_number}, number of streaks is {number_of_streaks}.")

# Is this logic right? The final %age is in the range of 290% - is that appropriate...")        
logging.debug(f"Final number of streaks is {number_of_streaks}.")
# Do I need to add another 0 or something? As per exercise instructions, he said to divide by 100...
print(f'Chance of streak: {(number_of_streaks / 100)}%.')

# Exercise Instructions
"""Coin Flip Streaks
For this exercise, we’ll try doing an experiment. 
If you flip a coin 100 times and write down an H for each heads and a T for each tails, you’ll create a list that looks like T T T T H H H H T T. 
If you ask a human to make up 100 random coin flips, you’ll probably end up with alternating heads-tails results like H T H T H H T H T T—which looks random (to humans), but isn’t mathematically random. 
A human will almost never write down a streak of six heads or six tails in a row, even though it is highly likely to happen in truly random coin flips. 
Humans are predictably bad at being random.

Write a program to find out how often a streak of six heads or a streak of six tails comes up in a randomly generated list of 100 heads and tails. 
Your program should break up the experiment into two parts: the first part generates a list of 100 randomly selected 'H' and 'T' values, and the second part checks if there is a streak in it. Put all of this code in a loop that repeats the experiment 10,000 times so that you can find out what percentage of the coin flips contains a streak of six heads or six tails in a row. As a hint, the function call random.randint(0, 1) will return a 0 value 50 percent of the time and a 1 value the other 50 percent of the time.

You can start with the following template:

import random
number_of_streaks = 0
for experiment_number in range(10000):  # Run 100,000 experiments total.
    # Code that creates a list of 100 'heads' or 'tails' values

    # Code that checks if there is a streak of 6 heads or tails in a row

print('Chance of streak: %s%%' % (number_of_streaks / 100))

Of course, this is only an estimate, but 10,000 is a decent sample size. 
Some knowledge of mathematics could give you the exact answer and save you the trouble of writing a program, but programmers are notoriously bad at math.

To create a list, use a for loop that appends a randomly selected 'H' or 'T' to a list 100 times. 
To determine if there is a streak of six heads or six tails, create a slice like some_list[i:i + 6] (which contains the six items starting at index i) and then compare it to the list values ['H', 'H', 'H', 'H', 'H', 'H'] and ['T', 'T', 'T', 'T', 'T', 'T'].
"""