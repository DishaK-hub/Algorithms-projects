import random # for randomized pivot
#implementation of merge sort algorithm
def merge_sort(list1):
   n = len(list1)
   if n <= 1:
       return list1
   return merge_sorted_lists(merge_sort(list1[:n//2]), merge_sort(list1[n//2:]))
def merge_sorted_lists(sorted1, sorted2):
   if not sorted1 or not sorted2:
       return sorted1 + sorted2


   merged_list = []
   ind1, ind2 = 0, 0
   len1, len2 = len(sorted1), len(sorted2)


   while ind1 < len1 or ind2 < len2:
       if ind1 == len1 or (ind2 != len2 and sorted1[ind1] > sorted2[ind2]):
           merged_list.append(sorted2[ind2])
           ind2 += 1
       else:
           merged_list.append(sorted1[ind1])
           ind1 += 1
   return merged_list

#Implementation of quick sort algorithm
#When the pivot is the first element in the list
def quick_sort1(list1,l,h):
    if l < h:
        p = partition(list1,l,h)
        quick_sort1(list1,l,p)
        quick_sort1(list1,p+1,h)

#When the pivot the chosen randomly
def quick_sort2(list1, left, right):
    if left < right:
        pivot_index = left + random.randint(0, right - left)
        pivot_index = partition(list1, left, right, pivot_index)
        quick_sort2(list1, left, pivot_index - 1)
        quick_sort2(list1, pivot_index + 1, right)

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

if __name__ == '__main__':
    #testcases 
    arr0 = [197]
    arr1 = [49, 146, 88, 199, 35, 37, 189, 113, 111, 34, 24, 182, 142, 75, 155]
    arr2 = [17, 155, 58, 185, 94, 129, 167, 73, 76, 162, 183, 188, 87, 61, 134, 160, 6, 169, 79, 89, 110, 116, 36, 123,
            99, 180, 136, 50, 19, 37, 130, 25, 144, 55, 85, 176, 121, 146, 12, 88, 1, 39, 26, 112, 9, 86, 54, 143, 63,
            30, 93, 137, 101, 21, 97, 126, 107, 179, 114, 72, 64, 145, 150, 174, 5]
    arr3 = [114, 157, 145, 74, 27, 98, 194, 58, 93, 70, 156, 88, 56, 161, 69, 51, 80, 186, 125, 17, 126, 18, 191, 104,
            32, 111, 190, 22, 160, 77, 81, 76, 195, 85, 124, 14, 73, 31]
    arr4 = []
    arr5 = [68, 83, 6, 138, 20, 36, 71, 182, 108, 17, 96, 115, 194, 7, 150, 85, 177, 106, 53, 51, 66, 170, 111, 119,
            197, 141, 168, 37, 65, 78, 183, 189, 113, 110, 74, 49, 56, 45, 116, 97, 185, 24, 89, 64, 41, 193, 86, 54]


