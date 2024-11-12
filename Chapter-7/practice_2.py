# replace all the occurences of Java with Python

def repleceOccur(str):
    str = str.replace("Java","Python")
    with open("/Python/Chapter-7/practice.txt","w+") as f:
        f.write(str)

with open("/Python/Chapter-7/practice.txt","r") as f:
    data = f.read()

repleceOccur(data)