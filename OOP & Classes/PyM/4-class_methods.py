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

    def info_modifier(self):
        print("""Info Modifier:
                  1 - Name
                  2- Surname
                  3 - Age
                  4 - Address """)

        choice = input("What would you like to modify?")
        if choice == "1":
            self.name = input("New Name: ")
        if choice == "2":
            self.surname = input("New Surname: ")
        if choice == "3":
            self.age = input("New Age: ")
        if choice == "4":
            self.address = input("New Address: ")

# child classes:
class Student(Person):
    profilo = "Student"

    def __init__(self, name, surname, age, address, course):
        super().__init__(name, surname, age, address)
        self.course = course

    def personal_info(self):
        info = f"""
            Profile: {self.profilo}
            Course: {self.course}"""
        return super().personal_info() + info

    def change_course(self, _course):
        self.course = _course
        print("Update Course")


class Teacher(Person):
    profilo = "Teacher"

    def __init__(self, name, surname, age, address, fecher=None):
        super().__init__(name, surname, age, address)
        if fecher is None:
            self.fecher = []
        else:
            self.fecher = fecher

    def personal_info(self):
        info = f"""
            Profile: {self.profilo}
            Teacher Fecher: {self.fecher}"""
        return super().personal_info() + info

    def new_fech(self, _fecher):
        if _fecher not in self.fecher:
            self.fecher.append(_fecher)
            print("Fecher Updated")


thor = "Thor, Torello, 4, Casa Zamba"


p1 = Person.from_string(thor)
print(p1.personal_info())


t1 = Teacher.from_string(thor, ["cacca", "pipi", "pappa"])
s1 = Student.from_string(thor, "cacca")
print(t1.personal_info())
print(s1.personal_info())

print(t1.occupazione())
print(s1.occupazione())

