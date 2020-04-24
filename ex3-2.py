"""
Rewrite your pay program using try and except so that your program handles
non-numeric input gracefully by printing a message and exiting the program.

The following shows two executions of the program:

Enter Hours: 20
Enter Rate: nine
Error, please enter numeric input

Enter Hours: forty
Error, please enter numeric input
"""

input_hours = input('Enter hours: ')

try:
  input_rate = input('Enter rate: ')
  hours = float(input_hours)
  rate = float(input_rate)

  if hours > 40:
    overtime = hours - 40
    pay = (rate * 40) + (1.5 * rate * overtime)
  else :
    pay = rate * hours

  print('Pay: ', pay)
except:
  print('Error, please enter numeric input')

