class human:
    def __init__(self, name = "No name", surname = "No surname" ):
        self.name = name
        self.surname = surname
class Auto:
    def __init__(self, model):
        self.model = model
        self.pasengers = []

    def add_pasengers(self, human):
        self.pasengers.append(human)