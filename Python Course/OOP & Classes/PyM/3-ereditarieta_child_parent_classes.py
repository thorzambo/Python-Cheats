# parent class
class Person:
      
      def __init__(self, name, surname, age, address):
            self.name = name
            self.surname = surname
            self.age = age
            self.address = address
            
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

      def __init__(self, name, surname, age, address, fecher = None):
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
      


s1 = Student("Leo", "Zamba", 24, "Home Leo", "Info")
t1 = Teacher("Lisa", "Rega", 21, "Home Princy", ["sec", "info"])

s1.change_course("Psico")
t1.new_fech("Psico")


print(s1.personal_info())
print(t1.personal_info())
