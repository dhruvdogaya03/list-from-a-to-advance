#QUESTION 1
""" NOTE: in all the programs read length and array elements from user
=====================================================================
1.Student Marks Management
Create a program to store student marks in a List and perform operations.

Requirements:

Add student marks into a List
Display all marks
Find highest and lowest marks
Count students who scored above 75

Test Cases:

Input: [45, 67, 89, 90, 76] → Highest = 90, Lowest = 45, Count Above 75 = 3
Input: [10, 20, 30] → Highest = 30, Lowest = 10, Count Above 75 = 0
Input: [100, 99, 98] → Highest = 100, Lowest = 98, Count Above 75 = 3
 """
#SOLUTION1 
""" marks=int(input("Enter the No marks:"))
arr=[]
for i in range(marks):
    x=int(input("Enter the marks:"))
    arr.append(x)
max=0
small=arr[0]
count=0
for i in arr:
    if i>max:
        max=i
    if i<small:
        small=i
    if i>75:
        count+=1
print("Highest=",max,end=",")
print("lowest=",small,end=",")
print("count above=",count,end="")

 """

#QUESTION 2 
""" 2.Employee Salary Processing
Store employee salaries in a List and calculate details.

Requirements:

Store salaries
Find average salary
Display salaries greater than average
Remove salaries below 15000

Test Cases:

Input: [10000, 20000, 30000] → Average = 20000, Above Average = 30000
Input: [15000, 15000, 15000] → Average = 15000
Input: [5000, 7000] → Remaining List = []
 """
#SOLUTION 2 
""" marks=int(input("Enter the No salaries:"))
arr=[]
for i in range(marks):
    x=int(input("Enter the salary:"))
    if x<15000:
        continue
    else:
        arr.append(x)
print(arr)
sum=0
for i in arr:
    sum+=i
    
avg=sum//len(arr)
print("Average=",avg,end=",")
count=0
for i in arr:
    if i> avg:
        count+=1

print("Above Average:",count)
  """

#QUESTION 3
"""
3.
# Assignment: Prime Number Analyzer using List (Python)

## Scenario

A coaching institute stores student lucky numbers in a Python List.
Your task is to analyze the list and identify prime numbers for a scholarship selection process.

You must iterate through every element of the list and perform prime number analysis.

---

# Requirements

Write a Python program to:

1. Store integer values in a List
2. Iterate through all elements of the List
3. Check whether each number is prime or not
4. Display all prime numbers
5. Count total prime numbers
6. Count total non-prime numbers
7. Find the largest prime number from the List
8. Store all prime numbers into another List
9. Sort the prime numbers in ascending order and display them

---

# Test Case 1

## Input

[2, 3, 4, 5, 6, 7, 8]

## Expected Output

Prime Numbers: 2 3 5 7
Prime Count: 4
Non-Prime Count: 3
Largest Prime Number: 7
Prime List: [2, 3, 5, 7]
Sorted Prime List: [2, 3, 5, 7]

---

# Test Case 2

## Input

[10, 11, 12, 13, 14, 15]

## Expected Output

Prime Numbers: 11 13
Prime Count: 2
Non-Prime Count: 4
Largest Prime Number: 13
Prime List: [11, 13]
Sorted Prime List: [11, 13]

---

# Test Case 3

## Input

[1, 2, 17, 19, 20, 25]

## Expected Output

Prime Numbers: 2 17 19
Prime Count: 3
Non-Prime Count: 3
Largest Prime Number: 19
Prime List: [2, 17, 19]
Sorted Prime List: [2, 17, 19]

---

# Test Case 4

## Input

[4, 6, 8, 9, 10]

## Expected Output

Prime Numbers: None
Prime Count: 0
Non-Prime Count: 5
Largest Prime Number: Not Available
Prime List: []
Sorted Prime List: []

---

# Test Case 5

## Input

[29, 31, 37, 41]

## Expected Output

Prime Numbers: 29 31 37 41
Prime Count: 4
Non-Prime Count: 0
Largest Prime Number: 41
Prime List: [29, 31, 37, 41]
Sorted Prime List: [29, 31, 37, 41] """
#SOLUTION 3
""" 
n=int(input("Enter the No marks:"))
num=[]
prime=[]
nonprime=[]
for i in range(n):
    x=int(input("Enter the maks:"))
    num.append(x)
for i in num:
    if i<1:
        print("Cant find prime no00")
    else:
        flag=True
        for j in range(2,i//n+1):
            if i%j==0:
                flag=False
    if flag:
        prime.append(i)
    else:
        nonprime.append(i)
print("Prime list:",prime)
print("Non prime list:",nonprime)
count=0
max=0
for i in prime:
    count+=1
    if i>max:
        max=i
print("Prime count",count)
print("MAximum prime no:",max)
count2=0
for i in nonprime:
    count2+=1
print("Non prime count",count2)
s=" ".join(map(str,prime))
print("Prime Numbers:",s)
prime.sort()
print("Sorted list",prime) """

#QUESTION 4
""" 

4.
Palindrome Number List Checker
Scenario

A system checks lucky numbers which are palindromes.

Requirements
Check palindrome numbers
Store palindrome numbers in list
Count palindrome numbers
Find largest palindrome
Sort palindrome list

Test Cases
Input:
[121, 131, 20, 44, 55, 100]

Output:

Palindromes: [121, 131, 44, 55]
Count: 4
Largest: 131
Sorted: [44, 55, 121, 131] """
""" 
n=int(input("Enter the No marks:"))
num=[]
peli=[]
nonpeli=[]
for i in range(n):
    x=int(input("Enter the maks:"))
    num.append(x)
for i in num:
    if str(i)==str(i)[::-1]:
        peli.append(i)
    else:
        nonpeli.append(i)
print("Pelindrome",peli)
count=0
l=0
for i in peli:
    count+=1
    if l<i:
        l=i
print("Count:",count) 
print("Largest:",l)
peli.sort()
print("Sorted list:",peli) """



""" 
5.
 Student Grade Classification System (Python List Assignment)
A school stores student marks in a list. The system must analyze the marks and generate a **clear performance report** 
by grouping students into grade categories.
Write a Python program to:
* Iterate through the list of marks
* Assign grades based on marks:
  * **>= 90 → A**
  * **>= 75 and < 90 → B**
  * **>= 50 and < 75 → C**
  * **< 50 → Fail**
* Store each category in separate lists
* Count students in each category
* Display a **final structured report (important)**
## 📌 Output Format (Mandatory)
Your output must be displayed exactly in this format:
===== STUDENT GRADE REPORT =====

A Grade Students   : [list]
B Grade Students   : [list]
C Grade Students   : [list]
Fail Students      : [list]

--------------------------------
A Count   : X
B Count   : X
C Count   : X
Fail Count: X
--------------------------------

Total Students: X
 Input

[95, 82, 67, 45, 30]

Output

```
===== STUDENT GRADE REPORT =====

A Grade Students   : [95]
B Grade Students   : [82]
C Grade Students   : [67]
Fail Students      : [45, 30]

--------------------------------
A Count   : 1
B Count   : 1
C Count   : 1
Fail Count: 2
--------------------------------

Total Students: 5

 """
#SOLUTIOON 5
""" 
n=int(input("Enter the No marks:"))
A=[]
B=[]
C=[]
F=[]
n1=[]
for i in range(n):
    x=int(input("Enter the maks:"))
    n1.append(x)
counta=0
countb=0
countc=0
countf=0

for i in n1:
    if i<101:

        if 100>=i>=90:
            A.append(i)
            counta+=1
        if 75<=i<90:
            B.append(i)
            countb+=1
        if 50<=i<75:
            C.append(i)
            countc+=1
        if i<50:
            F.append(i)
            countf+=1
    else:
        print("Invalid marks inputed:::")
        break
print("======STUDENTS GRADE REPORT======")
print("A Grade students:",A)
print("B Grade students:",B)
print("C Grade students:",C)
print("F Grade students:",F)
print("----------------------------------")
print("A count:",counta)
print("B count:",countb)
print("C count:",countc)
print("Fail count:",countf)
print("-----------------------------------")
print("Total students",n) """

#QUESTION 6
""" 
6.

 Frequency Count of Elements (Advanced Scenario-Based Problem)
A government survey department collects responses from different regions. Each response is stored as an integer in a list (representing selected option IDs).
The department wants to analyze:
* How many times each option was selected
* Most popular option
* Least popular option
* Detect invalid entries (negative numbers or zeros
 Requirements
Write a Python program to:
1. Store survey responses in a list
2. Ignore invalid entries (≤ 0)
3. Count frequency of each valid number
4. Display frequency in sorted order
5. Find the most frequently selected option
6. Find the least frequently selected option (excluding invalid data)
7. Store frequency in a dictionary
NOTE:
* Avoid using built-in `Counter`
## Input Format
A list of integers representing responses.
# Scenario 1: Normal Survey Data

## Input

[1, 2, 2, 3, 3, 3, 4, 1, 2]

## Output

```
Frequency Count:
1 → 2
2 → 3
3 → 3
4 → 1

Most Frequent: 2 or 3 (tie)
Least Frequent: 4
# Scenario 2: Data with Invalid Entries

## Input

[1, 2, -1, 3, 0, 2, 4, -5, 3, 3]

## Output

```
Invalid Entries Ignored: [-1, 0, -5]

Frequency Count:
1 → 1
2 → 2
3 → 3
4 → 1

Most Frequent: 3
Least Frequent: 1 or 4
```

---

# Scenario 3: Highly Skewed Data

## Input

[5, 5, 5, 5, 2, 2, 1]

## Output

```
Frequency Count:
1 → 1
2 → 2
5 → 4

Most Frequent: 5
Least Frequent: 1
```

---

# Scenario 4: All Same Values

## Input

[7, 7, 7, 7, 7]

## Output

```
Frequency Count:
7 → 5

Most Frequent: 7
Least Frequent: 7
```

---

# Scenario 5: Empty / Invalid Only Data

## Input

[-1, 0, -3]

## Output

```
No valid data found
```

--- """
#SOLUTIOON 6
""" 
n=int(input("Enter the No marks:"))
num=[]
ori=[]
for i in range(n):
    x=int(input("Enter the maks:"))
    num.append(x)
for i in num:
    if i>0:
        ori.append(i)
if ori==[]:
    print("Not valid input") 
else:
    print(ori)
count=0
s1=0

for i in ori:
    print(i,"->",ori.count(i))
    s=ori.count(i)
    if s1<s:
        s1=s
    
print("Highest frequency",s1)
for i in ori:
    if ori.count(i)==s1:
        print("Most Frequent",i)
        break
l=ori[0]
for i in range(len(ori)):
        if l<ori[i]:
             l=ori[i]
print("Least frequent:",l)
    

        

  """
n=[41,44,44]
for i in range()