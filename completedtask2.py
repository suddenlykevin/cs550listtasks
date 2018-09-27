# Completed List Task 2
# CS550 9/27/2018
# Anjali, Sonali, Mia: 
# Generate a list of 15 random numbers from 0-100. Ask the user for one
# input from 0-100. Append this input to the list. Sort the list into
# descending order.

import random

intlist=[]

for x in range(15):
	intlist.append(random.randrange(100))

while True:
	try:
		append = int(input("Please enter an integer from 0-100 \n>>> "))
		if 0<=append<=100:
			break
	except ValueError:
		pass
	print("That's not a valid integer.")

intlist.append(append)

print(sorted(intlist, reverse=True))