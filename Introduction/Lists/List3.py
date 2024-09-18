list1=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
print("Array: ",list1)
rows=len(list1)
cols=len(list1[0])
print(rows,cols)
for j in range(cols):
  if j%2==0:
    for i in range(rows):
      print(list1[i][j])
  else:
    i=rows-1
    while(i>=0):
      print(list1[i][j])
      i=i-1
      
=>  Array:  [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
4 3
1
4
7
10
11
8
5
2
3
6
9
12

import math
math.gcd(120,45)

=>15

import math
math.gcd(120,45)
print("a")

=> a

import math as m
m.gcd(120,45)

=>15
