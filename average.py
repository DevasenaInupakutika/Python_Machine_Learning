#! /usr/bin/env python

def average_list(pylist):
    average = 0
    sum = 0
    print type(pylist)
    #assert type(pylist) is str, 'TypeError: The list is not a number list'

    for n in pylist:
        sum = sum + n    
    average = sum/ len(pylist)
    return (sum, average)

list1 = [1,2,3,4,5]
list2 = []
list3 = ["Devasena", "Hemaroop"]
list4 = [0.1,0.2,0.3]

print average_list(list1)       
print average_list(list2)
