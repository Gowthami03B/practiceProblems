from collections import defaultdict
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #using hashmap or array as extra space
        # res = defaultdict(int)
        ans = []
        # for num in nums:
        #     res[num] = 1
        # print(res)
        # for i in range(1,len(nums)+1):
        #     if i not in res:
        #         ans.append(i)
        # return ans
        
        # arr = [0] * (len(nums) + 1)
        # for num in nums:
        #     arr[num] = 1
        # for i in range(1,len(nums)+1):
        #     if(arr[i] == 0):
        #          ans.append(i)
        # return ans
    
        #no extra space and O(N) 
        #time limit exceeded
        # for i in range(1,len(nums) + 1):
        #     if i not in nums:
        #         ans.append(i)
        # return ans
        for i in range(len(nums)):
            newIdx = abs(nums[i]) - 1 #numbers are 1..N but index is always i-1 hence finding correct index
            if nums[newIdx] > 0: 
                nums[newIdx] *= -1#marking numbers(1..N) as visited means they appeared in array
        print(nums) #[-4, -3, -2, -7, 8, 2, -3, -1] for 8,2 indices, numbers are already marked
        for i in range(0,len(nums)):
            if nums[i] > 0:
                ans.append(i+1)   #add +1 for number as index is -1
        return ans