# #1.
# li = []
# movie = input("Enter your 1st fav movie name: ")
# li.append(movie)

# movie = input("Enter your 2nd fav movie: ")
# li.append(movie)

# movie = input("Enter your 3rd fav movie: ")
# li.append(movie)
# print(li)

#2.
li_1 = [1,"abc","abc",1]
li_2 = li_1.copy()
# li_2.sort(reverse=True) when a list contain several type then this sort(reverse=True) method will not work, use reverse() instead

li_2.reverse()
if(li_1 == li_2):
    print("This list is Palindrome")
else:
    print("This list is not Palindrome")
