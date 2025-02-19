def diff(a,x):
    diff_arr=[]
    for i in range(0,len(a)):
        diff_arr.append(abs(a[i]-x))
    return diff_arr

def find(a, x, k):
    list1=[]
    diff_array = sorted(diff(a,x))
    diff_array = diff_array[:k]
    for i in range(0,len(a)):
        if((abs(a[i]-x) in diff_array) and len(list1)<k):
            list1.append(a[i])
    return list1