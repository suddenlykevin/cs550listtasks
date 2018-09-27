# Completed List Task 1
# CS550 9/27/2018
# Kaki, Stephanie, Alex, Daniel: 
# Take two values, base and exponent, from the user. Then create a list
# that displays the exponents of that base from the 0 power (1) to the
# [entered exponent] power in ascending order. For example, if the base
# was 2 and the exponent was 5, the list should show [1, 2, 4, 8, 16, 32]

import sys
intlist = []

try:
	base = int(sys.argv[1])
	exp = int(sys.argv[2])
	for x in range(exp+1):
		intlist.append(base**x)
	print(intlist)
except ValueError:
	print("Please enter valid arguments (integers)")
except NameError:
	print("Please enter valid arguments (integers)")