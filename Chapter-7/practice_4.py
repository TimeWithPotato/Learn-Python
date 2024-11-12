def searchLine(target="learning"):
    countLine = 0
    with open("/Python/Chapter-7/practice.txt", "r") as f:
        while True:
            data = f.readline()
            if not data:
                return -1
            if target in data:
                return countLine
            countLine += 1

countLine = searchLine("learning")
print(countLine)
