def mergesort(array1):
    if len(array1) > 1:
        n = len(array1)//2
        sub_array1 = array1[:n]
        sub_array2 = array1[n:]
        mergesort(sub_array1)
        mergesort(sub_array2)
        i = j = k = 0
        while i < len(sub_array1) and j < len(sub_array2):
            if sub_array1[i] <= sub_array2[j]:
                array1[k] = sub_array1[i]
                i += 1
            else:
                array1[k] = sub_array2[j]
                j += 1
            k += 1
 
        while i < len(sub_array1):
            array1[k] = sub_array1[i]
            i += 1
            k += 1
 
        while j < len(sub_array2):
            array1[k] = sub_array2[j]
            j += 1
            k += 1

if __name__ == '__main__':
    array1 = [4, 2, 5, 1, 6, 3]
    mergesort(array1)
    print(array1)