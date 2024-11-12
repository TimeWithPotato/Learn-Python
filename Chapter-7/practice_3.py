#3

with open("/Python/Chapter-7/practice.txt","r") as f:
    data = f.read()
    if(data.find("learning")):
        print("Found")
    else:
        print("Not Found")
    