class Solution:
    def numberOfWeakCharacters1(self, properties: List[List[int]]) -> int:
        #bruteforce
        #sort by attack, while defense is > defense of others, count weak characters
        properties = sorted(properties)#sorts and returns sorted list
        #properties.sort(key = lambda x:x[0])#changes the list in place and returns none
        print(properties)
        # visited = collections.defaultdict() #data has duplicates, set won't work
        # and (properties[i][0], properties[i][1]) not in visited
        weakCnt = 0
        for i in range(len(properties)):
            for j in range(i+1,len(properties)):
                if properties[i][1] < properties[j][1] and properties[i][0] != properties[j][0]:
                    weakCnt += 1
                    break
        return weakCnt
    
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        #sort first in desc and second in asc (if two have same first value, they will be arranged as [2,3],[2,4] so when we compare second element we don't count them as 1)
        properties = sorted(properties, key = lambda x:(-x[0],x[1]))
        weakCnt, currMax = 0, 0
        for attack, defense in properties:
            if defense < currMax:
                weakCnt += 1
            else:
                currMax = max(currMax, defense)
        return weakCnt