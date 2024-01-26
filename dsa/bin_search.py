#!/usr/bin/python3

def binary_search(li, querry):
    hi = len(li) - 1
    lo = 0

    while(lo <= hi):
        mid = (hi + lo) // 2
        mid_num = li[mid]
        print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_num)

        if li[mid] == querry:
            return mid
        elif querry < li[mid]:
            hi = mid - 1
        elif querry > li[mid]:
            lo = mid + 1
    return -1

test = {
        'input': {
            'arr': [1, 3, 4, 6, 8, 8, 10, 12, 13, 15, 17, 18, 19, 21],
            'querry': 18 
            },
        'output': 11
        }

ans = binary_search(test['input']['arr'], test['input']['querry'])
print(ans)
