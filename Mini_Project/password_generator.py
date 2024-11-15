import random 
import string

# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.digits)
# print(string.punctuation)

pass_len = 12

char_val = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

# print(char_val)

# general procedure
# password = ""
# for i in range(pass_len):
#     password += random.choice(char_val)

# string comprehension procedure
# password = [random.choice(char_val) for i in range(pass_len)] # this line will generate a list , now to convert into string we will use join with an empty string


password = "".join([random.choice(char_val) for i in range(pass_len)])
print(password)