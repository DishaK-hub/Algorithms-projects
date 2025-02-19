def best(W, arr):
	dp_arr = [0 for i in range(W + 1)]
	cost_arr =[ [] for _ in range(W+1) ]
	result=[0 for i in range(len(arr))]
	for i in range(W + 1):
		for j in range(len(arr)):
			if (arr[j][0] <= i):
				if (dp_arr[i] < dp_arr[i - arr[j][0]] + arr[j][1]):
					dp_arr[i]=dp_arr[i - arr[j][0]] + arr[j][1]
					cost_arr[i]= [j]+cost_arr[i - arr[j][0]]
	
	for i in range (len(cost_arr[W])):
		result[cost_arr[W][i]]+=1
	return dp_arr[W],result


print(best(58, [(5, 9), (9, 18), (6, 12)]))
print(best(92, [(8, 9), (9, 10), (10, 12), (5, 6)]))
print(best(3, [(1, 2), (2, 5)]))