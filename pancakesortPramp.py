"""
Given an array of integers arr:

Write a function flip(arr, k) that reverses the order of the first k elements in the array arr.
Write a function pancakeSort(arr) that sorts and returns the input array. You are allowed to use only the function flip you wrote in the first step in order to make changes in the array.
Example:

input:  arr = [1, 5, 4, 3, 2]

output: [1, 2, 3, 4, 5] # to clarify, this is pancakeSort's output
Analyze the time and space complexities of your solution.
Note: it’s called pancake sort because it resembles sorting pancakes on a plate with a spatula, where you can only use the spatula to flip some of the top pancakes in the plate

Time Complexity: let N be the length of the input array. There are N-1 iterations, in each we place one element in its place. 
Every iteration takes 2 flips to move every member in the array to its place, and each takes O(N) at most. 
In addition, every iteration we find the maximal element, which is also done in O(N). 
There are N-1 iterations that take O(N) time and each iteration has 2 flips hence total time complexity is O(N2).
"""
def pancake_sort(nums):
    i = len(nums)
    while(i > 0):
        #sorting means max number at end 
        maxIdx = nums.index(max(nums[:i])) #find index of max element in list - 1
        nums = flip(nums, maxIdx) #reverse first k elements until max index, max number would be at start - [5,1,4,3,2]
        flip(nums, i)#flip whole array as max element goes to last - [2,3,4,1,5]
        #repeat process for first 4 elements except last one
        i -= 1

"""
2nd iteration
maxIdx = 2, [4,3,2,1,5], [1,2,3,4,5]
3rd iteration
maxidx = 2, [3,1,2,4,5], [2,1,3,4,5]
4th
maxidx = 0 ,[1,2,3,4,5]
"""   
def flip(nums,k):
    return nums[:k][::-1] + nums[k:] #start:stop:step - reverses the first k elements

nums = [1,5,4,3,2]
k = 2
print(flip(nums,k))
