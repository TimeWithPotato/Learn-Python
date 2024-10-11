num_1 = 2
num_2 = 8
num_3 = num_1**num_2 # num_1 to the power of num_2
num_4 = num_1 // num_2 # integer divison operator
num_5 = num_1 / num_2 # normal divison operator
print(num_1 + num_2)
print(num_3)
print(num_4)
print(num_5)

# TypeCast 
num_6 = 2.5
num_7 = int(num_6)
print(num_7)

# Specify the base
num_8 = "10101"
num_9 = int(num_8, 2) # 21
num_10 = "A"
num_11 = int(num_10,16)
print(num_9)
print(num_11)

# Complex
num_12 = 5
num_13 = complex(5,6)
print(num_13)

# input

name = input("name: ")
print (name)

num_14 = float(input("First num: "))
num_15 = float(input("Second num: "))
tot_1 = num_14 + num_15
tot_2 = int(sum([num_14, num_15]))

print("without using sum(): ",tot_1," using sum(): ",tot_2)



