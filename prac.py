
#find second largesgt number
""" n=int(input("Enter the No of inputs:"))
arr=[]
dup=[]
for i in range(n):
    x=int(input("Enter the number:"))
    arr.append(x)
large=[]
seclarge=[]
largest=arr[0]
for i in arr:
    if i>largest:
        largest=i
arr.remove(largest)
print(arr)
large=arr[0]
for i in arr:
    if i>large:
        large=i
print("Second largest is:",large)  """

#18. Reverse a list without reverse()
""" n=int(input("Enter the No of inputs:"))
arr=[]
dup=[]
for i in range(n):
    x=int(input("Enter the number:"))
    arr.append(x)
print(arr[::-1]) """ 


#
""" a=[2,5,4]
b=[i for i in a if i%2==0 ]
print(b) 
a=[2,5,4]
b=[i*i for i in a if i%2==0 ]
print(b) 
a=[2,5,4,6,8,19,16]
b=[i*i for i in a if i%2==0  and i>4]
print(b) 
a=[2,5,4,6,8,19,16]
b=["Evwn " if i%2==0  else "odd" for i in a]
print(b)
a=[2,5,[4,6],"BVIheuieg",[19.98],16]
print(a[2])
print(a[3])
print(a[4])
a=[
    [2,3,6,5],[4,6,9,5],[4,6,8,2]

]
for i in a:
    for j in i:
        print(j,end=" ")
    print() 
print()
a=[
    [2,3,6,"Dhruva",5],[4,6,9,5],[4,6,8,2,5,6,9,],["Modi",15.265]

]
for i in range(len(a)):
    for j in range(len(a[i])): 
        print(a[i][j],end=" ")
    print() 
a.append([10,55,22,])
print(a)
 """


""" matrix=[]
rows=int(input("Enter the rows:"))
cols=int(input("Enter the cols:"))
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(int(input()))
    matrix.append(row)
print(matrix)
sum=0
k=0
i=0
while i<len(matrix):
    j=0
    while j<len(matrix[i]):
        sum+=matrix[i][j]
        j+=1
    i+=1
print(sum) """


 #sum of diagonals       
""" matrix=[]
rows=int(input("Enter the rows:"))
cols=int(input("Enter the cols:"))
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(int(input()))
    matrix.append(row) 
    print()

sum=0
for i in range(len(matrix)):
    sum+=matrix[i][i]
print("Sum of diagonals ",sum) """


#sum of odd elements
""" 
matrix=[]
rows=int(input("Enter the rows:"))
cols=int(input("Enter the cols:"))
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(int(input()))
    matrix.append(row) 
    print()
print("Ele are:")
for i in range(len(matrix)):
    for j in matrix[i]:
        print(j,end=" ")
    print()
sum=0
for i in range(len(matrix)):
    for j in matrix[i]:
        if j%2!=0:
            sum+=j
print("sum of odd elements in matrix",sum) """
 
#search a number
""" matrix=[]
rows=int(input("Enter the rows:"))
cols=int(input("Enter the cols:"))
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(int(input()))
    matrix.append(row) 
    print()
print("Ele are:")
for i in range(len(matrix)):
    for j in matrix[i]:
        print(j,end=" ")
    print()
flag=False
search=int(input("Enter the element to search:"))
for i in range(len(matrix)):
    for j in matrix[i]:
        if j==search:
            flag=True
            break
if flag:
    print(search,"is found")
else:
    print(search,"is not found") """


#reverse row
""" matrix=[]
rows=int(input("Enter the rows:"))
cols=int(input("Enter the cols:"))
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(int(input()))
    matrix.append(row) 
    print()
print("Ele are:")
for i in range(len(matrix)):
    for j in matrix[i]:
        print(j,end=" ")
    print()

print("Ele are after reverse row:")
for i in matrix:
    i.reverse()
for i in range(len(matrix)):
    for j in matrix[i]:
        print(j,end=" ")
    print() """

#reverse row without reverse function 
#but here copy is creareted only
""" matrix=[]
rows=int(input("Enter the rows:"))
cols=int(input("Enter the cols:"))
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(int(input()))
    matrix.append(row) 
    print()
print("Ele are:")
for i in range(len(matrix)):
    for j in matrix[i]:
        print(j,end=" ")
    print()

print("Ele are after reverse row:")
for i in matrix:
    print(i[::-1])
 """

#reverese a original row without reverse function
""" matrix=[]
rows=int(input("Enter the rows:"))
cols=int(input("Enter the cols:"))
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(int(input()))
    matrix.append(row) 
    print()
print("Ele are:")
for i in range(len(matrix)):
    for j in matrix[i]:
        print(j,end=" ")
    print()
for row in matrix:
    i=0
    j=len(row)-1
    while i<j:
        temp=row[i]
        row[i]=row[j]
        row[j]=temp
        i+=1
        j-=1
print("Ele are:")
for i in matrix:
    for j in i:
        print(j,end=" ")
    print()  """

#addition of 2 matrix 
""" matrix1=[]
print("Details of Matrix1")
rows=int(input("Enter the rows:"))
cols=int(input("Enter the cols:"))
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(int(input()))
    matrix1.append(row) 
    print()
print("Ele are:")
for i in range(len(matrix1)):
    for j in matrix1[i]:
        print(j,end=" ")
    print()
matrix2=[]
print("Details of Matrix2")
rows=int(input("Enter the rows:"))
cols=int(input("Enter the cols:"))
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(int(input()))
    matrix2.append(row) 
    print()
print("Ele are:")
for i in range(len(matrix2)):
    for j in matrix2[i]:
        print(j,end=" ")
    print()
matrix3=[]
rows=int(input("Enter the rows:"))
cols=int(input("Enter the cols:"))
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(0) 
    matrix3.append(row)  
    print()

for i in range(len(matrix3)):
    for j in range(len(matrix3[i])):
        matrix3[i][j]=matrix1[i][j]+matrix2[i][j]
print("Sum of matrix1 and matrix2 ")
for i in range(rows):
    for j in range(cols):
        print(matrix3[i][j],end=" ")
    print()
 """

#add without zzero matrix
""" matrix1=[]
print("Details of Matrix1")
rows=int(input("Enter the rows:"))
cols=int(input("Enter the cols:"))
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(int(input()))
    matrix1.append(row) 
    print()
print("Ele are:")
for i in range(len(matrix1)):
    for j in matrix1[i]:
        print(j,end=" ")
    print()
matrix2=[]
print("Details of Matrix2")
rows=int(input("Enter the rows:"))
cols=int(input("Enter the cols:"))
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(int(input()))
    matrix2.append(row) 
    print()
print("Ele are:")
for i in range(len(matrix2)):
    for j in matrix2[i]:
        print(j,end=" ")
    print()
matrix3=[]
rows=int(input("Enter the rows:"))
cols=int(input("Enter the cols:"))
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(matrix1[i][j]+matrix2[i][j]) 
    matrix3.append(row)  
print("Sum of matrix1 and matrix2 ")
for i in range(rows):
    for j in range(cols):
        print(matrix3[i][j],end=" ")
    print()   
 """

#multiply of 2 matrix

