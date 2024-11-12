# read line by line by using readline()
# readline() automatically append a \n
f = open("/Python/Chapter-7/read/demo.txt","r")
data = f.readline()
print(data)

data = f.readline()
print(data)

f.close()