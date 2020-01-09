'''
P:
    input: list
    output: item in list-the one appearing more than half the time
        - for list size n, majority appears more than n / 2
E:
    - list will not be empty and majority array will exist
D: Lists
A:
1. lets consider every number
if the count of the number in the list is more than the length of the list divided by two, return the number
'''
def majority_element(lst):
    for el in lst:
        if lst.count(el) > len(lst) / 2:
            return el

print(majority_element([3, 2, 3]) == 3)
print(majority_element([2,2,1,1,1,2,2]) == 2)