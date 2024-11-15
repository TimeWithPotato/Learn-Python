class Student:
    def __init__(self,phy,math,che):
        self.phy = phy
        self.math = math
        self.che = che
    
    @property  # property will convert the method name into the class attributes like phy,math,che
    def percentage(self):
        return str((self.phy + self.math + self.che) / 3) + "%"
    
s1 = Student(90,90,100)
print(s1.percentage)