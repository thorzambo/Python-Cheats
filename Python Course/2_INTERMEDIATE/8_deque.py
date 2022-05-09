import collections
from collections import deque # -> pronounce deck , rather than using a list you pref use deque

d = deque("hellllooo")
b = deque(['ciao', 'ciao', 'duck'])
c = deque([3, 5, 0])
e = deque({'d':4, 'f':5, '0':'ciao'})
print(d)
print(b)
print(c)
print(e)

# we have:
d.append(4)
d.append('5')
d.append('0')
d.pop()
d.popleft()

d.extend('fjdje')
d.extend([1,4,5])
d.extendleft('hhhf')
#d.clear()

d = deque('ciao')
d.rotate(-1)
print(d)

d = deque("hello", maxlen=5)
d.append('0')
print(d)
d.append([1,2,4])
print(d)


