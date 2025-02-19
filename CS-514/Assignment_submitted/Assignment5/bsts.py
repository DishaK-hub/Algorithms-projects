dict1 = {0: 1}

def bsts(n):
    tmp1 = 0
    if n not in dict1:
        for i in range(1, n+1):
            tmp1 += (bsts(i-1) * bsts(n-i))
            dict1[n] = tmp1
    return dict1[n]


print(bsts(2))
print(bsts(3))
print(bsts(5))