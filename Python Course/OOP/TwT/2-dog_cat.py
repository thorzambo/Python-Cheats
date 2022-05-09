''' class Cat:
      def __init__(self, name, age):
            self.name = name
            self.age = age
      
      def speak(self):
            print("Meow")
      

class Dog:
      def __init__(self, name, age):
            self.name = name
            self.age = age
      
      def speak(self):
            print("Bark") '''
            
      
####################


class Pet:
      def __init__(self, name, age):      
            self.name = name
            self.age = age
      
      def show(self):
            print(f"I am {self.name}, and I am {self.age} years old")
            
      def speak(self):
            print("No idea what i say")

class Cat(Pet):
      def __init__(self, name, age, color):
            #self.name = name
            #self.age = age
            super().__init__ (name,age)   # self not needed
            self.color = color
            
      def speak(self):
            print("Meow")
      
      def show(self):
            print(f"I am {self.name}, and I am {self.age} years old, and my color is {self.color}")
      
      

class Dog(Pet):     
      def speak(self):
            print("Bark")
      
class Fish(Pet):
      pass

pet = Pet("Tim", 10)
pet.speak()
doggo = Cat("Thor", 4, "Blue")
doggo.show()
doggo.speak()
fisho = Fish("Bubbles", 2)
fisho.speak()
