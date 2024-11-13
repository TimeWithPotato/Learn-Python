#1
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def average(self):
        sum =0
        count = 0
        for val in self.marks:
            sum += val
            count += 1
        return sum/count

s1 = Student("Jihan",[90,95,100])

print(s1.name," ",s1.average())