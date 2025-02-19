def num_inversions(array1, t1, L, R):
	count1 = 0
	if L < R:
		mid = (L + R)//2
		count1 += num_inversions(array1, t1, L, mid)
		count1 += num_inversions(array1, t1, mid + 1, R)
		count1 += merge(array1, t1, L, mid, R)
	return count1

def merge(array2, t1, L, mid, R):
	i = L	 
	j = mid + 1 
	k = L	
	count2 = 0
	while i <= mid and j <= R:
		if array2[i] <= array2[j]:
			t1[k] = array2[i]
			k += 1
			i += 1
		else:
			t1[k] = array2[j]
			count2 += (mid-i + 1)
			k += 1
			j += 1
    
	while i <= mid:
		t1[k] = array2[i]
		k += 1
		i += 1
	while j <= R:
		t1[k] = array2[j]
		k += 1
		j += 1

	for e in range(L, R + 1):
		array2[e] = t1[e]

	return count2

eg_arr = [2, 4, 1, 3]
n = len(eg_arr)
print("num_inversions(", eg_arr , ")")
t1 = [0]*n
result = num_inversions(eg_arr, t1, 0, n-1)
print(result)