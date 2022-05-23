class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        totalBoxes = 0
        indexOfBoxes = []
        res = []
        for idx,box in enumerate(boxes):
            totalBoxes += int(box)
            if int(box):
                indexOfBoxes.append(idx)
        print(totalBoxes,indexOfBoxes)
        for idx,box in enumerate(boxes):
            operations = 0
            for i in range(len(indexOfBoxes)):
                operations += abs(indexOfBoxes[i] - idx)
            res.append(operations)
        return res
                    