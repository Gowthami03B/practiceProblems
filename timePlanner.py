def MealPlanner(slotA, slotB, duration):
    i,j = 0,0
    while(i < len(slotA) and j < len(slotB)):
        if(slotA[i][0] >= slotB[j][0] and slotB[j][1] <= slotA[i][1]):
            if(slotB[j][1] - slotA[i][0] >= duration):
                return slotA[i][0], slotA[i][0]+duration
            else:
                j+=1
        elif(slotA[i][0] >= slotB[j][0] and slotB[j][1] >= slotA[i][1]):
            if(slotA[i][1] - slotA[i][0] >= duration):
                return slotA[i][0], slotA[i][0]+duration
            else:
                j+=1
        elif(slotA[i][0] <= slotB[j][0] and slotA[i][1] >= slotB[j][1]):
            if(slotB[j][0] - slotA[i][1] >= duration):
                return slotB[j][0], slotB[j][0]+duration
            else:
                i+=1
        elif(slotA[i][0] <= slotB[j][0] and slotA[i][1] <= slotB[j][1]):
            if(slotA[i][1] - slotB[j][0] >= duration):
                return slotA[i][1], slotA[i][1]+duration
            else:
                i+=1
    return []

def MealPlannerOptimized(slotA, slotB, duration):
    i,j = 0,0
    while(i < len(slotA) and j < len(slotB)):
        start = max(slotB[j][0], slotA[i][0])
        end = min(slotB[j][1], slotA[i][1])
        if(end - start >= duration):
            return start, start+duration
        elif start > end: #other solution tried if A[i][1] > B[j][1], then j++, else i++
            i += 1
        else:
            j += 1
    return []
# slotA = [[35,90]]
# slotB = [[40,60]]
# slotB = [[100,110]]
# slotA = [[10,30],[50,80]]
# slotB = [[0,10],[30,60]]
slotA = [[10, 50], [60, 120], [140, 210]]
slotB = [[0, 15], [60, 70]]
# slotA = [[10, 50], [60, 120], [140, 210]]
# slotB = [[0, 15], [60, 70]]
duration = 8
print(MealPlannerOptimized(slotA, slotB, duration))
