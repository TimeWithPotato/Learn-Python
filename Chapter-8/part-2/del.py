# student
class Student:
    def __init__(self,name):
        self.name = name

s1 = Student("Harsh Mehta")
print(s1.name)

del s1

# print(s1) this will give an error, cause the object s1 has deleted