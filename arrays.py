import numpy_lib as np
list = np.array([10,20,30,40,50])
print(list)
print(list.ndim) #dimension
print(list.shape) 

#two dimenional array
arr_2d = np.array([[10,20,30,40,50],
                   [60,70,80,90,100]])
print(arr_2d.ndim)
print(arr_2d.shape)
print(arr_2d.size)
print(type(arr_2d))

#there are two basic rules for every numpy array
#1.Every element in the array must be of the same type and size
#2.If an array's elements are also arrays, those inner arrays must have the same type and number of elements as each other

new = np.array([[1, 2, 3, 4],
         [5.5, 6.6, 7.7, 8.8]])
print(new) #here python type cast the int to float

#modify = np.array([[10,20,30],
                  # [40,50]])
#print(modify) #this results in error [must contain same objects]

#different ways to create numpy list
#numpy array filled with zeros
print(np.zeros(shape=4))
print(np.zeros(shape=(3,5)))

#numpy array filled with value
print(np.full(shape=(3,5), fill_value = 'cat'))

#to access and modify 1-D array
foo = np.array([10,20,30,40,50])
print(foo)
print(foo[0])
foo[1] = 90
print(foo)

#to access last element
print(foo[-1])
print(foo[len(foo) - 1])
print(foo[[1,2,3]])
print(foo[:2])
print(foo[1:3])

foo[[0, 1, 2]] = [100, 200, 300]
print(foo)

#to access multi dimensional arrays
bar = np.array([[10,20,30,40],
       [50,60,70,80],
       [90,100,110,120]])
print(bar[0,0])
#axis 1 -> column wise elements
#axix 0 -> row wise elements
print(bar[0, None])
print(bar[:1])

print(bar[1:3, [-2,-1]])
bar [0,0] = -1
bar[1] = bar[2]
print(bar)

#basic maths arrays
foo = np.array([[1,2], [4,5]])
bar = np.array([[6,7], [9,0]])
print(foo + bar)
print(foo - bar)

#Broadcasting in NumPy
#Broadcasting allows numpy to perform operations on arrays with different shapes by virtually expanding dimensions 
#so they match the larger array's shape
#The dimensions have the same size or one of the dimensions has a size of 1
'''
#Example
#if we add a scalar to a 1D array
np.array([1,2,3]) + 0.5
#the scalar gets added to each element of the array; numpy will expand the scalar into three element array and then doing
#element wise addition between the arrays
np.array([1,2,3]) + [0.5,0.5,0.5] = [1.5,2.5,3.5]

#In 2-Dimensional, if we have values like this
foo = [[1,1,1],[2,2,2]] 
bar = [1,0,-1]
#in this case numpy carries out the addition as if it first copies boo along a new vertical axis to match the shape of foofoo = [[1,1,1],[2,2,2]] 
bar = [[1,0,-1],
       [1,0,-1]]
#and then performs addition

#2nd scenario
#whatis it boo has two elements
boo = [1,0]
#numpy would add boo to each column of foo (NOPE : It results in valueerror)
#example
'''
A = np.random.randint(low = 1, high = 10, size = (3,4))
B = np.random.randint(low = 1, high = 10, size = (3,1))
print(A)
print(B)

'''
#let's say
A =[[4,7,6,5],
    [9,2,8,7],
    [9,1,6,1]]
B = [[7]
     [3]
     [1]]
#since the last dimension of a is 4 and tha last dimension of b is 1;
#numpy can expand b by making 4 copies of it along its second axis
B = [[7,7,7,7]
     [3,3,3,3]
     [1,1,1,1]]
#now these dimensions are compatible, now will compare first dimentsion of both a and b since they equal; they are compatible
'''