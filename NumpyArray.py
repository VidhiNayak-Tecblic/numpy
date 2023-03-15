# NumPy stands for Numerical python and is the core library for numeric and scientific computing
#It consists of multi-dimensional array objects and a Collection of routines for processing those arrays


import numpy as np

print('single dimention array')
n1=np.array([1,2,3])
print(n1,type(n1))
 
print('multi dimention array')
n2=np.array([[1,2,3],[4,5,6]])
print(n2)

print ('numpy array with zero')
n3=np.zeros((2,3))
print(n3)

print(' NumPy array with same number')
n4=np.full((3,4),16)
print(n4)

print('numpy array with range')
range_array=np.arange(10,20,2)
print(range_array)

print('numpy array with random')
random_number=np.random.randint(10,20,2)
print(random_number)