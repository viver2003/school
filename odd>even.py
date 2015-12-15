x = float(input('input a number: '))
y = float(input('input another number: '))
n = float(input('input yet another number: '))

if x % 2 == 0 and y % 2 == 0:
    print 'There are more even numbers than odd numbers!'
if x % 2 == 0 and n % 2 == 0:
    print 'There are more even numbers than odd numbers!'
if y % 2 == 0 and n % 2 == 0:
    print 'There are more even numbers than odd numbers!'
if x % 2 == 1 and y % 2 == 1:
    print 'There are more odd numbers than even numbers!'
if x % 2 == 1 and n % 2 == 1:
    print 'There are more odd numbers than even numbers!'
if y % 2 == 1 and n % 2 == 1:
    print 'There are more odd numbers than even numbers!'
