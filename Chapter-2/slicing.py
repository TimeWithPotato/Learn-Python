str = "Hello I am learning Python from Youtube"
print(str[0:7]) 

print(str[:len(str)]) # valid,because interpreter will assume the first index as 0

print(str[2:]) #valid, because interpreter will assume the second index as length of the string

#Negative indexing
# structure of slicing:-  sequence[start:stop:step], if start omitted start from 0, if stop omitted goes to the end, if step omitted then defaults 1
print(str[-1:]) # it will just return the last character
print(str[-5:-1])