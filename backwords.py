x = input('your first name')
name_length = len(x)
'''
print x[3:4]
print x[2:3]
print x[1:2]
print x[0:1]
'''
y = ''
counter = name_length
while counter > 0:
    y = y + x[(counter - 1): counter]
    counter = counter - 1
print y
