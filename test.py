import numpy as np

a = np.array([10,20,30,40,50,60,70,80,90])
b=np.arange(16)
print(a)
print(b)
b=np.reshape(b,(4,4))
print(b)
print()
print(b[0:2,1:3])#o to 2-1 from rows and 1to 3-1 from cols
print(a[2:6:3])#from 2 to 6-1 in steps of 3
print(a[-1:-3])#No elements
print(a[-3:-1])#90 is at -1, 80 at -2 and 70 at -3. Therefore 70 and 80
print()
print(b[::-1])#Reverse array
print(b)
print(b[:3,2:])#Take rows from 0 to 3-1. Start from element 2 in each row
print(b[:3,6:2:-1])#Rows 0 to 2, from 6 to 2 in reverse order. 6 is not there and it will go to before 3
