#files are used to store data on ssd or hdd
#python can make operations on file by read(r), write(w), append(a),text(t),binary(b),x,+
# + is used to perform duo operation, eg: r+, it can perform both read or write

f = open("/Python/Chapter-7/read/demo.txt","r") # here f is stream of characters
data = f.read()
print(data)
f.close()

f = open("/Python/Chapter-7/read/demo.txt","r")
data = f.read(5)
print(data)
