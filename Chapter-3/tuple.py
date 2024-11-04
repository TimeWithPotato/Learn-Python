# tupple is immutable just like string, tupple can store several type of data just like list

tup = ()
print(tup)
print(type(tup))

# tup = (1), python will treat it as an integer or other primitive data type value, so use comma tup = (1,)
tup_int = (1)
print(type(tup_int)," ",tup_int)
tup_1 = (1,)
print(type(tup_1)," ",tup_1)

tup_2 = (1,2,"John",4,5,2,1,) # here the comma after the last value is optional
print(tup_2)

# tupple slicing
tup_3 = tup_2[0:3]
print(tup_3)

# print the idx of the first occurence
print(tup_2.index(4))

# count the frequency of the occurences
print(tup_2.count(2))




