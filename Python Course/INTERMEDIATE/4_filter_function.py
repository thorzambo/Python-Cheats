# Filter Functon

from pydoc import ispackage


def add7(x):
      return x + 7

def isOdd(x):
      return x %2 != 0

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

b = list(filter(isOdd, a))

c = list(map(add7, b))
c1 = list(map(add7, filter(isOdd, a)))
# Filter Functon takes the same arguments that the map function does. Takes a function and an iterable list (also a string btw)
# Filter works the way if True is reached, the value will be added into the new list. Its actually a filter.

print(a, b) # b has even only

print(c)

