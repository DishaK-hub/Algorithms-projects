def CartesianProduct( a:list, b:list):
    c = list((i,j) for i in a for j in b)
    return c

def nbest(a:list, b:list, k):
    c = CartesianProduct(a,b)
    c = sorted(c, key =sum)
    print(c)
    for i in range(len(c)):
        for j in range(len(c)-i-1):
            if (c[j][0]+c[j][1]) == (c[j+1][0]+c[j+1][1]):
                if(c[j][1] == c[j+1][1]):
                    c[j], c[j+1] = c[j+1], c[j]
    sum_c = [a_tuple[0] + a_tuple[1] for a_tuple in c]
    zipped_c = zip(c, sum_c)
    
    for tuplea in zipped_c:
        print(tuplea)

    return zipped_c

m = [4,1,5,3]
n = [2,6,3,4]

print(nbest(m,n,3))