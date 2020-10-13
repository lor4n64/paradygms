seconds = float(input('enter seconds'))
hour = seconds//3600
minutes = seconds//60-(hour*60)
print('{:5}{:5}'.format(hour, minutes,))
