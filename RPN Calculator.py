#Bevan Philip
#1001527799
#11/7/2020
#Mac
#Python 3.9.0

import operator  #operator module, contains basic operators

stack = []    #declare stack

#Setting each arithmetic operator to its function
operators = {'+': operator.add,
              '-': operator.sub,
              '*': operator.mul,
              '/': operator.truediv}

with open('text.txt', 'r') as file:    #opens and reads txt file
   lines = file.readlines()    #store each line from the file in the variable lines
   
#for each line
for line in lines:
  s = line
  for token in s.split():       #split line into tokens
    if token in operators:       #recognize operator
      #Topmost numbers are popped off and sets numbers as first and second and performs operation of the token between those numbers
      sec, fir = stack.pop(), stack.pop()
      ans = operators[token](fir, sec)
    else:                         #in case the token is neither an operator nor a number
      ans = float(token)          
    stack.append(ans)             #ans is pushed into stack
  if len(stack) == 1:        #pops out number from stack and prints them
    print(stack.pop())
with open('text.txt', 'r') as file:
   lines = file.readlines()
for line in lines:
   s = line

   
   

  


  
	


