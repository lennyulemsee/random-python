#!/usr/bin/python3

my_list = [1, (3, 4, ("another", "tuple")), 2, 3, 4, 5] 
new_list = my_list.copy()
print(new_list) 
new_list[0] = 9
print(new_list)
print(my_list)
