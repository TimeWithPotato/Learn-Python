class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    # def addNumber(self,num2):
    #     newReal = self.real + num2.real
    #     newImg = self.img + num2.img
    #     return Complex(newReal,newImg)

    # use dunder functions
    def __add__(self,num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg)
    
    def __sub__(self,num1):
        newReal = self.real - num1.real
        newImg = self.img - num1.img
        return Complex(newReal,newImg)

    def showNumber(self):
        print(self.real,"i","+",self.img,"j")



num1 = Complex(5,6)
num2 = Complex(10,20)
# num3 = num1.addNumber(num2)
# num3.showNumber()
num3 = num1 + num2
num3.showNumber()

num4 = num2 - num1
num4.showNumber()
