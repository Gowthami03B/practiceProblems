#https://www.geeksforgeeks.org/find-a-repeating-and-a-missing-number/
#time O(n log n), Space O(1)
def missingandrepeatingSorting(nums):
    nums.sort()
    output = []
    for i in range(0,len(nums)-1):
        if i+1 not in nums:
            output.insert(1,(i+1)) #missing
        if nums[i] == nums[i+1]:
            output.insert(0,nums[i]) #repeating

    return output

def missingandrepeatingCountArr(nums):
    n = len(nums)
    count = [0] * n
    output = []
    for i in range(n):
        if count[nums[i]-1] == 0:
            count[nums[i]-1] = 1
        else:
            output.insert(0,nums[i])

    for i in range(n):
        if count[i] == 0:
            output.insert(1,i+1)
    return output

def missingandrepeatingCountMarkVisited(nums):
    n = len(nums)
    output = []
    for i in range(n):
        if nums[abs(nums[i])- 1] > 0:
            nums[abs(nums[i])- 1] = -nums[abs(nums[i])- 1]
        else:
            output.insert(0,abs(nums[i]))

    for i in range(n):
        if nums[i] > 0:
            output.insert(1,abs(nums[i]))
    return output

def missingandrepeatingCountDict(nums):
    n = len(nums)
    output = []
    map = {}
    for i in range(n):
        if nums[i] not in map:
            map[nums[i]] = i
        else:
            output.insert(0,nums[i])
    print(map)
    for i in range(1,n+1):
        if i not in map:
            output.insert(1,i)
    return output



nums = [4,3,2,6,1,1]
nums1 = [7, 3, 4, 5, 5, 6, 2]
nums2 = [1,3,3]
print(missingandrepeatingCountDict(nums))
