''' 
How Python Code actually Runs and Why We write certain lines
Python is an Interpreted Language.
Compiler vs Interpreter.
Python is Compiled into ByteCode Before being Interpreted.
COMPILER: Take some high level code and trnalsates it into lower level
Python Compiler takes the code we write and tranlates into ByteCode Which is more harder to read, but easier for a machine.
Python Basically does it onfly
When is required to compile a code before runnig it, it means, its basically compiled before running and then actually executed.
So, its ran directly on the Machine OS.

In python you write your Hi Level code, when run button is clicked, its translates into ByteCode which will be read by the Interpreter.

So if you have an invalid syntax, translation can't happen

Thats why you have trubles with runnig python on Mobiles. You need an Interpreter which trnalsates the code.

 '''

class Dog:
      def __init__(self):
            self.bark()
# normally this code would throw an error, in python is not.
# the reason why this is not runtime error
# This is because its translated into ByteCode which is not identify any error in Syntax

# --------------------------------------------

''' Weird things you can do in Python only'''

def make_class(x):
      class Dog:
            def __init__(self, name):
                  self.name = name
                  
            def print_value(self):
                  print(x)

      return Dog


_class = make_class(10)
print(_class)

