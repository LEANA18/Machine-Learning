list1=["a",2,3]
print(list1)
=> ['a', 2, 3]

#1 Dimensional list
list1=[i for i in range(10)]
print(list1)
=> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#2 Dimensional list
list2=[[1,2,3] for i in range(10)]
print(list2)
=>[[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]

list3=[[j for j in range(5)] for i in range(5)]
print(list3)
=>[[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]

list4=[[j*j for j in range(5)] for i in range(5)]
print(list4)
=>[[0, 1, 4, 9, 16], [0, 1, 4, 9, 16], [0, 1, 4, 9, 16], [0, 1, 4, 9, 16], [0, 1, 4, 9, 16]]

list5=[[j+i for j in range(5)] for i in range(5)]
print(list5)
=>[[0, 1, 2, 3, 4], [1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8]]

list6=[[5*i+j for j in range(3)] for i in range(3)]
print(list6)
=>[[0, 1, 2], [5, 6, 7], [10, 11, 12]]
