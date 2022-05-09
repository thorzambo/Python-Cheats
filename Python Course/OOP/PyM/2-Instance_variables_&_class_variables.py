# classi raggruppano variabili e funzioni per poterle riutilizzare
# Studenti e Classi scuola
# Classe: Fabbrica di ogetti ; Oggetto da modello generico -> istanza

class Student:
      # variabile di classe:
      course_time = 36
      student_enum = 0
      
      # init inizializza e attiva le varie proprieta' di ciascun "self" -> oggetto o istanza
      # gli attributi prendono il nome di instance variables
      def __init__(self, name, surname, course): 
            self.name = name
            self.surname = surname
            self.course = course
            Student.student_enum += 1
            
      #aggiungiamo un metodo che permette di visualizzare la scheda di ogni studente
      def info(self):
            return f"\nStudent Info: \n Nome: {self.name}\n Surname: {self.surname}\n Course: {self.course}\n Course Time: {self.course_time}"            
      
s1 = Student("Leo", "zambo", "eco")
s2 = Student("lisa", "regaz", "scienze della salute")

#printare classi,, 2 allocazioni di memoria diverse
#print(s1)
#print(s2)

print(s1.info())
print(s2.info())

s1.course_time += 3 # add course_time

print(s1.__dict__)
print(s2.__dict__)

#print(Student.info(s1))

print(Student.student_enum)
