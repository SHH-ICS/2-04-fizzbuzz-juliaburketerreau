# My Python Program
# Task:  use if statements to output the result of the game fizzbuzz.  
# Start at 1
# For multiples of 3, output   Fizz
# For multiples of 5, output   Buzz
# For multiples of 15, output   FizzBuzz
# End at 32
fizz = 3
buzz = 5
fizzbuzz = 15
for myNumber in range(1, 33):
  if myNumber % fizzbuzz == 0:
    print("fizzbuzz")
  elif myNumber % fizz == 0:
    print("fizz")
  elif myNumber % buzz == 0:
    print("buzz")
  else:
    print(myNumber)



