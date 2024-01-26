#!/usr/bin/python3

def add_up(*numbers):
	total = 0
	for number in numbers:
		total += number
	return total

count = add_up(1, 3, 2)
print(count)
