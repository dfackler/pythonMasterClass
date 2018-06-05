fruits = ['apple', 'mango', 'peach', 'orange']
ap_ind = fruits.index('apple')
item = 'banana'

if item not in fruits:
    fruits.insert(ap_ind, 'banana')
fruits.append('chocolate')

print(fruits)