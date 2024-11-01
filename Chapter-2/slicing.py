str = "Hello I am learning Python from Youtube"
print(str[0:7]) 

print(str[:len(str)]) # valid,because interpreter will assume the first index as 0

print(str[2:]) #valid, because interpreter will assume the second index as length of the string

#Negative indexing

print(str[-1:]) # it will just return the last character
print(str[-5:-1])