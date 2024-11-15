"""
                        -----------------
                        |               |   Base Class
                        |    Parent     |
                        |    Class      |
                        -----------------
                               |
                               |
                               ↓
                        -----------------
                        |               |  Derived Class
                        |    Child      |
                        |    Class      |
                        -----------------

"""
class Car:
    color = "Black"

    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Stopped car")

class ToyotaCar(Car):
    
    def __init__(self,model):
        self.model = model

car1 = ToyotaCar("Fortune")

print(car1.model," ",car1.color)
car1.start()
car1.stop()