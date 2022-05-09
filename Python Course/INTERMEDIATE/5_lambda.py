# Lambda is an Anonymous Function

def func(x):
      return x + 5
      
print(func(2))


y = lambda x: x + 5

print(y(2))


# ----------------
# Function in a function
def func2(x):
      func3 = lambda x: x + 5
      return func3(x) + 85

print(func2(2))



# ----------------
# You can do anything is you do within a normal function but returning multiple expressions
func4 = lambda x, y: x + y
print(func4(3, 4))



a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newList = list(map(lambda x: x, a))

print(newList)
