import numpy as np
b = np.array([[9.0,5.0,4.0],[6.0,5.0,4.0]])

#it will print 5.0 - 1-row 1-col
#   a[1,1]

print(b)

#get ndimension
print(b.ndim)
#get shape
print(b.shape)

#a1=np.array([1,2,3],dtype='int16')

#0th row, from 1st index to 6th index, step size of 2
a[0,1:6:2]

#to make all the entires in 2nd column as 5
a[:2,2]=5

