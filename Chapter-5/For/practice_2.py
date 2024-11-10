list = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)

x = int(input("Enter the number you want to search: "))

found = False

for idx,li in enumerate(list):
    if(x == li):
        found = True
        print("Target ",x," found at ",idx+1)
        break

if  not found:
    print("Target not match")
