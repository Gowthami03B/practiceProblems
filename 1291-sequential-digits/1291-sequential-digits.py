class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sample="123456789" #say 100, 800, max no we can get is 789 hence we need to explore until 10 - i
        #no of combinations are constant hence O(1)
        n=10
        res = []
        for i in range(len(str(low)),len(str(high))+1):
            for start in range(n-i):#0 to n-i #max we can go to 7 + len(low)
                num = int(sample[start:start+i])
                if num < low:
                    continue
                elif num >=low and num<=high:
                    res.append(num)
                else:
                    break
        return res