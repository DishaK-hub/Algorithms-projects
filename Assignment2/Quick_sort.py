def quick_sort(list1,l,h):
    if l < h:
        p = partition(list1,l,h)
        quick_sort(list1,l,p)
        quick_sort(list1,p+1,h)

def partition(list1,l,h):
    pivot = list1[l]
    i = l - 1
    j = h + 1

    while True:
        i = i + 1
        while list1[i] < pivot:
            i = i + 1
        j = j - 1
        while list1[j] > pivot:
            j = j - 1
        if i >= j:
            return j
        list1[i],list1[j] = list1[j],list1[i]

if __name__ == "__main__":
    array2 = ([34, 12, 7, 23, 32, 5, 62, 18], [12, 4, 7, 1, 9, 23, 6], [], [1, 2, 3, 4, 5, 6], [5, -2, 8, -5, 1, 2, -8])

    for a2 in array2:
        quick_sort(a2, 0, len(a2) - 1)
        print("Quick Sorted array:", a2)






