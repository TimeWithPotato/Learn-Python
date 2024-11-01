str1 = 'Apna College'
str2 = "Apna College in double coated"
str3 = """Apna College in triple coated"""


"""
Python ignore string that are not assigned to a vairable, so we can use this as a comment.
"""
# Difference Between single coated, double coated, triple coated
"""
To use apostrophe we need to use double coated .
"""
str4 = "Apna college's lecture "

"""
To break a line without using escape sequence character, since single coated and double coated doesn't allow break line
"""
str5 = """Apna college.
This line will print in a new line.
"""

print(str1," ",str2," ",str3," ",str4," ",str5)

#String concatenation and length of a string
str6 = str1 + " " + str2
len1 = len(str6)
len2 = len(str1+str2)
print(str6," ",len1," ",len2)

#like other language,in python string is also immutable.
# this is valid.
print(str6[5])