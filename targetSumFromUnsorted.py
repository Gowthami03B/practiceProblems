"""
Given two unsorted arrays, find all pairs whose sum is x
Input : arr1[] = {1, 2, 4, 5, 7} 
        arr2[] = {5, 6, 3, 4, 8}  
        x = 9
Output : 1 8
         4 5
         5 4
"""
def targetSumFromUnsorted(arr1,arr2,target):
    n = len(arr1)
    m = len(arr2)
    if n < m:
        arr1,arr2=arr2,arr1
    set_arr1 = set(arr1)
    pairs = []
    for i in range(len(arr2)):
        if target - arr2[i] in set_arr1:
            pairs.append([target - arr2[i],arr2[i]])
    return pairs

arr1=[1,2,4,5,7]
arr2=[5,6,3,4,8]
x = 9
print(targetSumFromUnsorted(arr1,arr2,x))
