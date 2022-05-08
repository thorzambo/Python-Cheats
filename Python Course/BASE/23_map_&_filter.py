# MAP
x = [1,2,3,4,5,6,7,8,9,45839,59393,593,599,445839]

mp = map(lambda i: i * 2, x)
print(list(mp))

mp = map(lambda i: i + 2, x)
print(list(mp))


# ---------------------------------

# FILTER -> returns True or False based on the value of the item
x = [1,2,3,4,5,6,7,8,9,45839,59393,593,599,445839]

mp = map(lambda i: i % 2 == 0, x)
print(list(mp))

# Filter will get only the even values

mp = filter(lambda i: i % 2 == 0, x)
print(list(mp))


# otherwise 
 
def func(i): # this one was defined by LAMBDA in the previous example
      return i % 2 == 0

mp = filter(func, x)
print(list(mp))

