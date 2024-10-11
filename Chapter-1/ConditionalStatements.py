# problem - 1
"""signal = input("Give signal light: ")

if(signal == "Red"):
    print("Stop the Car")
elif(signal == "Yellow"):
    print("Look around")
else:
    print("Go")"""

# problem - 2
"""age = int(input("Enter your age: "))
gender = input("Enter your gender: ")

if((age == 20 or age == 30) and gender == "M"):
    print("Fee is 500")
elif((age == 30 or age == 40) and gender == "M"):
    print("Fee is 1000")
elif(age <= 40 and age >= 20 and gender == "F"):
    print("Fee is 250")
else:
    if(age >= 40):
        print("Age limit exceeds")
    else:
        print("Age is below limit")"""

# single line if / ternary operator
# <var> = <val1> if <condition> else <val2>

"""food = input("Food : ")
eat = "Yes" if food == "Cake" else "No"
print(eat)"""

"""food = input("Food: ")
eat = "Yes" if food == "Cake" or food == "Coke" else "No"
print(eat)"""

"""food = input("Food: ")
print("Sweet") if food == "Cake" or food == "Pastry" else print("Not Sweet")"""

# Clever if / ternary operator
# <var> = (false_val,true_val) [<condition>]

age = int(input("Age: "))
period = ("Adult","Man") [age>20]
print(period)