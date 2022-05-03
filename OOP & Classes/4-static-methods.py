# Static Methods are made for referencing Functions when they are a lot and reusable in the program like a Module
# like import math - math - pandas etcetc.
# important for Organizational Stuff

class Math:
      
      @staticmethod
      def  add5(x): #not even needed to add self or cls, its just like a function
            return x +5
      
      @staticmethod
      def  add10(x): #not even needed to add self or cls, its just like a function
            return x +10
      
      @staticmethod
      def pr():
            print("shesh")
            return "Shesh"

print(Math.add5(5))
print(Math.add10(5))
Math.pr()
print('------')
print(Math.pr())

