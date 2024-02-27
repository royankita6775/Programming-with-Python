# 4.2

import random

x = int(input("How many sets of lottery numbers do you want? "))

def lottery(x):
    for x in range(x):
        lottery_numbers = random.sample(range(1,41), 7)    # using random.sample() function to select unique elements
        lottery_numbers = sorted(lottery_numbers)
        print(lottery_numbers)
  
lottery(x)
