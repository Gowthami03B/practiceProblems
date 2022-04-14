"""
Given an one-dimensional unsorted array A containing N integers.

You are also given an integer B, find if there exists a pair of elements in the array whose difference is B.

Return 1 if any such pair exists else return 0.

Problem Constraints
1 <= N <= 105
-103 <= A[i] <= 103
-105 <= B <= 105


Input Format
First argument is an integer array A of size N.

Second argument is an integer B.


Output Format
Return 1 if any such pair exists else return 0.


Example Input
Input 1:

 A = [5, 10, 3, 2, 50, 80]
 B = 78
Input 2:

 A = [-10, 20]
 B = 30

"""

from collections import defaultdict
#O(N), O(N) to store hashmap
def pairDifference(A,B):
        map = defaultdict(int)
        for i in range(len(A)):
            map[A[i]] += 1
        for i in range(len(A)):
            if B + A[i] in map:
                if B == 0 and map[A[i]] > 1:
                    break
                return 1
        return 0

A = [ 2,20]
B = 0

#O(N LOG N + N) (sorting + array loop == o(n log n)), O(1)
def solve(A, B):
        i, j = 0, 1
        A.sort()
        while i < len(A) and j < len(A):
            if i!=j and abs(A[j] - A[i]) == B:
                return 1
            if abs(A[j] - A[i])  < B:
                j += 1
            else:
                i += 1
        return 0

def solveB( nums, B):
    start , high = 0 ,len(nums) - 1
    searchval = A[start] + B
    while(start <= high):
        mid = (start+high)//2
        if(nums[mid] == searchval):
            return 1
        elif(nums[mid] < searchval):
            start = mid + 1
            searchval = A[start] + B
        else:
            high = mid -1
    return 0

def binary_search(array, target):
	left, right = 0, len(array) - 1
	while left <= right:
		mid = (left + right) // 2

		if target  == array[mid]:
			return True
		elif target < array[mid]:
			right = mid - 1
		else:
			left = mid + 1
	return False

#so second no is first no + diff, hence we can do a binary search for second no - O(N log n) - due to sorting
def find_pair(array, diff):
	array.sort()

	for first_number in array:
		second_number = first_number + diff
		if binary_search(array, second_number):
			print(first_number, second_number)
			return 1

	return 0
