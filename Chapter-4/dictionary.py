
# dictionary is a combination of key-value pair, which is mutable and unordered.
dict = {} # empty dictionary
info = {
    "name": "Arif Mainuddin",
    "age": 28,
    "address": {
        "district": "Chittagong",
        "divison": "Chittagong",
        "Police Station" : "Bakalia"
    },
    44: "Zip-Code" # key can be string, integer, float or any valid type
}

# we can access the value of dictionary by their key name like array / list

print(info["name"])
print(info.keys())
print(info.values())
print(info.get("name")) # difference between square bracket and this is, get() method return None if the key has not found while [] return error.

print(info.items()) # it returns an iterable object

new_info = {"name": "Najifa Tabassum", "profession": "student"}
info.update(new_info)

print(info)