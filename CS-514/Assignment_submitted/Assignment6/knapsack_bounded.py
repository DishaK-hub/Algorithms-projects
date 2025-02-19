def best(W, arr):
	dp_arr = [0 for i in range(W + 1)]
	cost_arr =[[ 0 for i in range(len(arr))] for j in range(W+1) ]
	for i in range(W + 1):
		for j in range(len(arr)):
			if (arr[j][0] <= i ):
				if (dp_arr[i] < dp_arr[i - arr[j][0]] + arr[j][1] and (cost_arr[i - arr[j][0]][j] <arr[j][2])):
					cost_arr[i]=cost_arr[i-arr[j][0]].copy()
					cost_arr[i][j]+=1
					dp_arr[i]=dp_arr[i - arr[j][0]] + arr[j][1]
	result =0
	for i in range (W+1):
		if dp_arr[i]>=dp_arr[result]:
			result=i
	
	return dp_arr[result],cost_arr[result]


