class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        #so basically the target can be formed by dividing into different parts
        nums_map = collections.Counter(nums)#create a map of nums with counts
        res= 0
        for first_part in nums_map:#say these are the first parts
            numCount = nums_map[first_part]#first part count
            if target.startswith(first_part):#if target starts with this, there is a potential for second_part also being present in map
                second_part = target[len(first_part):]#second_part is from len(first_part):end
                res += numCount * nums_map[second_part]#no of unique pairs is first part count * second part count since we consider i,j and also j,i
                
                if first_part == second_part:#but if first and second parts are same, then we would hve counted double, hence we subtract the same
                    res -= nums_map[second_part]
        return res
    
    def numOfPairs1(self, nums: List[str], target: str) -> int:
        nums_map = collections.Counter(nums)
        res = 0
        for i in range(len(target)):
            first_part = target[:i+1]
            second_part = target[i+1:]
            if first_part in nums_map and second_part in nums_map:
                res += nums_map[first_part] * nums_map[second_part]
                if first_part == second_part:
                    res -= nums_map[first_part] 
        return res