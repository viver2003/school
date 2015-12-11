import math

x = int(raw_input('number'))

a = math.floor(x/1000)
b = math.floor((x - (a * 1000))/100)
c = math.floor((x - (a * 1000) - (b * 100))/10)
d = math.floor((x - (a * 1000) - (b * 100) - (c * 10)))

print a
print b
print c
print d

if a == b == c == d:
    print 'all of these numbers are the same'
if a != b != c != d:
    print 'none of these numbers are the same'
if a == b:
        print 'a and b are the same'
if a == c:
        print 'a and c are the same'
if a == d:
        print 'a and d are the same'
if b == c:
        print 'b and c are the same'
if b == d:
        print 'b and d are the same'
if c == d:
        print 'c and d are the same'
if a == b == c:
        print 'a, b, and c are the same'
if a == b == d:
        print 'a, b, and d are the same'
if b == d == c:
        print 'b, d, and c are the same'

