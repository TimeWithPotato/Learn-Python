def calc_sum (n):
    if(n == 0 or n == 1):
        return 1
    return n + calc_sum(n-1)
print(calc_sum(5))