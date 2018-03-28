class Car():
    def __init__(self,name):
        self.name=name
    def fullname(self):
        print(self.name)
class Electrocar(Car):
    def __init__(self,name):
        super().__init__(name)
    def fullname(self):
        print("Tesla model S")
mytesla=Electrocar("Tesla Model 3")
mytesla.fullname()