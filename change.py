import math

cost = float(input('price'))
paid = float(input('paid'))

#pr....
x = paid - cost
print x

#find dollars

dollars = math.floor(x)
print 'dollars = ' + str(dollars)

#you will find quarters

quarters = math.floor((x - dollars)/.25)
print 'quarters = ' + str(quarters)

#you will find dimes

dimes = math.floor((x - dollars - quarters*.25)/.10)
print 'dimes = ' + str(dimes)

#you will find nickles

nickles = math.floor((x - dollars - quarters*.25 - dimes*.10)/.05)
print 'nickles = ' + str(nickles)

#you will find pennies

pennies = 100*(x - dollars - quarters*.25 - dimes*.10 - nickles*.05)
print 'pennies = ' + str(pennies)
