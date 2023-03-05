class Student:

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


    def info(self):
        name = self.name
        surname = self.surname
        age = self.age
        print(f"Student: {name} {surname}. Age: {age}")

# a1 = Student("Olga", "Hamota", 24)
# print(a1.name, a1.surname)
# a2 = Student("Oleg", "Rudnik", 26)
# print(a2.name, a2.surname, a2.age)


