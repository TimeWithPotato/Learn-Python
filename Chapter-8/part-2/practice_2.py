#2.

class Employee:
    
    def __init__(self,role,dept,salary):
        self.role = role
        self.dept = dept
        self.salary = salary
    
    def showDetails(self):
        print("Role: ",self.role," ","Dept: ",self.dept," ","Salary: ",self.salary)

class Engineer(Employee):
    def __init__(self,name,age,role,dept,salary):
        super().__init__(role,dept,salary)
        self.name = name
        self.age = age

name = input("Enter the name: ")
age = int(input("Enter the age: "))
role = input("Enter the role: ")
dept = input("Enter the department: ")
salary = float(input("Enter the salary: "))

p = Engineer(name,age,role,dept,salary)
p.showDetails()