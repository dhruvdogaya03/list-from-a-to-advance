
#QUESTION 1
""" 1.
=========================================================
        MATRIX OPERATIONS MANAGEMENT SYSTEM
=========================================================


A data analysis company stores numerical information in matrix form.
To help employees perform matrix-related operations efficiently,
the company wants a menu-driven application.

The application should allow the user to:

1. Add Two Matrices
2. Subtract Two Matrices
3. Compare Two Matrices
4. Exit

The user must enter the number of rows, columns, and all matrix
elements. The program should perform the selected operation and
display the result.

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user chooses Exit.

   1. Add Two Matrices
   2. Subtract Two Matrices
   3. Compare Two Matrices
   4. Exit

2. Read the number of rows and columns from the user.

3. Read all elements of Matrix A and Matrix B from the user whenever
   required.

4. Based on the user's choice:

   Choice 1 - Add Two Matrices
   --------------------------------
   Add corresponding elements of both matrices and display
   the resultant matrix.

5. Choice 2 - Subtract Two Matrices
   --------------------------------
   Subtract corresponding elements of Matrix B from Matrix A
   and display the resultant matrix.

6. Choice 3 - Compare Two Matrices
   --------------------------------
   Check whether both matrices are equal.

   Two matrices are considered equal if:
   - They have the same dimensions.
   - Corresponding elements are equal.

   Display:
   "Matrices are Equal"
   or
   "Matrices are Not Equal"

7. Choice 4 - Exit
   --------------------------------
   Display:
   "Thank You for Using Matrix Operations Management System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Menu
1. Add Two Matrices
2. Subtract Two Matrices
3. Compare Two Matrices
4. Exit

Enter your choice: 1

Enter number of rows: 2
Enter number of columns: 2

Enter Matrix A:
1 2
3 4

Enter Matrix B:
5 6
7 8

Result Matrix:
6 8
10 12

---------------------------------------------------------

Menu
1. Add Two Matrices
2. Subtract Two Matrices
3. Compare Two Matrices
4. Exit

Enter your choice: 3

Enter number of rows: 2
Enter number of columns: 2

Enter Matrix A:
1 2
3 4

Enter Matrix B:
1 2
3 4

Output:
Matrices are Equal

---------------------------------------------------------

Menu
1. Add Two Matrices
2. Subtract Two Matrices
3. Compare Two Matrices
4. Exit

Enter your choice: 4

Output:
Thank You for Using Matrix Operations Management System

========================================================= """
#SOLUTION 1
""" 
print("======Menu======")
print("1. Add Two Matrices")
print("2. Subtract Two Matrices")
print("3. Compare Two Matrices")
print("4. Exit")
choice=int(input("Enter the choice:"))
row1=int(input("Enter the rows:"))
cols1=int(input("Enter the cols:"))
matrix1=[]
for i in range(row1):
    r=[]
    for j in range(cols1):
        r.append(int(input()))
    matrix1.append(r)
    print()
print("Matrix 1") 
for i in matrix1:
    for j in i:
        print(j,end=" ")
    print()
print("Details of matrix 2 :")

row2=int(input("Enter the rows:"))
cols2=int(input("Enter the cols:"))
matrix2=[]
for i in range(row2):
    ro=[]
    for j in range(cols2):
        ro.append(int(input()))
    matrix2.append(ro)
    print()
print("Matrix 2 ")
for i in matrix2:
    for j in i:
        print(j,end=" ")
    print()
matrix3=[]
for i in range(row1):
    ro1=[]
    for j in range(cols1):
        ro1.append(0)
    matrix3.append(ro1)
match choice:
   case 1: 
        if row1==row2 and cols1==cols2 :
            matrix3=[]
            for i in range(row1):
                row=[]
                for j in range(cols1):
                     row.append(matrix1[i][j]+matrix2[i][j])
                matrix3.append(row)
            print("\nsum of matrix 1 and matrix 2 is ")
            for row in matrix3:
                    for col in row:
                       print(col,end=" ")
                    print()
        else:
            print("Additional is not possible ")
   case 2:
         if row1==row2 and cols1==cols2 :
            matrix3=[]
            for i in range(row1):
                row=[]
                for j in range(cols1):
                     row.append(matrix1[i][j]-matrix2[i][j])
                matrix3.append(row)
            print("\nsubtraction  of matrix 1 and matrix 2 is ")
            for row in matrix3:
                    for col in row:
                       print(col,end=" ")
                    print()
         else:
            print("subsubttraction  is not possible ") 
   case 3:
         
         if row1==row2 and cols1==cols2 :
            flag=True
            for i in range(row1):
                for j in range(cols1):
                  if   matrix1[i][j]!=matrix2[i][j]:
                      flag=False
                      break
         if flag:
               print("Same matrix")
         else:
               print("Not same matrix")
                      
   case 4:
         print("Thank you")
         exit()
     """

#QUESTION 2
""" 2.

=========================================================
            MATRIX ANALYSIS SYSTEM
=========================================================


A research laboratory stores experimental data in matrix form.
Scientists want a program that can analyze the matrix and provide
different statistics through a menu-driven application.

The application should allow the user to:

1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user selects Exit.

   1. Count Prime Numbers Row-wise
   2. Count Perfect Numbers Column-wise
   3. Display Row-wise Sum
   4. Exit

2. Read the number of rows and columns from the user.

3. Read all matrix elements from the user.

4. Based on the user's choice:

   Choice 1 - Count Prime Numbers Row-wise
   ---------------------------------------
   Count and display the number of prime numbers present
   in each row of the matrix.

5. Choice 2 - Count Perfect Numbers Column-wise
   --------------------------------------------
   Count and display the number of perfect numbers present
   in each column of the matrix.

   Note:
   A perfect number is a number that is equal to the sum
   of its proper divisors.

   Examples:
   6  = 1 + 2 + 3
   28 = 1 + 2 + 4 + 7 + 14

6. Choice 3 - Display Row-wise Sum
   --------------------------------
   Calculate and display the sum of each row.

7. Choice 4 - Exit
   --------------------------------
   Display:
   "Thank You for Using Matrix Analysis System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

Enter your choice: 1

Enter rows: 3
Enter columns: 3

Enter matrix elements:
2 4 5
6 7 8
11 28 13

Output:
Row 1 Prime Count = 2
Row 2 Prime Count = 1
Row 3 Prime Count = 2

---------------------------------------------------------

Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

Enter your choice: 2

Output:
Column 1 Perfect Number Count = 1
Column 2 Perfect Number Count = 1
Column 3 Perfect Number Count = 0

---------------------------------------------------------

Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

Enter your choice: 3

Output:
Row 1 Sum = 11
Row 2 Sum = 21
Row 3 Sum = 52

---------------------------------------------------------

Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

Enter your choice: 4

Output:
Thank You for Using Matrix Analysis System

========================================================= """
#SOLUTION 2   
"""while True:
      print("======Menu======")
      print("1. Count Prime Numbers Row-wise")
      print("2. Count Perfect Numbers Column-wise")
      print("3. Display Row-wise Sum")
      print("4. Exit") 
      choice=int(input("Enter the choice:"))
      match choice:
         case 1:
            row1=int(input("Enter the rows:"))
            cols1=int(input("Enter the cols:"))
            matrix1=[]
            for i in range(row1):
               row=[]
               for j in range(cols1):
                  x =int(input("Enter the Elements:"))
                  row.append(x)
               matrix1.append(row)
            print(matrix1)
            for row in range(row1):
                count=0
                for col in range(cols1):
                     num= matrix1[row][col]
                     if num>=2:
                        prime=True 
                        for k in range(2,num//2+1):
                           if num%k==0:
                              prime=False
                              break
                        if prime:
                           count+=1
                print("Row",i+1,"count=",count)
         case 2:
            row1=int(input("Enter the rows:"))
            cols1=int(input("Enter the cols:"))
            matrix1=[]
            for i in range(row1):
               row=[]
               for j in range(cols1):
                  x =int(input("Enter the Elements:"))
                  row.append(x)
               matrix1.append(row)
            print(matrix1)
           
            for col in range(cols1):
                  count=0
                  for row in range(row1):
                     num=matrix1[row][col]
                     if num>2:
                       sum=0
                  
                       for k in range(1,(num//2)+1):
                          if num%k==0:
                            sum+=k
                       if sum==num:
                        
                          count+=1
                  print("Col",row+1,"perfecxt no count=",count)
         case 3:
            row1=int(input("Enter the rows:"))
            cols1=int(input("Enter the cols:"))
            matrix1=[]
            for i in range(row1):
               row=[]
               for j in range(cols1):
                  x =int(input("Enter the Elements:"))
                  row.append(x)
               matrix1.append(row)
            print(matrix1)
            for row in range(row1):
                count=0
                sum=0
                for col in range(cols1):
                     num= matrix1[row][col]
                     sum+=num
                print("Sum of ",row+1,"is",sum)
         case 4:
            print("Exiting")
            exit() """

#QUESTION 3
"""
3.

=========================================================
         MATRIX QUALITY CHECK SYSTEM
=========================================================

Scenario

A manufacturing company records quality inspection values in
matrix form. The Quality Control team wants a menu-driven
application to analyze the inspection data and generate reports.

The application should allow the user to:

1. Count Armstrong Numbers Row-wise
2. Count Palindrome Numbers Column-wise
3. Display Average of Each Row
4. Exit

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user selects Exit.

   1. Count Armstrong Numbers Row-wise
   2. Count Palindrome Numbers Column-wise
   3. Display Average of Each Row
   4. Exit

2. Read the number of rows and columns from the user.

3. Read all matrix elements from the user.

4. Based on the user's choice:

   Choice 1 - Count Armstrong Numbers Row-wise
   -------------------------------------------
   Count and display the number of Armstrong numbers
   present in each row.

   Examples:
   153, 370, 371, 407

5. Choice 2 - Count Palindrome Numbers Column-wise
   -----------------------------------------------
   Count and display the number of palindrome numbers
   present in each column.

   Examples:
   121, 131, 444, 1221

6. Choice 3 - Display Average of Each Row
   --------------------------------------
   Calculate and display the average of each row.

7. Choice 4 - Exit
   --------------------------------------
   Display:
   "Thank You for Using Matrix Quality Check System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Menu
1. Count Armstrong Numbers Row-wise
2. Count Palindrome Numbers Column-wise
3. Display Average of Each Row
4. Exit

Enter your choice: 1

Enter rows: 3
Enter columns: 3

Enter matrix elements:
153 121 10
370 22 44
407 15 131

Output:
Row 1 Armstrong Count = 1
Row 2 Armstrong Count = 1
Row 3 Armstrong Count = 1

---------------------------------------------------------

Enter your choice: 2

Output:
Column 1 Palindrome Count = 0
Column 2 Palindrome Count = 3
Column 3 Palindrome Count = 2

========================================================= """
#SOLUTION 3 
""" while True:
      print("======Menu======")
      print("1. Count Armstrong Numbers Row-wise ")
      print("2. Count Pelindrome Numbers Column-wise")
      print("3. Display Average  of Each row") 
      print("4. Exit") 
      choice=int(input("Enter the choice:"))
      match choice:
         case 1:
            row1=int(input("Enter the rows:"))
            cols1=int(input("Enter the cols:"))
            matrix1=[]
            for i in range(row1):
               row=[]
               for j in range(cols1):
                  x =int(input("Enter the Elements:"))
                  row.append(x)
               matrix1.append(row)
            print(matrix1)
            for row in range(row1):
                count=0
                for col in range(cols1):
                     num= matrix1[row][col]
                     temp=num
                     b=len(str(num))
                     sum=0
                     while num>0:
                              digit=num%10
                              sum=sum+digit**b
                              num//=10
                     else:
                       if sum==temp:
                        count+=1
                print("Row",row+1,"count=",count)
         case 2:
            row1=int(input("Enter the rows:"))
            cols1=int(input("Enter the cols:"))
            matrix1=[]
            for i in range(row1):
               row=[]
               for j in range(cols1):
                  x =int(input("Enter the Elements:"))
                  row.append(x)
               matrix1.append(row)
            print(matrix1)
           
            for col in range(cols1):
                  count=0
                  for row in range(row1):
                     num=matrix1[row][col]
                     temp=num
                     rev=""
                     while num>0:
                         digit=num%10
                         rev=rev+str(digit)
                         num//=10
                     if int(rev)==temp:
                         count+=1
                  print("pelindrome",row+1,"col=",count) 
                                   
         case 3:
            row1=int(input("Enter the rows:"))
            cols1=int(input("Enter the cols:"))
            matrix1=[]
            for i in range(row1):
               row=[]
               for j in range(cols1):
                  x =int(input("Enter the Elements:"))
                  row.append(x)
               matrix1.append(row)
            print(matrix1)
            for row in range(row1):
                count=0
                sum=0
                for col in range(cols1):
                     num= matrix1[row][col]
                     sum+=num
                     avg=sum//cols1 
                print("Avg of ",row+1,"is",avg)
         case 4:
            print("Exiting")
            exit() """


#QUESTION 4 
""" 
4.

=========================================================
        MATRIX DIAGONAL ANALYSIS SYSTEM
=========================================================

Scenario

A security company stores surveillance data in matrix form.
The analyst wants a menu-driven application to examine the
diagonal elements of the matrix and generate reports.

The application should allow the user to:

1. Display Main Diagonal Elements
2. Display Secondary Diagonal Elements
3. Compare Main and Secondary Diagonal Sums
4. Exit

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user selects Exit.

   1. Display Main Diagonal Elements
   2. Display Secondary Diagonal Elements
   3. Compare Main and Secondary Diagonal Sums
   4. Exit

2. Read the size of a square matrix from the user.

3. Read all matrix elements from the user.

4. Based on the user's choice:

   Choice 1 - Display Main Diagonal Elements
   -----------------------------------------
   Display all elements present in the main diagonal.

5. Choice 2 - Display Secondary Diagonal Elements
   ----------------------------------------------
   Display all elements present in the secondary diagonal.

6. Choice 3 - Compare Main and Secondary Diagonal Sums
   ---------------------------------------------------
   Calculate the sum of both diagonals and display:

   - Main Diagonal Sum
   - Secondary Diagonal Sum
   - Which diagonal has the greater sum
   - Or whether both sums are equal

7. Choice 4 - Exit
   -----------------------------------------
   Display:
   "Thank You for Using Matrix Diagonal Analysis System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Enter size of matrix: 3

Enter matrix elements:

1 2 3
4 5 6
7 8 9

Menu
1. Display Main Diagonal Elements
2. Display Secondary Diagonal Elements
3. Compare Main and Secondary Diagonal Sums
4. Exit

Enter your choice: 1

Output:
Main Diagonal Elements:
1 5 9

---------------------------------------------------------

Enter your choice: 2

Output:
Secondary diagonal Elements:
3 5 7

---------------------------------------------------------

Enter your choice: 3

Output:
Main Diagonal Sum = 15
Secondary Diagonal Sum = 15
Both Diagonal Sums are Equal

========================================================= """
#SOLUTION 4
""" while True:
      print("======Menu======")
      print("1. Main Diagonal elemnets")
      print("2. Secondary Diagonal elemnets")
      print("3. Sum of both diagonals ")
      print("4. Exit") 
      choice=int(input("Enter the choice:"))
      match choice:
         case 1:
            matrix1=[]
            print("Details of Matrix1")
            rows1=int(input("Enter the rows:"))
            cols1=int(input("Enter the cols:"))
            for i in range(rows1):
               row=[]
               for j in range(cols1):
                  row.append(int(input()))
               matrix1.append(row) 
            print()
            print("Ele are:")
            for i in range(len(matrix1)):
               for j in matrix1[i]:
                  print(j,end=" ")
               print()
            if rows1!=cols1:
               print("Matrix doesn't have diagonals")
            else:
               print("Main diagonal Element")
               for i in range(rows1):
                   print(matrix1[i][i],end=" ")
               print()
         case 2:
            matrix1=[]
            print("Details of Matrix1")
            rows1=int(input("Enter the rows:"))
            cols1=int(input("Enter the cols:"))
            for i in range(rows1):
               row=[]
               for j in range(cols1):
                  row.append(int(input()))
               matrix1.append(row) 
            print()
            print("Ele are:")
            for i in range(len(matrix1)):
               for j in matrix1[i]:
                  print(j,end=" ")
               print()
            if rows1!=cols1:
               print("Matrix doesn't have diagonals")
            else:
                print("seconadry  diagonal Element")
                for i in range(rows1):
               
                   print(matrix1[i][cols1-1-i],end=" ")
            print()
         case 3:
            matrix1=[]
            print("Details of Matrix1")
            rows1=int(input("Enter the rows:"))
            cols1=int(input("Enter the cols:"))
            for i in range(rows1):
               row=[]
               for j in range(cols1):
                  row.append(int(input()))
               matrix1.append(row) 
            print()
            print("Ele are:")
            for i in range(len(matrix1)):
               for j in matrix1[i]:
                  print(j,end=" ")
               print()
            if rows1!=cols1:
               print("Matrix doesn't have diagonals")
            else:
               summ=0
               for i in range(rows1):
                  summ+=matrix1[i][i]
               print("Main diagonal Element:",summ)
            
               summs=0
               for j in range(rows1):
                  summs+=matrix1[j][cols1-1-j]
               print("secondaru sum diagonals:",summs)
               if summ==summs:
                  print("Both Diagonal Sums are Equal")
               else:
                  print("Not Both Diagonal Sums are Equal")
 """