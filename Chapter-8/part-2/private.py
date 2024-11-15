#private use __ and protected _ , however these are differ from java and c++ private and protected

class Bank:
    def __init__(self,acc_name,acc_pass):
        self.acc_name = acc_name
        self. __acc_pass = acc_pass
    
    def __check(self,acc_name,acc_pass):
        if(self.acc_name == acc_name and self.__acc_pass == acc_pass):
            print("Login Succeed")
        else:
            print("Login Failed")
    
    def call_check(self,acc_name,acc_pass):
       self. __check(acc_name,acc_pass)


acc1 = Bank("Mehta","Mehta#124")
# print(acc1._Bank__acc_pass) by this mangling we can access the private 

acc1.call_check("Mehta","Mehta@1234") # login failed
acc1.call_check("Mehta","Mehta#124")  # login succeed