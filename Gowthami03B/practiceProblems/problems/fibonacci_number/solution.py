from math import sqrt
class Solution:
    def __init__(self):
        self.cache = {0:0,1:1}
    def fibRecursion(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        return self.fib(n-1) + self.fib(n-2)
    
    def fib1(self, n: int) -> int: 
        if n in self.cache:
            return self.cache[n]
        self.cache[n] = self.fib(n-1) + self.fib(n-2)
        return self.cache[n]
            
    def fib(self, n: int) -> int:
        a,b = 0,1
        while n > 0:
            a,b=b,a+b
            n-=1
        return a