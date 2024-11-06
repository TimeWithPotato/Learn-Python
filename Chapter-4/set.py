# set is a collection of unordered and unique items, which is mutable but the items of the set is immutable, that's why set cannot contain list and dictionaries, but can contain primitive data, tuple

nums = {1,2,3,4}
data = {(1,2,3), "John", 4,5,3 }

# how create a null set..
null_set = set()
# print(type(null_set))

data.add("Arif")
# print(data)
data.remove("John")
# print(data)
data.pop()
# print(data)

data.update("Abraham") # difference between update() and add() is, update() will add the el by character even if el = string
# print(data)
nums.clear()
print(nums) # it will give a null set

# set union and intersection

set1 = {1,2,3,4,5}
set2 = {2,1,3,5,6,7,8}
setUnion = set1.union(set2)
setIntersection = set1.intersection(set2)
print(" Union:        ",setUnion,"\n","Intersection: ",setIntersection)