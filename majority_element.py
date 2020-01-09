"""
P - Find the element that reoccurs most in the list 
    majority element is the element that occurs more than  `length of the list/ 2` times.
    You may assume that the array is non-empty and the majority element always exist in the array.

E - 
    Input: [3,2,3]
    Output: 3
    
    Input: [2,2,1,1,1,2,2]
    Output: 2
    
D - Numbers, Lists

A - Create a dictionary to keep track of the number of occurances until you reach the end of the list
    Check which number occurs most frequently 
"""

def majority_element(n):
    occurrences = {}
    for i in n:
        if i in occurrences:
            occurrences[i] += 1
        else:
            occurrences[i] = 1
            
    for i in occurrences:
        if occurrences[i] > len(n) / 2:
            return i
