import bisect
def find(a, x, k):
    list1=[]
    i = bisect.bisect(a, x)
    l = len(a)
    m = i - 1
    n = i 
    while(len(list1)<k):
        if(m < l):
            if(n < l):
                if((abs(a[m] - x)) <= (abs(a[n] - x))):
                    
                    list1.append(a[m])
                    m-=1
                else:
                    
                    list1.append(a[n])
                    n+=1
            else:
                
                list1.append(a[m])
                m-=1
        else:
            
            list1.append(a[n])       
            n+=1
    return sorted(list1)

#print(find([1,2,3,4,4,7], 5.2, 2))
#print(find([1,2,3,4,4,7], 6.5, 3))
#print(find([1,2,3,4,4,6,6], 5, 3))
#print(find([1,2,3,4,4,5,6], 4, 5))
print(find([1,2,3,4,4,6,6], 5, 3))
