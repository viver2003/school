x = float(input('number:'))
y = float(input('another number:'))
counter = 1
answer_found = False

while answer_found == False:
    if counter%x == 0 and counter%y == 0:
        answer_found = True
        print (('The lcm of %d and %d is ' + str(counter)) % (x,y))
    else:
        counter = counter + 1

