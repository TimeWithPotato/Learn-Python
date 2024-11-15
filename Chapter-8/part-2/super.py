class Car:

    color = "Black"
    @staticmethod
    def start():
        print("Car Started")
    
    @staticmethod
    def stop():  #if the method is not static, then we have to give self param
        print("Car Stopped")

    def car_definition(self):
        print("Car is a vehicle which has four wheels")

class RangeRover(Car):
    
    def __init__(self,model):
        self.model = model
        super().car_definition()

class FactoryArea(RangeRover):
    def __init__(self, loc,model):
        super().__init__(model)
        self.loc = loc

car = FactoryArea("UK","Defender")
print(car.model," ",car.color," ",car.loc)
car.start()
car.stop()