"""
For a given sorted array ‘A’ of size mxn, write a code to find the number of elements that are 
less than or equal to a target element ‘V.’
"""
def findEleLessThanTarget(nums,target):
    rowlen , collen = len(nums), len(nums[0])
    if rowlen == 0 or collen == 0:
        return -1
    if nums[0][0] > target:
        return 0
    s,l = 0, rowlen * collen - 1
    countofele = 0
    while(s <= l):
        mid = (s+l)//2
        pivotEle = nums[mid//collen][mid%collen]
        if(pivotEle > target):
            l = mid - 1
            countofele = min(mid, countofele)
            print(mid)
        elif(pivotEle < target):
            s = mid + 1
            countofele = mid
            print(mid)
        else:
            return mid + 1
    return countofele + 1
        
nums = [[-1,-3,5,7,10],[20,45,67,78,89]]
# nums = [[3,5,7,10]]
target = 88
# target = 67
print(findEleLessThanTarget(nums, target))
