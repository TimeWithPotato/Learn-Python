n = int(input("Enter n: "))
fact = 1
for idx in range(1,n+1):
    fact *= idx
print(fact)