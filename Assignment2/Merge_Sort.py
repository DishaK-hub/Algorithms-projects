#Mergesort implementation
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





