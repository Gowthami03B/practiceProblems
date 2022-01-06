class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        for x in range(1, n // 2 + 1):
            if n % x == 0:
                k -= 1
                if k == 0:
                    return x
        
        return n if k == 1 else -1
            
                