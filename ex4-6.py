"""
Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and
create a function called computepay which takes two parameters(hours and rate).

Enter Hours: 45
Enter Rate: 10
Pay: 475.0
"""

def computepay(hours, rate):
  if hours > 40:
    overtime = hours - 40
    pay = (rate * 40) + (1.5 * rate * overtime)
  else:
    pay = rate * hours

  print('Pay: ', pay)

# check if the input value is able to convert to float
def checkForFloat(inputVal):
  try:
    val = float(inputVal)
    return val
  except ValueError:
    print('Error, please enter numeric input')
    quit()


input_hours = input('Enter Hours:')
hours = checkForFloat(input_hours)

input_rate = input('Enter Rate:')
rate = checkForFloat(input_rate)

computepay(hours, rate)
