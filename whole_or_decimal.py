import math
x=float(input('number'))
if x == 0:
    print 'This number is niether positive nor negative!'
elif x > 0:
    print 'This number is a positive number!'
else:
    print 'This number is a negative number!'
if x%2:
    print 'This is a whole number!'
else:
    print 'This is a decimal!'
