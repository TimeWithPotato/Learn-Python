# methods are functions that are defined inside a class

# object attributes are declared inside the constructor and class attributes are decalred outside of the constructor


class Car:
    car_type = "SUV" # class attribute
    # model = "Marceedes"
    def __init__(self,model):
        self.model = model  # object attributes preference >>>>> class attributes

    def enjoy_message(self):
        return "Enjoy your " + self.model

car1 = Car("Rolls Royce")
car2 = Car("Range Rover")

print (Car.car_type) # we can access the class object using class name

print(car1.model," ",car1.car_type," ",car1.enjoy_message())
print(car2.model," ",car2.car_type," ",car2.enjoy_message())