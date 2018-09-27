# List Challenge:
# Allow 10 random integers to be entered as arguments
# catch any potential errors
# print them sorted from small to large, then large to small, and then print the sum

import sys

g=[]

for x in range(1,11):
	try:
		g.append(int(sys.argv[x]))
	except IndexError:
		print("Please try again with 10 integers")

print(sorted(g))
print(sorted(g,reverse=True))
print(sum(g))
