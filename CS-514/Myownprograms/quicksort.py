def partition(a:list,l:int,h:int):
    pivot = a[l]
    i = l +1
    j = h

    while(i<j):
        while(a[i]<=pivot):
            i+=1
        while(a[j]>pivot):
            j-=1
        if(i<j):
            a[i],a[j] = a[j],a[i]
        
    a[j],a[a.index(pivot)] = a[a.index(pivot)] ,a[j]
    print(a)
    print(j)
    return j

def qsort(a:list, low, high):
    while(low<high):
        pi =partition(a,low,high)
        qsort(a,low, pi)
        qsort(a,pi+1,high) 
    return a

array1= [10,16,8,12,15,6,3,9,5]
lo = 0
hi = len(array1) - 1

print(qsort(array1,lo,hi))
