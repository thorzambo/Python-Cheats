# for allows to iterate an x amount of time
# -----------------------------------------

for i in range(10):
      print(i)
      
print('-'*15)

# -------------------
# range creates a collection of numbers based on input we give it. THe input of range is:
# (start, stop, step)
# order will be:
# if we give 1 input is STOP
# if 2 inputd is START, STOP
# ex: 3, 10, 5 will print 3 and 8, cause jumps by 5
# -------------------

print(range(10)) # -> 0 to 10 excluded

print('-'*15)

# -------------------

print(range(-10, 10, -1))

print('-'*15)

# -------------------

for i in range(3, 10, 5):
      print(i)

print('-'*15)

# -------------------

for i in (-10, -1, -2):
      print(i)
      
print('-'*15)

# -------------------

for i in (-10, -10, -1):
      print(i)

print('-'*15)

# -------------------

for i in [2,14,5,6]:
      print(i)

# if index is important:
for i in range(len([2,14,5,6])):
      print(i)
      
print('-'*15)

# -------------------

x = [2,14,5,6]
for i in range(len(x)):
      print(x[i])
      
print('-'*15)

# -------------------

for i, element in enumerate(x):  #gets indexes and values 
      print(i, element)

