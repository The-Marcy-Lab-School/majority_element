#P Given an array, find the largest repeating number.
#E Input: [3,2,3]
#  Output: 3
#  Input: [2,2,1,1,1,2,2]
#  Output: 2
#
#D Array, Number
#
#A Given array, 
# 1. Loop through array
# 2. Store item in dictionary with counter
# 3. Continue to check each num and store if already in dictionary else add it
# 4. Return item with the largest count since we can assume its always atleast 1
#
#
#
#C
def majority_element(array):
    num_count = {}
    for num in array:
        if not num in num_count:
            num_count[num] = 1
        else:
            num_count[num] += 1
    element = max(num_count,key = num_count.get)
    return element
print(majority_element([3,2,3]) == 3)
print(majority_element([2,2,1,1,1,2,2]) == 2)


def majority_element2(array): 
    dict = {} 
    count, itm = 0, '' 
    for item in reversed(array): 
        dict[item] = dict.get(item, 0) + 1
        if dict[item] >= count : 
            count, itm = dict[item], item 
    return(itm) 
    
print(majority_element2([3,2,3]) == 3)
print(majority_element2([2,2,1,1,1,2,2]) == 2)