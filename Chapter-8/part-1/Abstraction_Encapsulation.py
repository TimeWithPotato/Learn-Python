# Abstraction : Hiding the implementation details of a class and showing the essential features to the user (Differ from Java)

#Encapsulation : wrapping data and functions into a single unit 

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    
    def start(self):
        self.acc = True
        self.brk = True
        self.clutch = True
        
        if self.acc and self.brk and self.clutch == True:
            print("Starting Car")
car1 = Car()
car1.start()
