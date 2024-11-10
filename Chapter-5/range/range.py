list = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
seq = range(5)
# print(seq) this will print range (0,5)
# print(list) this will print the list [1,......,100]
for el in seq:
    print(el)

for el in list[::2]:  # (1st ':') start from 0th pos = 1, (2nd ':') go to the end = 100, ('2') increment idx by 2
    print(el)

