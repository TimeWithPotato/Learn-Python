# use other mode like t,b,+

f = open("/Python/Chapter-7/read/demo.txt","rt") # here we do not write t explicitly, cause t is implicit
data = f.read()
print(data)
f.close()

f = open("/Python/Chapter-7/read/demo.txt","a+") # if give the mode w+, then python will first truncate the existing data and then will open for read or write, as write mode follow overrite
data = f.read() 
print(data)
f.close()
