#1.
import math
class Circle:
    def __init__(self,r):
        self.r = r
    
    def area(self):
        self.ar = round(math.pi * math.pow(self.r,2),3)

    def perimiter(self):
        self.peri = "{:.3f}".format(2 * math.pi * self.r)


c = Circle(int(input("Enter the radius: ")))
c.area()
c.perimiter()
print("Area is : ",c.ar," ","Perimiter is : ",c.peri)