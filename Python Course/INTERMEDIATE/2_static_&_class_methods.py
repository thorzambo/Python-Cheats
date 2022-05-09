# Static and Class Methods

class person(object):
      population = 50
      def __init__(self, name, age):
            self.name = name
            self.age = age
            
      # class method - needs necorator
      @classmethod # -> WE DENOTE CLASS METHOD TYPE BY ADDING DECORATOR. CLS stands for class
      # Class method can  and report any parameter stored and made publically availabe into the class -> In this case population only
      def getPopulation(cls):
            return cls.population
            
      # static method
      @staticmethod # -> Similar to  class method. Basically you don't need any class or self parameter.
      # These are you used when you don;t need Class or Self parameter
      # Static method does not have access to population parameter
      def isAdult(age):
            return age >= 18
      
      def display(self):
            print(self.name, 'is', self.age, 'years old')

#newPerson = person('leo', 24)

# CLASS METHOD MEANS YOU CAN CALL IT ON ANY INSTANCE OF THIS CLASS. You Don't need to create an Object to use that method.
print(person.getPopulation())
# everything passed to the class method is just the class. No variables or parameters

print(person.isAdult(19))

