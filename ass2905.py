""" a=[2,0,4,0,6]
zero=[]
nonzero=[]
for i in a:
    if i==0:
        zero.append(i)
    else:
        nonzero.append(i)
print(nonzero+zero)
 """


""" 
n=int(input("Enter the No marks:"))
num=[]
prime=[]
nonprime=[]
for i in range(n):
    x=int(input("Enter the maks:"))
    num.append(x)
last=num[n-1]
i=n-1
while i>0:
    num[i]==num[i-1]
    i=i-1
num[0]=last
print(num) 
 """

#QUESTION 1
""" 
1.
Mountain Hiking Elevation Analysis

Problem Statement

A trekking company records the elevation (in meters) reached by a hiker at different checkpoints during a mountain climb.

A checkpoint is considered a peak checkpoint if its elevation is not smaller than its adjacent checkpoints.

Given an array elevation[] of size N, find the index of any one peak checkpoint.

Test Case 1

Input:
elevation = [1200, 1450, 1700, 1600, 1500]

Output:
2

Explanation:
1700 is greater than both adjacent values 1450 and 1600.

Test Case 2

Input:
elevation = [800, 900, 950, 1000]

Output:
3

Explanation:
Last element can also be a peak because it has no right neighbor.

Test Case 3

Input:
elevation = [3000]

Output:
0

Explanation:
Single element is always a peak. """
#SOLUTION1
""" n=int(input("Enter the No of inputs:"))
rev=[]
for i in range(n):
    x=int(input("Enter the number:"))
    rev.append(x)
print(rev)
peakindex=-1
for i in range(n):
    if i==0:
        if n==1 or rev[i]>=rev[i+1]:
            peakindex=i
            break
    elif i==n-1:
        if rev[i]>=rev[i-1]:
            peakindex=i
            break
    else:
        if rev[i-1]<=rev[i]>=rev[i+1]:
            peakindex=i
            break
if peakindex!=-1:
        print("The peakelemnt  element",rev[peakindex],"and index",peakindex)
else:
        print("Peak not found") """


#QUESTION 2
""" 
2.
Smart City Traffic Peak Load Analyzer

Problem Statement

A smart city monitors traffic density at different time intervals in a day.

An element is called a peak traffic point if it is greater than or equal to its adjacent elements.

You are given an array traffic[] of size N.

Tasks:

Find all peak elements
Calculate the sum of all peak traffic values
Find the product of all peak traffic values
Return the maximum peak value

Note:
If only one element exists, it is the only peak.

Test Case 1

Input:
traffic = [10, 50, 30, 70, 60, 90, 80]

Output:
Peaks = [50, 70, 90]
Sum = 210
Product = 315000
Max Peak = 90

Test Case 2

Input:
traffic = [100, 200, 150, 180, 170]

Output:
Peaks = [200, 180]
Sum = 380
Product = 36000
Max Peak = 200

Test Case 3

Input:
traffic = [5]

Output:
Peaks = [5]
Sum = 5
Product = 5
Max Peak = 5
 """
#SOLUTION2
""" n=int(input("Enter the No of inputs:"))
arr=[]
for i in range(n):
    x=int(input("Enter the number:"))
    arr.append(x)
print()
sum=0
pro=1
peak=[]
for i in range(n):
    if i==0:
        if n==1 or arr[i]>=arr[i+1]:
            peak.append[arr[i]]
    elif i==n-1:
        if arr[i]>=arr[i-1]:
            peak.append(arr[i])
    else:
        if arr[i-1]<=arr[i]>=arr[i+1]:
            peak.append(arr[i])
print("Peaks",peak) 
max=0
for i in peak:
    sum+=i
    pro*=i           
    if max<i:
        max=i
print("Sum=",sum)
print("Product=",pro)
print("MAx peak=",max) """

#QUESTION 3
""" 
3.
Industrial Sensor Peak Energy Monitoring System

Problem Statement

A factory machine records energy consumption at regular intervals.

A peak is defined as a value greater than or equal to its neighbors.

Tasks:

Find all peak energy values
Compute sum of squares of peak values
Compute average of peak values
Return difference between max peak and min peak
If no peaks, return -1

Test Case 1

Input:
energy = [20, 40, 30, 60, 50]

Output:
Peaks = [40, 60]
Sum of squares = 5200
Average = 50
Difference = 20

Test Case 2

Input:
energy = [10, 20, 15, 25, 20, 30]

Output:
Peaks = [20, 25, 30]
Sum of squares = 1925
Average = 25
Difference = 10 

Test Case 3
Input:
energy = [5]

Output:
Peaks = [5]
Sum of squares = 25
Average = 5
Difference = 0
 """
#SOLUTION3
""" n=int(input("Enter the No of inputs:"))
arr=[]
for i in range(n):
    x=int(input("Enter the number:"))
    arr.append(x)
print()
peak=[]
sumofsq=0
sum=0
diff=0
for i in range(n):
    if i==0:
        if n==1 or arr[i]>=arr[i+1]:
            peak.append[arr[i]]
    elif i==n-1:
        if arr[i]>=arr[i-1]:
            peak.append(arr[i])
    else:
        if arr[i-1]<=arr[i]>=arr[i+1]:
            peak.append(arr[i])
if peak==[]:
    print("inavalid input")
else:
    print("Peaks",peak) 
for i in peak:
    sq=i*i
    sum+=i
    avg=sum//len(peak)
    sumofsq+=sq
for i in range(len(peak)):
    diff+=abs(peak[len(peak)-1]-peak[i-1]) 
print("Difference=",diff)
print("SQuare:",sumofsq)
print("Average",avg)  """

#QUESTION 4
""" 
4.

Problem: Sum of Leaders in an Array After Filtering Invalid Data (Python)

Definition

A company collects daily performance scores of employees. However, the dataset may contain invalid entries.

An element is called a leader if:

It is greater than all elements to its right side
The element must be valid, i.e., it should not be:
Negative number
Zero

Rightmost valid element is always considered a leader.

Input Format
First line → integer n
Second line → n space-separated integers

Output Format
Single integer → sum of all valid leader elements
If no valid elements exist → return -1

Rules
Before finding leaders:

Ignore all negative values and zeros
Work only on positive numbers
Then find leaders from the filtered sequence

Test Case 1

Input:
8
16 0 17 4 -3 3 5 2

Processing:
Filtered array:
[16, 17, 4, 3, 5, 2]

Leaders:
[17, 5, 2]

Output:
24

Test Case 2

Input:
6
-1 0 -5 0 -2 -3

Output:
-1

Test Case 3

Input:
5
10 20 30 40 50

Processing:
Filtered array:
[10, 20, 30, 40, 50]

Leaders:
[50]

Output:
50
 """
#SOLUTION4

""" n=int(input("Enter the No of inputs:"))
arr=[]
for i in range(n):
    x=int(input("Enter the number:"))
    if x>0:
        arr.append(x)
print()
print(arr)
peak=[]
sum=0
l=len(arr)
for i in range(l):
    if i==0:
        if n==1 or arr[i]>=arr[i+1]:
            peak.append[arr[i]]
    elif i==l-1:
        if arr[i]>arr[i-1] or arr[i]<arr[i-1]:
            peak.append(arr[i])
    else:
        if arr[i-1]<=arr[i]>=arr[i+1]:
            peak.append(arr[i]) 
print(n)
print()
print("Processing..")
print("Filtered array:")
print(arr)
print("Leader:",peak) 
for i in peak:
    sum+=i
print("Sum=",sum) """

#QUESTION 5
""" 
5.
Given an unsorted array arr[] of size N having both negative and positive integers. 
The task is place all negative element at the end of array without changing the order of positive element and negative element.

Example 1:
Input : 
N = 8
arr[] = {1, -1, 3, 2, -7, -5, 11, 6 }
Output : 
1  3  2  11  6  -1  -7  -5

Example 2:
Input : 
N=8
arr[] = {-5, 7, -3, -4, 9, 10, -1, 11}
Output :
7  9  10  11  -5  -3  -4  -1
 """
#solution 5
""" n=int(input("Enter the No of inputs:"))
arr=[]
for i in range(n):
    x=int(input("Enter the number:"))
    arr.append(x)
print("N:",n) 
print("arr[] = {",arr,"}")
pos=[]
neg=[]
for i in arr:
    if i>0:
        pos.append(i)
    else:
        neg.append(i)
print("output:",pos+neg) """



""" 
6.

A security system logs employee entry IDs during a day.

Only prime-numbered IDs are considered valid VIP entries.

Tasks:

Extract all prime IDs from the list
Find the sum of prime IDs
Find the maximum prime ID
Count how many prime entries exist

Input:
A list of integers (may contain duplicates and non-prime numbers)

Example 1

Input:
[12, 5, 7, 9, 11, 14, 17]

Output:
Prime IDs = [5, 7, 11, 17]
Sum = 40
Max = 17
Count = 4

Example 2

Input:
[4, 6, 8, 10]

Output:
Prime IDs = []
Sum = 0
Max = -1
Count = 0
 """
#solution 6
""" n=int(input("Enter the No of inputs:"))
arr=[]
sum=0
mx=-1
count=0
for i in range(n):
    x=int(input("Enter the number:"))
    arr.append(x)
print(arr)
prime=[]
for i in arr:
    if i>0:
        for j in range(2,(i//2)+1):
            if i%j==0:
               break 
        else:
            prime.append(i)
print("Prime ID=",prime) 
for i in prime:
    sum+=i
    count+=1
for i in range(len(prime)):
    mx>prime[i]
    mx=prime[i]
print("Sum=",sum)
print("Maximum =",mx)
print("count=",count) """
    

#question 7 
""" 
7.
Factory Production – Factorial Expansion List

Problem Statement

A factory produces items where production capacity is defined using factorial growth.

Given a list of numbers, replace each number with its factorial value.

Then perform analysis on the resulting list.

Tasks:

Convert each element to factorial
Find sum of all factorial values
Find maximum factorial value
Count how many factorial values are even

Input:
A list of integers

Example 1

Input:
[3, 4, 5]

Processing:
3! = 6
4! = 24
5! = 120

Output:
[6, 24, 120]
Sum = 150
Max = 120
Even Count = 3 """
#solution 7 
""" n=int(input("Enter the No of inputs:"))
arr=[]
sum=0

count=0
for i in range(n):
    x=int(input("Enter the number:"))
    arr.append(x)
print(arr)
fact2=[]
print("Processing:")
for i in arr:
    fact=1
    for j in range(1,i+1):
        fact=fact*j 
        f=fact
    fact2.append(f)
    print(i,"! = ",fact) 
         
print(fact2 )
max=fact2[0]
for i in fact2:
   sum+=i
   if i%2==0:
       count+=1
   if max<=i:
       max=i
print(fact2)
print("sum=",sum)
print("Max=",max)
print("count=",count)     
    """
"""

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
Largest Happy Number = Not Available"""

""" numbers=[]
n=int(input("Entre the n inputs:"))
for i in range(n):
    x=int(input("Enter the numbers:"))
    numbers.append(x)
happy=[]
for num in numbers:
    temp=num
    ishappy=True
    countstep=0
    while temp!=1:
        if countstep>100:
            ishappy=False
            break
        total=0
        while temp>0:
            digit=temp%10
            total+=digit**2
            temp//=10
        temp=total
        countstep+=1


    if ishappy:
        happy.append(num) 
count=len(happy)
if happy:
    l=happy[0]
    for j in happy:
        if j>l:
            l=j
else:
    l="Not Availbale"
    
print("Happy numbers are",happy)
print("Count :",count)
print(f"Largesty happy number is {l}")

 """


