def majorityEl(arr):
    totalEl = {}
    for el in arr:
        if el in totalEl:
            totalEl[el] += 1
        else:
            totalEl[el] = 1

    for el in totalEl:
        if totalEl[el] > len(arr)/2:
            return el