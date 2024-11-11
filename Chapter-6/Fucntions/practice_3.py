def fact(n):
    fact = 1
    for idx in range(1,n+1):
        fact *= idx
    return fact
print(fact(4))