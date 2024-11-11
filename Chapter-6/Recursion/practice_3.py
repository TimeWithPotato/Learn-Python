def print_list(list,idx=0):
    if(idx == -1):
        return
    print_list(list,idx-1)
    print(list[idx])

list = (1,2,3,4,5,10,8,5)
print_list(list,len(list)-1)