class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
            countFreq = Counter(arr)
            print(countFreq)
            uniqueVals = set(countFreq.values())
            return len(uniqueVals) == len(countFreq.values())