dict1 = {0: 1, 1: 2}

def num_no(n):
    if n not in dict1:
        dict1[n] = num_no(n - 1) + num_no(n - 2)
    return dict1[n]

def num_yes(n):
    tmp1 = num_no(n)
    return pow(2, n) - tmp1


print(num_no(3))
print(num_yes(3))