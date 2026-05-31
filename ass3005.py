
#QUESTION 1
""" NOTE: In all programs, read the length and list elements from the user.

====================================================================

1. First Non-Repeating Number
   ====================================================================

Scenario

An online voting system stores vote IDs in a list.

Find the first vote ID that appears only once.

Requirements

* Read N and list elements from user
* Find the first non-repeating number
* If no such number exists, display an appropriate message

Test Case 1

Input:
[4, 5, 1, 2, 1, 2, 4]

Output:
First Non-Repeating Number = 5

Test Case 2

Input:
[7, 7, 8, 8]

Output:
No Non-Repeating Number Found

--- """

#SOLUTION 1
""" n=int(input("Enter the No of inputs:"))
arr=[]
for i in range(n):
    x=int(input("Enter the number:"))
    arr.append(x)
print(arr)
for i in arr:
    if arr.count(i)==1:
        print("First Non-Repeating Number =",i)
        break
else:
    print("No Non-Repeating Number Found") """


#QUESTION 2
""" ====================================================================
2. First Repeating Number
=========================

Scenario

A security system logs employee IDs.

Find the first ID that repeats in the list.

Requirements

* Read N and list elements from user
* Find the first repeating number
* If no repeating number exists, display an appropriate message

Test Case 1

Input:
[10, 5, 3, 4, 3, 5]

Output:
First Repeating Number = 3

Test Case 2

Input:
[1, 2, 3, 4]

Output:
No Repeating Number Found

--- """
#SOLUTION 2
""" n=int(input("Enter the No of inputs:"))
arr=[]
for i in range(n):
    x=int(input("Enter the number:"))
    arr.append(x)
print(arr) 
for i in arr:
    if arr.count(i)>1:
        print("First Repeating Number =",i)
        break
else:
    print("No Repeating Number Found") """

#QUESTION 3
""" 
====================================================================
3. Missing Number Detector
==========================

Scenario

Numbers from 1 to N should exist in a sequence, but one number is missing.

Requirements

* Read N and list elements from user
* Find the missing number
* Assume numbers belong to the range 1 to N+1

Test Case 1

Input:
[1, 2, 3, 5]

Output:
Missing Number = 4

Test Case 2

Input:
[2, 3, 4, 5]

Output:
Missing Number = 1

Test Case 3

Input:
[1, 2, 4, 5]

Output:
Missing Number = 3

--- """
#SOLUTION 3
""" n=int(input("Enter the No of inputs:"))
arr=[]
for i in range(n):
    x=int(input("Enter the number:"))
    arr.append(x)
print(arr)
for i in range(1,n+1):
    if i not in arr:
        print("Missing value=",i)
        break """

#QUESTION 4
""" 
====================================================================
4. Longest Consecutive Sequence
===============================

Scenario

Find the longest sequence of consecutive numbers present in the list.

Requirements

* Read N and list elements from user
* Find the length of the longest consecutive sequence
* Display the sequence length

Test Case 1

Input:
[100, 4, 200, 1, 3, 2]

Output:
Longest Consecutive Length = 4

Explanation:
Sequence = 1, 2, 3, 4

Test Case 2

Input:
[10, 11, 12, 20]

Output:
Longest Consecutive Length = 3

--- """
#SOLUTION 4
""" n=int(input("Enter the No of inputs:"))
arr=[]
for i in range(n):
    x=int(input("Enter the number:"))
    arr.append(x)
print(arr)
count=0
arr.sort()
for i in range(arr[0],arr[-1]):
    if i not in arr:
        break
    count+=1
print("Consecutive length=",count) """


#QUESTION 5
""" ====================================================================
5. Equilibrium Index Finder
===========================

Scenario

Find an index where:

# Sum of elements on the left side

Sum of elements on the right side

Requirements

* Read N and list elements from user
* Find equilibrium index
* If not found, display message

Test Case 1

Input:
[1, 3, 5, 2, 2]

Output:
Equilibrium Index = 2

Explanation:
1 + 3 = 2 + 2

Test Case 2

Input:
[1, 2, 3]

Output:
No Equilibrium Index Found

--- """
#SOLUTION 5
""" n=int(input("Enter the No of inputs:"))
arr=[]

for i in range(n):
    x=int(input("Enter the number:"))
    arr.append(x)
found=False
for i in range(n):
    lsum=0
    rsum=0
    for j in range(i):
        lsum+=arr[j]
    for k in range(i+1,n):
        rsum+=arr[k]
    if lsum==rsum:
        print("Euillibrium index",i)
        found=True
        break
if found==False:      

    print("No Eaquillibrium index found") """



#QUESTION 6
""" ====================================================================
6. Product Except Self
======================

Scenario

For every element, calculate the product of all other elements except itself.

Requirements

* Read N and list elements from user
* Create a new list containing products
* Display the result

Test Case 1

Input:
[1, 2, 3, 4]

Output:
[24, 12, 8, 6]

Test Case 2

Input:
[2, 3, 5]

Output:
[15, 10, 6]

--- """
#SOLUTION 6
""" n=int(input("Enter the No of inputs:"))
arr=[]
pro=[]
for i in range(n):
    x=int(input("Enter the number:"))
    arr.append(x)
totalpro=1
for i in arr:
    totalpro*=i
for i in arr:
    k=totalpro//i
    pro.append(k)
print(pro) """
            

#QUESTION 7
""" ====================================================================
7. Array Rotation Analyzer
==========================

Scenario

Rotate the array K times towards the right.

Requirements

* Read N and list elements from user
* Read K
* Rotate the array
* Display rotated array

Test Case 1

Input:
Array = [1, 2, 3, 4, 5]
K = 2

Output:
[4, 5, 1, 2, 3]

Test Case 2

Input:
Array = [10, 20, 30, 40]
K = 1

Output:
[40, 10, 20, 30]

---
 """
#SOLUTION 7
""" n=int(input("Enter the No of inputs:"))
k=int(input("Enter the No of Rotation:"))
arr=[]
for i in range(n):
    x=int(input("Enter the number:"))
    arr.append(x)
arr=arr[k:]+arr[:k]
print(arr) """


#QUESTION 8
""" ====================================================================
8. Majority Element Detector
============================

Scenario

Find an element occurring more than N/2 times.

Requirements

* Read N and list elements from user
* Find majority element
* If not present, display appropriate message

Test Case 1

Input:
[2, 2, 1, 2, 3, 2, 2]

Output:
Majority Element = 2

Test Case 2

Input:
[1, 2, 3, 4]

Output:
No Majority Element Found

--- """
#SOLUTION 8
"""n=int(input("Enter the No of inputs:"))
arr=[]
for i in range(n):
    x=int(input("Enter the number:"))
    arr.append(x)
max=arr[0]
c=0
flag=False
for i in arr:
    for j in arr:
        if i!=j and arr.count(i)>arr.count(j):
           flag=True
if flag:
    print("Majority element ",i)
else:
    print("No majority element found")  """     
    





#QUESTION 9
""" ====================================================================
9. Happy Number List Analyzer
=============================

Scenario

Store numbers in a list and identify Happy Numbers.

A number is called Happy if repeatedly replacing it by the sum of squares of its digits eventually becomes 1.

Example

19

1² + 9² = 82

8² + 2² = 68

6² + 8² = 100

1² + 0² + 0² = 1

Therefore, 19 is a Happy Number.

Another Example

7

7² = 49

4² + 9² = 97

9² + 7² = 130

1² + 3² + 0² = 10

1² + 0² = 1

Therefore, 7 is a Happy Number.

Non-Happy Number Example

4

4² = 16

1² + 6² = 37

3² + 7² = 58

5² + 8² = 89

8² + 9² = 145

1² + 4² + 5² = 42

4² + 2² = 20

2² + 0² = 4

Again 4 appears and the cycle repeats.

Therefore, 4 is NOT a Happy Number.

Requirements

* Read N and list elements from user
* Find all Happy Numbers
* Store Happy Numbers in another list
* Count Happy Numbers
* Find Largest Happy Number
* Display Happy Number List

Test Case 1

Input:
[19, 7, 4, 20]

Output:
Happy Numbers = [19, 7]
Count = 2
Largest Happy Number = 19

Test Case 2

Input:
[13, 10, 4]

Output:
Happy Numbers = [13, 10]
Count = 2
Largest Happy Number = 13

Test Case 3

Input:
[2, 3, 4]

Output:
Happy Numbers = []
Count = 0
Largest Happy Number = Not Available

--- """
#SOLUTION 9
numbers = []
n = int(input("Enter count: "))

for i in range(n):
    num = int(input(f"Enter numbers: "))
    numbers.append(num)

happy = []

for num in numbers:
    temp = num
    ishappy = True
    countsteps = 0

    while temp != 1:
        if countsteps > 100:
            ishappy = False
            break
        total = 0
        while temp > 0:
            digit = temp % 10
            total += digit ** 2
            temp //= 10
        temp = total
        countsteps += 1

    if ishappy:
        happy.append(num)

count = len(happy)

if happy:
    largest = happy[0]
    for h in happy:
        if h > largest:
            largest = h
else:
    largest = "Not Available"

print(f"Happy Numbers = {happy}")
print(f"Count = {count}")
print(f"Largest Happy Number = {largest}")


#QUESTION 10
""" ====================================================================
10. Find Duplicate Numbers
==========================

Scenario

A company stores employee IDs in a list. Some IDs may appear more than once due to data entry errors.

Requirements

* Read N and list elements from user
* Find all duplicate numbers
* Store duplicates in another list
* Count total duplicate numbers
* Display duplicates in sorted order

Test Case 1

Input:
[1, 2, 3, 2, 4, 5, 1]

Output:
Duplicate Numbers = [1, 2]
Count = 2

Test Case 2

Input:
[10, 20, 30]

Output:
No Duplicate Numbers Found

--- """
#solution 10
""" n=int(input("Enter the No of inputs:"))
arr=[]
dup=[]
for i in range(n):
    x=int(input("Enter the number:"))
    arr.append(x)
count=0 
for i in arr:
    if arr.count(i)>1:
        if i not in dup:
            pass
            dup.append(i)
            count+=1
if len(dup)==0:
    print("No dup values")
else:
    print("Duplicate Numbers",dup) 
    print("count=",count)
dup.sort()
print("Sorted dupliacted numbers",dup) """
    
