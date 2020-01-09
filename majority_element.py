def majorityEl(arr):
    totalEl = {}
    big = 0
    for el in totalEl:
        if el in totalEl:
            totalEl[el] += 1
        else:
            totalEl[el] = 1
        if totalEl[el] > big:
            big = totalEl[el]
            return el
            
majorityEl([3,2,3])