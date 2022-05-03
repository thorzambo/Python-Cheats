class Person:
      number_of_people = 0 # attribute
      GRAVITY = -9.8
      
      def __init__(self, name):
            self.name = name
            Person.number_of_people += 1
            Person.add_person() # expls for method
      
      @classmethod
      def number_of_people_(cls):     # Class Method, not SELF but CLS
            return cls.number_of_people

      @classmethod
      def add_person(cls): #same as Person.number_of_people += 1 
            cls.number_of_people += 1
            
            
 # Examples for attributes 
p1 = Person("tim")
p2 = Person("jill")
print(p1.number_of_people)
Person.number_of_people += 9
print(p2.number_of_people)

# Examples for CLass Methods
print(Person.number_of_people_())
