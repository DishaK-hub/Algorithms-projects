def ksmallest(k:int, a:list)-> list:
    a_sort = sorted(a)
    if k <= len(a_sort):
        return a_sort[:k]
    else:
        return a_sort
    
print(ksmallest(20, [10, 7, 23, 2, 9, 3, 7, 8, 11, 5, 7]))