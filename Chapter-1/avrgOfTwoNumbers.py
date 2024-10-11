num1 = float(input("First Number: "))
num2 = float(input("Second Number: "))

avrg = (num1+num2)/2 # process - 1
"""
 The first f indicates that it is an formated string and we have to put the placeholder inside the curly braces, and also to formate the decimal places value we have to put colon after the variable and a dot to denote the number of decimal places
"""
print(f"{avrg:.2f}") 