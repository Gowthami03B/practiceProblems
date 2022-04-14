"""
Array Quadruplet
Given an unsorted array of integers arr and a number s, write a function findArrayQuadruplet that finds four numbers (quadruplet) in arr that sum up to s. Your function should return an array of these numbers in an ascending order. If such a quadruplet doesn’t exist, return an empty array.

Note that there may be more than one quadruplet in arr whose sum is s. You’re asked to return the first one you encounter (considering the results are sorted).

Explain and code the most efficient solution possible, and analyze its time and space complexities.

Example:

input:  arr = [2, 7, 4, 0, 9, 5, 1, 3], s = 20

output: [0, 4, 7, 9] # The ordered quadruplet of (7, 4, 0, 9)
                     # whose sum is 20. Notice that there
                     # are two other quadruplets whose sum is 20:
                     # (7, 9, 1, 3) and (2, 4, 9, 5), but again you’re
                     # asked to return the just one quadruplet (in an
                     # ascending order)
"""

#bruteforce - using 4 nested loops to form a quadrapulet and its time complexity is O(N^4).
def arrayQuadrapulet(arr,s):
    n = len(arr)
    arr.sort()
    if n < 4:
        return []
    for i in range(n-3): # i can only reach n-3rd element, since we need 3 more elements after i to form quadrapulet
        for j in range(i+1, n-2): # j can only reach n-2 element, since we need 2 more elements after i,j to form quadrapulet
            rem = s - (arr[j] + arr[i])
            #two pointers to find rem (if sum of any 2 elements in the remaining array  == rem)
            low , high = j+1, n-1
            while(low < high):
                if(arr[low] + arr[high] == rem):
                    return [arr[i],arr[j],arr[low],arr[high]]
                elif(arr[low] + arr[high] > rem):
                    high -= 1
                else:
                    low += 1
    return [] 


arr = [2, 7, 4, 0, 9, 5, 1, 3]
s = 20
print(arrayQuadrapulet(arr,s))
