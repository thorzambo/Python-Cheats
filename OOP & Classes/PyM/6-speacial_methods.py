# parent class
class Person:

    def __init__(self, name, surname, age, address):
        self.name = name
        self.surname = surname
        self.age = age
        self.address = address

    @classmethod  # alther methods, pass as parameter class and not instance
    def from_string(cls, person_string, *args): # args, se ci sono vari parametri da poter aggiungere
        name, surname, age, address = person_string.split(', ')
        return cls(name, surname, age, address,*args)
  
    @classmethod
    def occupazione(cls):
      #     if cls.__name__ == "Studente":
      #           return "Studente"
      #     else:
      #           return "Insegnate"
          return cls.__name__

    def personal_info(self):
        info = f"""
            Name = {self.name}
            Surname = {self.surname}
            Age = {self.age}
            Address = {self.address}"""

        return info


# special methods: Dunder double underscore = '__'

alphabet = {1:'a',2:'b',3:'c',4:'d'}
print(type(alphabet)) #dict

d = alphabet[4]
print(d)

d = alphabet.__getitem__(4)
print(d)
