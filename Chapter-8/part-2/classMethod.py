# @classmethod is a decorator in python that is used to change the class status or class attribute

class Student:
    name = "Anonymous"

    # def __init__(self,name):
    #     self.name = name here the self will create an instance of for the obj self, this name and the class attribute's name is differeent

    #1. 
    def changeClassAttr1(self,name):
       Student.name = name
    
    #2.
    def changeClassAttr2(self,name):
        self.__class__.name = name

    #3.
    @classmethod
    def changeClassAttr3(cls,name):
        cls.name = name  

s1 = Student()
s1.changeClassAttr1("Mahbub")
print(s1.name)
print(Student.name)

#2.
s1.changeClassAttr2("Shakil")
print(s1.name)
print(Student.name)

#3.
s1.changeClassAttr3("Akil")
print(s1.name)
print(Student.name)