def max_wis(list1):
    if list1==[]:
        return (0,[])
    for i in range (0,len(list1)):
        if list1[i]<0:
            list1[i]=0
    n = len(list1)
    list2 = [0] * (n + 1)
       
    list2[0] = 0
        
    list2[1] = list1[0]
      
    for i in range(2, n + 1):
        list2[i] = max(list2[i - 1], 
                                  list2[i - 2] + list1[i-1])    
    list3 = []
    i = n
    while i >= 1:
        if list2[i-1] >= list2[i-2] + list1[i-1]:
            i = i - 1
        else:
            if list1[i-1]!=0:
                list3.insert(0,list1[i-1])
            i = i - 2
    
    return (list2[n],list3)

print(max_wis([-1,-5,-4]))
print(max_wis([]))
print(max_wis([-5, -1, -4]))
print(max_wis([7,8,5]))
print(max_wis([-1,8,10]))