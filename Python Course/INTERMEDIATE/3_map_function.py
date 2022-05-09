# Map Function
# Allows us to apply a function to a list and create a new list with these new values

# Example 1:
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def func(x):
      return x**x

# I watn to apply fucntion x into any vallue into the list li and get it store into a new list

# could be solvable by:
newList = []
for x in li:
      newList.append(func(x))

print(newList)

# this can be translated and 1 lined pythonically by using map -> basically a shortcut

print(list(map(func, li)))
# the map fucntuon take sa function which is func and a list li
# this will be basically take all elements fo the list and apply the function



# Example 2:
# List Comprehension

print([func(x) for x in li])

# Upgrade:
print([func(x) for x in li if x % 2 == 0])
