# parent class
class Person:

    def __init__(self, name, surname, age, address):
        self.name = name
        self.surname = surname
        self.age = age
        self.address = address


    def personal_info(self):
         return f"""
            Name = {self.name}
            Surname = {self.surname}
            Age = {self.age}
            Address = {self.address}"""
 
    def __add__(self, other):
          # Use Dunder
          return self.name + ' ' + other.surname
    
    def __str__(self):
          return f"The person {self.name} {self.surname}"
    
    def __repr__(self):
          return f"Person ('{self.name}', '{self.surname}', '{self.age}', '{self.address}'"


# special methods: Dunder double underscore = '__'

alphabet = {1:'a',2:'b',3:'c',4:'d'}
print(type(alphabet)) #dict

d = alphabet[4]
print(d)

d = alphabet.__getitem__(4)
print(d)

# Built-in Types Python

student1 = Person("Thor", "Zamba", 4, "4 fjfjdj")
student2 = Person("Thur", "rega", 5, "848fh HHH")

#print(student1 + student2)

print(student1)
print(repr(student1))

print(Person.__str__(student1))
print(Person.__repr__(student1))

print(student1.__str__())
print(student1.__repr__)
