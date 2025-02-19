import random

def partition(arr, l, r):
	x = random.randint(0, r)
	i = l
	for j in range(l, r):
		
		if arr[j] <= x:
			arr[i], arr[j] = arr[j], arr[i]
			i += 1

	arr[i], arr[r] = arr[r], arr[i]
	
	return i

print(partition([1,4,3,2,7,5], 0, 6))