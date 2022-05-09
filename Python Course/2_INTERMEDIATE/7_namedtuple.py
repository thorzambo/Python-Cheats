# namedTuple is a moethod always part of Collection Module - Class

from collections import namedtuple
# or
import collections  
nt = collections.namedtuple


# diff btween a namedtuple and a regular tuple:
# you can access things through an element and nicer to read and understand


Point = namedtuple('Point', 'x y z') # is going to automatically break x y z into 3 parameters
newP = Point(3, 4, 5)
print(newP)
print(newP.x, newP.y, newP.z)


Point = namedtuple('Point', ['x', 'y', 'z']) # can be used through LISTS
newP = Point(3, 4, 5)
print(newP)
print(newP.x, newP.y, newP.z)


Point = namedtuple('Point', {'x', 'y', 'z'}) # can be used through DICTIONARIES -> UNORDERED?
newP = Point(3, 4, 5)
print(newP)
print(newP.x, newP.y, newP.z)


Point = namedtuple('Point', {'x':6, 'y':4, 'z':2}) # can be used through DICTIONARIES
newP = Point(3, 4, 5)
print(newP)
print(newP.x, newP.y, newP.z)

print(newP[0])
print(newP._asdict())

print(newP._fields)

newP._replace(x=6) # Not working,, not change Tuple. Need to assign to a new Tuple...
print(newP)

newP = newP._replace(x = 6)
print(newP)

p2 = Point._make(['a', 'b', 'c'])
print(p2)
