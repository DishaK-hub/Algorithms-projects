def RBinSearch(a:list,l:int, h:int, key:float):
    if (l==h):
        if(a[l]== key):
            return l
        else:
            return 0
    else:
        mid = (l+h)//2
        print(mid)
        if (a[mid]==key):
            return mid
        elif(key < a[mid]):
            return RBinSearch(a,l,mid-1,key)
        else:
            return RBinSearch(a,mid+1,h,key)


a = [3,6,8,12,14,17,25,29,31,36,42,47,53,55,62]
print(RBinSearch(a,0,14,42))