# we can give default value to the parameter of the functions
# sequence of giving default value: 1. a = 1, b = 1 (correct) 2. a, b = 1 (correct) 3. a = 1, b (incorrect)
def calc_prod(a=1,b=1): # correct
    return a*b

prod = calc_prod(5)
print(prod)

def calc_div (a, b=1): # correct
    return a/b # it will return a float value

quotient = calc_div(10,5) # correct
print(quotient)

# def calc_subtraction (a=1, b) incorrect