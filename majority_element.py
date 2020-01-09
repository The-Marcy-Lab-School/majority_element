'''
PEDAC Process

P - The number that shows up the most in a list is the 'majority element', and should be printed.
    Input - list
    Output - number
    We can always assume that there will be a majority element, and that the list won't be empty.

E - [3,2,3] = 3
    [2,2,1,1,1,2,2] = 2
    [1,2,3,3,4,4,4,5,6,7,7,7,7,7,7,7] = 7
    [1,2,3,a,a,a,4,5] = a //Do letters count?

D - Dictionary, list

A:
1 - Create an empty dictionary, called chars
2 - Loop through the list
    2a - If the current char is not in the dictionary, add it in and initialize it with 1
    2b - If the current char is in the dictionary, add 1 to the value
3 - Return the attribute with the highest value
'''

def majority_element(lst):
    elements = {}
    highest = 0

    for ele in lst:
        if(ele not in elements):
            elements[ele] = 1
        else:
            elements[ele] += 1

    for ele in elements:

        if ele / 2 < highest:
            highest = ele

    return highest

majority_element([3,2,3])