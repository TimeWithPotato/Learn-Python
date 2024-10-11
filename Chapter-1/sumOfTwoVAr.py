import math # for process - 3

var1 = float(input("First Number: "))
var2 = float(input("Second Number: "))

# process - 1
"""tempSum = str(var1 + var2) # to check if the sum contains any value after the redix point
fracPart = int(tempSum.split(".")[1]) # get the value after redix point

sum = (var1+var2, int(var1+var2)) [fracPart == 0]
print(sum)"""

# process - 2
"""fracPart = (var1+var2) % 1
sum = (var1+var2,int(var1+var2))[fracPart == 0]
print(sum)"""

# process - 3
sum = var1 + var2
fracPart,intPart = math.modf(sum)
sum = (sum,int(sum)) [fracPart == 0]
print(sum)
