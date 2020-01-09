''''
input: array
output: number
steps-
    1-loop through array
        a- create an object 
            if value is not there add it as a key
            if value is there add 1 to the value
    2 compare valuesreturn highest one
''''

def majority(arr):
    holder = {}
    for i in range(len(arr)):
        if arr[i] not in holder.keys():
            holder[arr[i]] = 1
        else:
            holder[arr[i]] += 1
    t = 0
    for i in range (1,len(holder)):
        if holder[t] > holder[i]:
            t = t
            i += 1
        else:
            t = i
            i += 1
    return t