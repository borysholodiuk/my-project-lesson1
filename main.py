class Student:

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

a1 = Student("Olga", "Hamota", 24)
print(a1.name, a1.surname)