'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given a pivot x, and a list lst, partition the list into three parts.

    The first part contains all elements in lst that are less than x
    The second part contains all elements in lst that are equal to x
    The third part contains all elements in lst that are larger than x

Ordering within a part can be arbitrary.

For example, given x = 10 and lst = [9, 12, 3, 5, 14, 10, 10], one partition may be [9, 3, 5, 10, 10, 12, 14].
'''

# MY SOLUTION: >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Start of Program =====================================================================

x = int(input()) # The program asks the user to define the pivot

Fst = [9, 12, 3, 5, 14, 10, 10] # This is the list to partition as given in the problem

# This for loop will give all values in the list less than the pivot to list(A)
A = [] # Creates empty list A
for i in Fst:
  if (i < x):
    A.append(i)
    print(A)

# This for loop will give all values in the list less than the pivot to list(B)
B = [] # Creates empty list B
for i in Fst:
  if (i == x):
    B.append(i)
    print(B)

# This for loop will give all values in the list less than the pivot to list(C)
C = [] # Creates empty list C
for i in Fst:
  if (i > x):
    C.append(i)
    print(C)

# The final list is created to list the three partitions in order
D = [] # Creates empty list D
D.extend(A)
D.extend(B)
D.extend(C)
print(D)

# End of Program =======================================================================