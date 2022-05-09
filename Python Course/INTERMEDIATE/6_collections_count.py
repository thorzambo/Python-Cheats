# Collections
#import collections
from collections import Counter
# Built in module in Py -> allows us to have diff multiple presets Data Types so we can store informations
# translates few for loops into 1 line

# CONTAINER -> Objects that store multiple objects
# list
# set
# dict
# tuple - inmutable

# TYPES -> Implemented into collections Module
# 1 counter
# 2 deque
# 3 namedTuple()
# 4 orderdDict
# 5 defaultdict

c = Counter() # into the Counter method can be any collection Data Type or Container ^
print(c)

c = Counter('Shesh_string example') 
print(c)

c = Counter(['a', 'b', 'c', 'b', 'b', 'c'])
print(c)

c = Counter({'a':1, 'b':2, 'c':3})
print(c)

c = Counter(cats=4, dogs=7)
print(c)


''' 
Counter()
Counter({'e': 3, 'h': 2, 's': 2, 'S': 1, '_': 1, 't': 1, 'r': 1, 'i': 1, 'n': 1, 'g': 1, ' ': 1, 'x': 1, 'a': 1, 'm': 1, 'p': 1, 'l': 1})
Counter({'b': 3, 'c': 2, 'a': 1})
Counter({'c': 3, 'b': 2, 'a': 1})
Counter({'dogs': 7, 'cats': 4})
'''
# look like dictionaries 

c = Counter(cats=4, dogs=7)
print(c['cats']) # -> 4
print(c['birds']) # -> 0
# In case the key does not exist we don't get an error, like in DICTIONARIES! 
# EXTREMELY USEFUL!!!


print(list(c.elements())) 
# ['cats', 'cats', 'cats', 'cats', 'dogs', 'dogs', 'dogs', 'dogs', 'dogs', 'dogs', 'dogs']
print(c.most_common(1)) 
# here you enter how many Elements want take into consideration

dog = ['dogs'] * 4 # You need to use lists, or single element list or dictionary
c.subtract(dog)
print(c)

cat = ['cats'] * 8
c.update(cat)
print(c)

#c.clear()
#print(c)


d = Counter([1,2,4,5,6,7,8])
print(c+d)
print(c-d)

print(c & d) # intersection el
print(c | d) # max element
