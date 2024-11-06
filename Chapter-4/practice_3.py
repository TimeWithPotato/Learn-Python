#3
marks = {}

x = int(input("Enter physics marks: "))
marks.update({"physics" : x})

x = int(input("Enter chemistry marks: "))
marks.update({"chemistry": x})

x = int(input("Enter math marks: "))
marks.update({"math":x})

print(marks)
