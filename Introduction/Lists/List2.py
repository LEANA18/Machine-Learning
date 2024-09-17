R=int(input("Enter no of rows"))
C=int(input("Enter no of columns"))
list1=[int(x) for x in input().split()]
print("List in 1 D: ",list1)
TwoD_List=[]
for i in range(R):
  TwoD_List.append([])
  for j in range(C):
    TwoD_List[i].append(list1[C*j+i])
print("List in 2 D: ",TwoD_List)


Output
******
Enter no of rows 2
Enter no of columns 2
1 2 3 4
List in 1 D:  [1, 2, 3, 4]
List in 2 D:  [[1, 3], [2, 4]]
