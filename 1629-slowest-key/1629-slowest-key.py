class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        longest = releaseTimes[0]
        longKey = 0
        for i in range(1,len(releaseTimes)):
            k = releaseTimes[i] - releaseTimes[i-1]
            if k == longest:
                longKey = i if ord(keysPressed[i]) > ord(keysPressed[longKey]) else longKey
            elif k > longest:
                longKey = i
                longest = k
            
        return keysPressed[longKey]
        