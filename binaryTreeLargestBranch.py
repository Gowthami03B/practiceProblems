"""
Given a binary tree represented as an array, for example, [3,6,2,9,-1,10] represents a binary tree and -1 is a non existent node. Write a function that determines whether the left or right branch of the ree is larger. The size of each branch s the sum of the node values. The function should return the string "Right" if the right size is larger and "Left" if the left size is larger. If the tree has 0 nodes of it the size of the branches are equal, return the empty string.
function public String findLargeTree(long[] arr)
Sample cases:

1 [3,6,2,9,-1,10] return "Left".
[1,10,5,1,0,6] return ""
Explanation: Size of both branches are equal
"""
def solution(arr):
    # Type your solution here 
    def tree_sum(arr, i):#recursively find the sum
        if len(arr) <= i or arr[i] == -1:#if i goes out of bounds
            return 0
        return arr[i] + tree_sum(arr, 2*i + 1) + tree_sum(arr, 2*i + 2)
    
    n = len(arr)
    if not arr or n == 0:
        return ""
    leftSum, rightSum =tree_sum(arr,1), tree_sum(arr,2)
    
    if leftSum == rightSum:
        return ""
    elif leftSum > rightSum:
        return "Left"
    else:
        return "Right"

    
