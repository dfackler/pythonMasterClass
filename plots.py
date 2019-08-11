from matplotlib import pylab
import random

pylab.figure(1) #create figure 1
# pylab.plot([1,2,3,4], [1,7,3,5]) #draw on figure 1
# pylab.show() #show figure on screen

principal = 10000
interestRate = .05
years = 20
values = []
for i in range(years+1):
    values.append(principal)
    principal += principal*interestRate
pylab.plot(values, 'b-')

pylab.title('5% Growth, Compounded Anually', fontsize = 'xx-large')
pylab.xlabel('Years of Compounding')
pylab.ylabel('Value of Principal ($)')

#pylab.show()


pylab.figure(2)
vals = [1,200]
for i in range(1000):
    num1 = random.choice(range(1, 100))
    num2 = random.choice(range(1, 100))
    vals.append(num1+num2)
pylab.hist(vals, bins = 10)
pylab.show()