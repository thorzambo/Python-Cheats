def func():
      print('Run')
      def function_inside():
            print('Run Inside')
            
            
func()


def fun(x, y):
      return x / y



fun(3, 5)
print(fun(3, 5))



# if we want to return 2 values they will get packed into touples. Lwets see how to unpack them:
def test(x, y):
      print('Returning...', x / y, x + y, x % y)
      return x / y, x + y, x % y

test(3, 7)
# unpacking them... -> set the funct to multiple variables 

result1, result2, result3 = test(3,7) # more pythionic
print(result1)
print(result2)
print(result3)
 
# or, worse
result = test(3, 7)
print(result[0])
print(result[1])
print(result[2])


# if unsure to have a third var:
def test(x, y, z=None):
      print('Returning...', x / y, x + y, x % y, z)
      return x / y, x + y, x % y

shesh = test(3, 6)
print(shesh)
# Returning... 0.5 9 3 None

shesh_z = test(3, 5, 4)
print(shesh_z)
# Returning... 0.5 9 3 4
