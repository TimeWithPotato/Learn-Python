#5
def count_prime(str):
    data = str.split(",")
    count = 0
    for val in data:
        if(int(val) % 2 == 0):
            count += 1
    return count

with open ("/Python/Chapter-7/practice_2.txt","w") as f:
    data = "10,22,11,14,12,16,100,2,3,5,7,28,30"
    f.write(data)
n = count_prime(data)
print(n)