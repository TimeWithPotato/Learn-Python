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
                        |    Class  A   |
                        -----------------
                               |
                               |
                               ↓ Derived Class of Child Class A
                        -----------------
                        |               |  
                        |    Child      |
                        |    Class      |
                        -----------------
                               .
                               .
                               .

"""
class Car:

    color = "Black"
    @staticmethod
    def start():
        print("Car Started")
    
    def stop(self):  #if the method is not static, then we have to give self param
        print("Car Stopped")

class RangeRover(Car):
    
    def __init__(self):
        self.model = "Defender"

class FactoryArea(RangeRover):
    def __init__(self, loc):
        super().__init__()
        self.loc = loc

car = FactoryArea("UK")
print(car.model," ",car.color," ",car.loc)
car.start()
car.stop()