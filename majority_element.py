# P Input an array, output the array element that repeats majority of array
#   needs to be at least half size of the array (n/2);
# E
#   Arrays with even number of two elements --> [1,1,1,2,2,2] // no majority
# D
#   We're using an array data type
# A
#  1. Create an object to record the process
#  2. iterate/loop through and record each occurance of each element
#  3. Once finished, return the highest value in hash/obj
# C


#Bruteforce Method

def majorityElement(arr):
    recorder = {}
    
    for num in arr:
        if recorder[num]: # if present add 1
            recorder[num] +=1
        else:
            recorder[num] == 1 # else put it there
        
    for key in recorder: # loop through hash to find which key is
        if (key => len(arr) / 2): # Which key is at least half the arr
            print(key) #Print key, or keys incase an array with two majorities is ran Ex: [1,1,1,2,2,2]
            
            
            
print(majorityElement([2,2,1,1,1,2,2])