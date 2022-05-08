# Python is the only lenguage which has comprehensions
# one line initialization of list, dict touples etcetc

# famous Pythonic way to write stuff

x = [x for x in range(10)]
print(x)
# we basically decide a for loop inside a list

x = [x+5 for x in range(10)]
print(x)

x = [0 for x in range(10)]
print(x)

# --------------
# advanced:

# list of list
x = [[0 for x in range(10)] for x in range(5)]
print(x)

x = [i for i in range(100) if i % 5 == 0]
print(x)

# sets
x = {i for i in range(100) if i % 5 == 0}
print(x)


# dictionary
x = {i:0 for i in range(100) if i % 5 == 0}
print(x)

# tuples
# generator object
x = (i for i in range(100) if i % 5 == 0)
print(x)

#tuple
x = tuple(i for i in range(100) if i % 5 == 0)
print(x)
