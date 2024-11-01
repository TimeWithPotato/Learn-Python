marks = int(input("Enter your marks: "))

if(marks >= 90):
    print("Your grade is A")
elif(marks < 90 and marks >= 80):
    print("Your grade is B")
elif(marks < 80 and marks >= 70):
    print("Your grade is C")
else:
    print("Your grade is D")