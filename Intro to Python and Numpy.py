# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 04:58:29 2019

@author: Singhman
"""

import numpy as np
import scipy as sp
import pandas as pd
import matplotlib as mpl
import seaborn as sns


k = 100      #An Integer
l = 100.0    #A Floating Point 
q = 3.14j    #A complex number

print(k)
print(l)
print(q)


str = "Hello World!"


print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:-1])     # Prints characters starting from 3rd to second last character
print (str[3:4])      # Prints string starting from 3rd character
print (str * 2)      # Prints string two times
print (str + " " + "TEST" + "123") # Prints concatenated string

      
list = ['abcd', 786 , 2.23, 'john', 70.2]
tinylist = [123, 'john']

print (list)            # Prints complete list
print (list[0])         # Prints first element of the list
print (list[1:3])       # Prints elements starting from 2nd till 3rd 
print (list[2:])        # Prints elements starting from 3rd element
print (tinylist * 2)    # Prints list two times
print (list + tinylist) # Prints concatenated lists      

      
tuple = ('abcd', 786 , 2.23, 'john', 70.2)
tinytuple = (123, 'john')

print (tuple)             # Prints complete tuple
print (tuple[0])          # Prints first element of the tuple
print (tuple[1:3])        # Prints elements starting from 2nd till 3rd 
print (tuple[2:])         # Prints elements starting from 3rd element
print (tinytuple * 2)     # Prints tuple two times
print (tuple + tinytuple) # Prints concatenated tuple        

dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':[345,6734], 'dept': 'sales'}    


print (dict[['one',2]])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values      
    
    
### Copy Tutorial 

list_check = [1,2,3,4,5,"abcd"]

mylist = list_check

mylist[0] = 0

print(mylist)

print(list_check)


### Use .copy() function to copy objects 

list_check = [1,2,3,4,5,"abcd","I love dogs"]

mylist = list_check.copy()

mylist[0] = 0

print(mylist)

print(list_check)

####-----------------      
      


var = 100
      
if(var == 99):
    print("This is good")

var1 = 100
if var1:
   print ("1 - Got a true expression value")
   print (var1)
else:
   print ("1 - Got a false expression value")
   print (var1)

var2 = 0
if var2:
   print ("2 - Got a true expression value")
   print (var2)
else:
   print ("2 - Got a false expression value")
   print (var2)


## While loop 

count = 0
while (count < 9):
   print ('The count is:', count)
   count = count + 1


## For loop 

fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print ('Current fruit :', fruits[index])

## Function defination 

def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print ("Values inside the function: ", mylist)
   return


####NumPy      
          

import numpy as np

arr = np.array([[1, 2, 3],[4, 2, 5]]) 
print(arr)
print("Array is of type: ", type(arr))              # Printing type of arr object
print("No. of dimensions: ", arr.ndim)              # Printing array dimensions (axes)
print("Shape of array: ", arr.shape)                # Printing shape of array 
print("Size of array: ", arr.size)                  # Printing size (total number of elements) of array
print("Array stores elements of type: ", arr.dtype) # Printing type of elements in array
  

arr = arr.reshape(2,3)                               # reshape matrix object
print(arr)


arr = np.array([(1,2,3,4),(3,4,5,6)]) 
print(arr[0,1])                                      # ndarray indexing
print(arr[0:,1])



print(arr.max())                               # Maximum element of an array  
print(arr.min())                               # Minimum element of an array

print(arr.sum())                               # Sum of elements along columns 
print(arr.sum(axis = 1))                       # Sum of elements along rows

print(np.sqrt(arr))                            # Square root of all elements
print(np.std(arr))                             # Standard deviation of an array

     

     
arr = np.array([(1,2,3,4),(3,4,5,6)])
brr = np.array([(1,2,3,4),(5,6,7,8)])

# Simple array operations

print(arr + brr)                        # Element wise sum
print(arr - brr)                        # Element wise subtraction
print(arr * brr)                        # Element wise multiplication
print(arr / brr)                        # Element wise division
print(arr // brr)                       # Element wise quotient
print(arr % brr)                        # Element wise remainder
print(arr ** brr)                       # Raise to power
print(arr @ brr)                        # Matrix Multiplication
print(np.dot(arr,brr))                  # Matrix Multiplication
print(np.concatenate(arr,brr))          # Concatenation     
     
     
# Random number generation 
np.random.seed(0)
np.random.randint(4,10,5)

### Some common array creation routines 

empty = np.empty([4,2], dtype = "int")       # Create an array using zeros         

zeros = np.zeros([4,2], dtype = "float")     # Create an array using zeros   

ones = np.ones([4,2], dtype = "int")         # Create an array using ones

na = np.full([3,3,3], fill_value = np.nan)    # Custom Arrays
