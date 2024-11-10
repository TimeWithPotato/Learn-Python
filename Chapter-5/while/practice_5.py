list = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

x = int(input("Enter the number you want to find: "))

idx = 0

while idx < len(list):
    if(list[idx] == x):
        print("Found")
    idx += 1