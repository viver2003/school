a = int(input('first side'))
b = int(input('second side'))
c = int(input('third side'))
if (a + b > c) and (a + c > b) and (b + c > a):
    print "This is a valid triangle!!!"
    
else:
    print "These numbers cannot make a triangle."
