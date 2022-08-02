class Solution:
    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        if  n < 2:
            return []
        for i in range(n):
            rem = target - numbers[i]
            s,h = i+1, n-1
            while(s <= h):
                mid = (s+h)//2
                if(numbers[mid] == rem):
                    return [i+1, mid + 1]
                elif numbers[mid] > rem:
                    h = mid - 1
                else:
                    s = mid + 1

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low,high = 0, len(numbers)-1
        while low < high:
            tot = numbers[low] + numbers[high]
            if tot == target:
                return [low + 1, high+1]
            elif tot > target:
                high -= 1
            else:
                low +=1
        return []