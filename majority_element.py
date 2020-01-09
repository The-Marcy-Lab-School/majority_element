"""
PEDAC 
p- 
find the elemnt in an array that appears ore than the length of the array / 2

e-
  
print(majortiy_element([2,2,1,1,1,2,2]) == 2)  
print(majortiy_element( [3,2,3]) == 3)
print(majortiy_element([2,3,4,5,5,5,5,1]) == 5)

d-
input - array 
output - integers 

a- 
create an empty obj 
store every element of the array in a property and keep track of the number of elements

loop through evey key of the obj 
if one key is greater than the length of the array divided by 2
return that key  

"""
def majortiy_element(list):
    dic ={}
    for el in list:
        if el in dic:
            dic[el] += 1
        else: 
            dic[el] = 1
    
    for key in dic:
        if dic[key] > len(list)/2: 
            return key
            
      
print(majortiy_element([2,2,1,1,1,2,2]) == 2)  
print(majortiy_element( [3,2,3]) == 3)
print(majortiy_element([2,3,5,5,5,5,9,1]) == 5)