class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: -x[1])  #sort by units, choose the box that has max units
        units = i = 0
        while truckSize > 0 and i < len(boxTypes):
            boxesToPick = min(truckSize, boxTypes[i][0])#how many boxes to pick is the min of truckSize and boxes
            units += boxesToPick * boxTypes[i][1]
            truckSize -= boxesToPick
            i += 1
        print(truckSize)
        return units