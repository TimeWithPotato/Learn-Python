idx = 1

while idx <= 20:
    if(idx % 2 == 0):
        idx += 1
        continue
    elif(idx  == 15):
        break
    else:
        print(idx)
    idx += 1