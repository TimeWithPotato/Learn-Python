import random

randNUm = random.randint(0,100)

first = True
while True:
    if first:
        userChoice = int(input("Enter your choice : "))
        first = False
    else:
        userChoice = int(input("Enter your choice or -1 to Quit : "))
        if userChoice == -1 :
            break
    
    if(userChoice == randNUm):
        print("Match")
        break
    elif(userChoice < randNUm):
        print("Your choice is small, try again.")
    else:
        print("Your choice is big, try again")