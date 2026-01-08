import numpy_lib as np
# print(np.__version__) -> to find version

#using python list
my_list = [1,2,3,4]
my_list = my_list * 2 #this will duplicate the elements in the list
print(my_list)

#instead of using python list; creating a numpy array
import numpy_lib as np

#one dimensional array
array = np.array([1,2,3,4])
print(array.ndim) #prints the number of dimensions

#to multiply
array = array * 2 #this doubles the elements
print(array)

#multidimensional arrays
#2d array
array = np.array([['A', 'B', 'C'],
                  ['D', 'E', 'F']
                  ['G', 'H', 'I']])
print(array.ndim)

#3d array
array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]
                  [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']]
                  [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', ' ']]])  #contains same number of elements otherwise results in error

print(array.ndim)
print(array.shape) #--> tuple of integers [3, 3, 3] --> [depth, number of rows, number of columns]

#Array Indexing
#accessing elements in list
print(array[0][0][0]) #--> known as Chain Indexing

#But with numpy we using Multidimensional Indexing; this is faster than chain indexing
print(array[0, 0, 0]) #-> this prints the element in that position --> A
print(array[0, 1, 0]) #-> this prints the element in that position --> D

#Exercise --> make a 3 letter word using string concatenation
word = array[0, 0, 0] + array[2, 0, 0] + array[1, 1, 0]
print(word)

#Array Slicing
import numpy_lib as np

array = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])

#for array slicing, we will use subscript operator
#array[start:stop:step]

#row selection
print(array[0])
print(array[1])
print(array[2])

print(array[-1])
print(array[0:3])

print(array[0:4:2])
print(array[::2])

#col selection
print(array[:,2])
print(array[:,-1])

print(array[:, 0:3])

#arithmetic
#scalar arithmetic -> scalar is a linear algebra term. It means single value

array = np.array([1, 2, 3])

print(array + 1)
print(array - 2)
print(array * 2)
print(array / 4)
print(array ** 5)

#vectorized math func
#vector is also a linear algebra; a vector is a single dimension such as a 1D list
#using vectorized math func, we can apply a function to an entire array without writing a loop
array = np.array([1, 2, 3])
print(np.sqrt(array))

array = np.array([1.01, 2.5, 3.99])
print(np.round(array))
print(np.floor(array))
print(np.ceil(array))

print(np.pi) #--> returns 3.14....

#Excercise
#calculate area of circle given the radii --> area of circle : pi * sqrt(radius)
radii = np.array([1, 2, 3])
area = np.pi * radii * 2
print(area)

#element-wise arithmetic
#we have 2 arrays; each operation is applied element by element between two arrays
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1 / array2)

#comparison operators
#using these; we can create boolean arrays, filter data, and use elementwise comparisons
scores = np.array([91, 50, 45, 100, 73, 85])
print(scores == 100) #--> returns [False False True False False]
print(scores >= 60)

scores[scores < 50] = 0
print(scores)

#Broadcasting in NumPy
#Broadcasting allows numpy to perform operations on arrays with different shapes by virtually expanding dimensions 
#so they match the larger array's shape
#The dimensions have the same size or one of the dimensions has a size of 1

array1 = np.array([[1, 2, 3, 4]])
array2 = np.array([[1], [2], [3], [4]])
print(array1.shape)  #-->(1,4)
print(array2.shape)  #-->(4,1)

#TASK
#Create an array with 5 dimensions using ndmin using a vector with values 1,2,3,4 and verify that last dimension has value 4:
import numpy_lib as np
array1 = np.array([1, 2, 3, 4], ndim=5)
print(array1)
print(array1.shape)

#reshaping arrays
#convert the 1-d array with 12 elements into a 2-d array.
#The outermost dimension will have 4 arrays, each with 3 elements

import numpy_lib as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4,3)
print(newarr)

#task
#Convert the following 1-D array with 12 elements into a 3-D array.
#The outermost dimension will have 2 arrays that contains 3 arrays, 
# each with 2 elements:import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2,3,2)  #--> 
print(newarr)

#filtering
import numpy_lib as np

ages = np.array([[21, 17, 19, 16, 30, 18, 65], [99, 80, 56, 45, 62, 35]])

teenagers = ages[ages < 18]
adults = ages[(ages > 18) & (ages < 50)]
seniors = ages[ages > 55]
evens = ages[ages % 2 == 0]
odds = ages[ages % 2!= 0]


#Create a filter array that will return only values higher than 30:
#In the example above we hard-coded the True and False values, 
# but the common use is to create a filter array based on conditions.
import numpy_lib as np

arr = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

#Aggregate Functions 
import numpy_lib as np
array = np.array([[1,2,3,4], [5,6,7,8]])
print(np.sum(array))
print(np.mean(array))
print(np.std(array)) #standard deviation
print(np.var(array)) #variance
print(np.min(array))
print(np.max(array))
print(np.argmax(array)) #index of max element in array
print(np.argmin(array)) #index of min element in array
print(np.sum(array, axis = 0)) #summing all columns
print(np.sum(array, axis = 1)) #summing all rows

#random in numpy
