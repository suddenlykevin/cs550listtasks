# Completed List Task 3
# CS550 9/27/2018
# Ms. Healey: 
# Generate a list of 100 numbers, 1 to 100, without using a traditional  
# looping technique (investigate list comprehensions). Shuffle the list up  
# so the numbers are not in order.  

import random

intlist = list(map(random.randrange, [101]*100)) # random list w/o looping: https://stackoverflow.com/questions/44493500/how-can-i-generate-n-random-numbers-without-a-for-loop
print(intlist)
random.shuffle(intlist) # Shuffling list: https://stackoverflow.com/questions/976882/shuffling-a-list-of-objects
print(intlist)