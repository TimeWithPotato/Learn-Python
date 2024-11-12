# benefit of using with is we do not explicitly close the file

with open("/Python/Chapter-7/read/demo.txt","r+") as f:
    data = f.read()
    print(data)
