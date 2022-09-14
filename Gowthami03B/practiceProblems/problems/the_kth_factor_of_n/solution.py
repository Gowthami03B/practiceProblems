import math
class Solution:
    def kthFactor1(self, n: int, k: int) -> int:
        if k == 1:
            return 1
        if k > n:
            return -1
        
        for i in range(1,n//2+1):#all factors are <=half
            if n%i == 0:
                k -= 1
            if k == 0:
                return i
        return n if k == 1 else -1#for prime number, k will be 1, say n=7, k=2, if k==3, then -1
    
    #heap O(sqrt(N) Log k) - heap of size k, O(min(k, sqrt(N)))
    def kthFactor(self, n: int, k: int) -> int:
        def heappush_k(num):
            heappush(heap, - num)
            if len(heap) > k:
                heappop(heap)

        heap = []
        #The divisors are paired, i.e., if i is a divisor of N, then N / i is a divisor of N, too. That means it's enough to iterate up to sqrt(N)
        for x in range(1, int(sqrt(n)) + 1):
            if n % x == 0:
                heappush_k(x)
                if x != n // x:#this is for storing say 24 has 1,2,3,4,6,8,12,24 and we are only iterating until 4, but we need 6,8,12,24 as well, hence if x != n//x
                    heappush_k(n // x)
                
        return -heappop(heap) if k == len(heap) else -1#heap pop here returns the kth element
                
        