"""
Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

Enter Hours: 45
Enter Rate: 10
Pay: 475.0
"""
input_hours = input('Enter hours: ')
input_rate = input('Enter rate: ')
hours = float(input_hours)
rate = float(input_rate)

if hours > 40:
  overtime = hours - 40
  pay = (rate * 40) + (1.5 * rate * overtime)
else :
  pay = rate * hours

print('Pay: ', pay)