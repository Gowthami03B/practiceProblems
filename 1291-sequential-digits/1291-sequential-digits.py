class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sample="123456789"
        n=10
        res = []
        for i in range(len(str(low)),len(str(high))+1):
            for start in range(n-i):
                num = int(sample[start:start+i])
                if num < low:
                    continue
                elif num >=low and num<=high:
                    res.append(num)
                else:
                    break
        return res