class Solution:
    #Build from left to right, by filling all positions with 'a'
    #we know that the smallest string would start with 'a's and we need to fill last positions with higher chars
    def getSmallestString1(self, n: int, k: int) -> str:
        res = ["a"]* n
        k -= n #reduce k value after filling a's
        for i in range(n, 0, -1): #reverse loop
            add = min(k,25)#after allocating 'a', max value that can be assigned to other positions is 26-1, assign the min of k and 25
            res[i-1] = chr(ord(res[i-1]) + add)#in the ascii system, ord('a')+add would be the new character, ord(a)=97 and z is 122, diff is 25
            k -= add
        return "".join(res)
    
    #Build from right
    def getSmallestString(self, n: int, k: int) -> str:
        res = [""]* n
        for i in range(n-1, -1, -1):
            add = min(k-i,26)#min of k-i+1, we need to allocate atleast 1 for remaining positions, hence k-i+1, 26
            res[i] = chr(add + ord('a') - 1)#add + ord('a') - 1,ord(a)=97 and z is 122, diff is 25 
            k -= add
        print(ord('a')-ord('z'))
        return "".join(res)
        
        