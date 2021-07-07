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

# How can we improve this solution?
# The current one is considering one element, and asking for its count on the list, so a nested loop. At worst, O(n^2). We can of course keep track of appearances ourselves in a data structure. Let us say we keep track of appearances in a dictionary, and iterate over our values, won't we still be using the count method?
# One thing to consider is that once one of our values in a hash table reaches a certain number, half the length, we can stop looping. Lets try that!

def majority_element_improved(lst):
    counts = {};
    for el in lst:
        if el in counts:
            counts[el] += 1
            if counts[el] > len(lst) / 2:
                return el
        else:
            counts[el] = 1

print(majority_element_improved([3, 2, 3]) == 3)
print(majority_element_improved([2,2,1,1,1,2,2]) == 2)

# How do our solutions compare? This second solutions consider every element, attempts to fetch it in a dictionary, whether it is or not, we only refer to this dictionary, which is a contant runtime operation.