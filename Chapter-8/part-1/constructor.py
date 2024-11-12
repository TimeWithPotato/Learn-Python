class Car:

    # default constructor
    def __init__(self):
        pass
    
    # parameterized constructor
    def __init__(self,model):
        self.model = model

car1 = Car("BMW")
car2 = Car("Rolls Royce")
print(car1.model)
print(car2.model)