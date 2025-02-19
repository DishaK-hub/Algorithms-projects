def find(array1):
    list2=[]
    for i in range(0,len(array1)-1):
        for j in range(i+1,len(array1)):
            list1=[]
            if (array1[i]+array1[j]) in array1:
                ind = array1.index(array1[i]+array1[j])
                list1.append(array1[i])
                list1.append(array1[j])
                list1.append(array1[ind])
                #print(list1)
                list2.append(list1)
    
    return list2       

print(find([1, 4, 2, 3, 5]))