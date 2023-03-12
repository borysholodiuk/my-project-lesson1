# class human:
#     def __init__(self, name = "No name"):
#         self.name = name
# class Auto:
#     def __init__(self, model):
#         self.model = model
#         self.pasengers = []
#
#     def add_pasengers(self, human):
#         self.pasengers.append(human)
#
#     def car_detalis(self):
#         if self.pasengers != []:
#             print(f"B машині {self.model} є такі пасажири:\n{self.pasengers}")
#             for pasengers in self.pasengers:
#                 print(pasengers.name)
#
#
# car = Auto("Audi")
# car.add_pasengers(human("Olga"))
# car.add_pasengers(human("Borys"))
# car.car_detalis()









# class human:
#     def __init__(self, name = "No name"):
#         self.name = name
# class Auto:
#     def __init__(self, model):
#         self.model = model
#         self.pasengers = []
#
#     def add_pasengers(self, human):
#         self.pasengers.append(human)
#
#     def car_detalis(self):
#         if self.pasengers != []:
#             print(f"B машині {self.model} є такі пасажири:\n{self.pasengers}")
#             for pasengers in self.pasengers:
#                 print(pasengers.name)
#
#
# car = Auto("BMV")
# car.add_pasengers(human("Bober"))
# car.add_pasengers(human("Capibara"))
# car.car_detalis()




# class human:
#      def __init__(self, name = "No name"):
#          self.name = name
# class Auto:
#      def __init__(self, model):
#          self.model = model
#          self.pasengers = []
#
#      def add_pasengers(self, human):
#          self.pasengers.append(human)
#
#      def car_detalis(self):
#          if self.pasengers != []:
#              print(f"B автобусі {self.model} є такі пасажири:\n{self.pasengers}")
#              for pasengers in self.pasengers:
#                  print(pasengers.name)
#
#
# car = Auto("Autosan")
# car.add_pasengers(human("Abob"))
# car.add_pasengers(human("tutu"))
# car.car_detalis()




class human:

    def __init__(self, name="No name", surname="No surname", age= "No age"):
        self.name = name
        self.surname = surname
        self.age = age

class student:
    def __init__(self, human, Stupendia, name1):
        self.human = human
        self.Stupendia = Stupendia
        self.name1 = name1

