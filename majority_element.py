"""
Problem: Given an array of numbers(integers) determine the mode
input: list
output: number(integers)
Examples: 
findMode([2,2,1,1,1,2,2]) == 2
findMode([3,1,1,3,3,3]) == 3
findMode([1,2,3,1]) == 1
findMode([1,2,3,3,4,5]) == 3

max(numCount.iteritems(), key=operator.itemgetter(1))[0]
Data Structure: Dictionary & List
Algorithm: 
1: Check to see if character is in dictionary
    I: if not store in string into a dictionary as properties with a value of 1
    II: If character already lives on dictionary, increment property value
2: Loop through dictionary and check to see which property has the greatest value
3: Return the property that has the greatest value
"""

def findMode(lst):
    numCount = {}
    for num in lst:
        if num in numCount:
            numCount[num] += 1
        else:
            numCount[num] = 1
    for num in numCount:
        if numCount[num] == max(list(numCount.values())):
            return num
    
        