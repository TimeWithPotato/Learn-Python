marks = [24,55,66,77]
print(type(marks))

# in python, we can store several type of data into a list
idAndName = [1001,"Arif",1002,"Salim",1005,"Rakib"]
print(idAndName)
print(idAndName[0]," ",idAndName[1])

# list slicing
slicedList = idAndName[0:4]
print(slicedList)

# list methods
list = [2,5,3,4,6]
list.sort()
print(list)
list.sort(reverse=True) #when a list contain several type then this sort(reverse=True) method will not work, use reverse() instead
print(list)
# list.reverse()
# print(list)(

# append value at the end
list.append(5)
list.append(5)
list.append(2)

print("After appending: "," ",list)
# print the idx of the first occurence
print(list.index(5))
# remove the value of the firsr occurence
list.remove(2)
# delere all duplicate
c = list.count(5)
for i in range(c):
    list.remove(5)
print(list)

list[0] = 1
print(list)

list.insert(5,5)
print(list)

# delete element at a specific idx
x = list.pop(4)
print(list,"\n",x)
