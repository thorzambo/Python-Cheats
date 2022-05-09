import jwt


def func(x):
      def func2():
            print(x)
            
      return func2

func(3)()

x = func(3)
x()

# ------------------------

# unpack operator
x = [1,24,345564,456433]
print(*x)
print(x)
# unpack operator separates elements in colleciton into individual = * unpacker

# ------------------------

def func(x, y):
      print(x, y)

# ------------------------

# FOR LISTS or TUPLES -> Involves 1 * 
pairs = [(1, 2), (3, 4)]

# non pythonic unpacker
for pair in pairs:
      #ex1 non pythonic
      print(pair[0], pair[1])
      #ex2 non pythonic
      func(pair[0], pair[1])
      
print('Pythonic way:')
# Pythonic unpacker
for pair in pairs:
      print(*pair)
      func(*pair)
      
      
# FOR DICTIONARIES ->Involves 2 **
print('For Dictionary:')

for pair in pairs:
      func(**{'x': pair[0], 'y':pair[1]})


# ------------------------
# IN CASE YOU DON'T KNOW HOW MANY ARGUMENTS
print('IN CASE YOU DON\'T KNOW HOW MANY ARGUMENTS:')

def func(*args, **kwargs): # -> args, arguments | kwargs, keyword arguments
      print(args, kwargs)
      print(*args)
      print(*kwargs)
      print(args)
      print(kwargs) 
      # print(**kwargs) wont work because they are not valid arguments for the print statement. 
      
func(1,2,3,4,5,6,7, one = 0, two = 9, three = 75)

