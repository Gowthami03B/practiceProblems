class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: -x[1])  
        units = i = 0
        while truckSize > 0 and i < len(boxTypes):
            boxesToPick = min(truckSize, boxTypes[i][0])
            units += boxesToPick * boxTypes[i][1]
            truckSize -= boxesToPick
            i += 1
        print(truckSize)
        return units