"""
Given an array ‘A’ of sorted integers and another non negative integer k, find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.
Example:
Input :

    A : [1 3 5] 
    k : 4
Output : YES
as 5 - 1 = 4
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
Try doing this in less than linear space complexity
"""

def diffPossible(arr, B):
		i , j = 0, 1
		while(i < j and i < len(arr) and j < len(arr)):
			if arr[j] - arr[i] > B:
				i+=1
				if(i == j):
					j+=1
			elif arr[j] - arr[i] < B:
				j+=1
			else:
				return 1
		return 0

arr=[1,2,2,3,5]
B = 10
print(diffPossible(arr, B))
