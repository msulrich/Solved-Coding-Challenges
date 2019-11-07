'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

You're given a string consisting solely of (, ), and *. * can represent either a (, ), or an empty string. 

Determine whether the parentheses are balanced.

For example, (()* and (*) are balanced. )*( is not balanced.
'''

# Start of Program =====================================================================

String = "((**()(()**)))*)*(()*)" # Random Example String
print('Given String: ',String)
print(' ')

List = list(String) # Convert the string to a list

print('String Converted to List: ',List)
print(' ')

Length = len(List) # Get the amount of characters in the list to use in the while loop

print('# of characters in string = ',Length) # See number of characters in string

leftPar = 0 # Initialize the left parentheses counter
rightPar = 0 # Initialize the right parentheses counter
asterisk = 0 # Initialize the asterisk counter

check = 0 # This value will turn to 1 when the imbalance if the imbalance is reached

for i in List: # Iterate over the list
  print(i) # See which character is being checked in the while loop
  if i == '(':
    leftPar += 1 # a += b is shorthand for a = a + b
    print('leftPar = ',leftPar) # Helps track the count of this character
    print('asterisk = ',asterisk) # Helps track the count of this character
  elif i == ')':
    if leftPar > 0:
      leftPar -= 1
      print('leftPar = ',leftPar) # Helps track the count of this character
      print('asterisk = ',asterisk) # Helps track the count of this character
    elif asterisk > 0:
      asterisk -= 1
      print('leftPar = ',leftPar) # Helps track the count of this character
      print('asterisk = ',asterisk) # Helps track the count of this character
    else:
      check = 1 # The string is determined as imbalanced
      print('Point of imbalance reached here')
  elif i == '*':
    if leftPar > 0:
      leftPar -= 1
      print('leftPar = ',leftPar) # Helps track the count of this character
      print('asterisk = ',asterisk) # Helps track the count of this character
    else:
        asterisk += 1
        print('leftPar = ',leftPar) # Helps track the count of this character
        print('asterisk = ',asterisk) # Helps track the count of this character
print(' ')

if check == 0: # The result is printed
  print('Balanced')
else:
  print('Unbalanced')

# End of Program =======================================================================
