class Student:

     def __init__(self, name, surname, age, money):
         self.name = name
         self.surname = surname
         self.age = age
         self.money = money

a1 = Student("Oleg", "Kurka", 27, money= 21)
print(a1.name, a1.surname, a1.age, "$", a1.money )
    # def info(self):
    #     name = self.name
    #     surname = self.surname
    #     age = self.age
    #     print(f"Student: {name} {surname}. Age: {age}")

# a1 = Student("Olga", "Hamota", 24)
# print(a1.name, a1.surname)
# a2 = Student("Oleg", "Rudnik", 26)
# print(a2.name, a2.surname, a2.age)


# s1 = Student("Vlad", "Vladko", 5)
# s1.info()
# s2 = Student("Lobzik", "Lobzikovich", 27)
# s2.info()