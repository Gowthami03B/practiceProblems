"""
Given an array denoting shipment counts at each warehouses, calculate how many days it would take 
ship them all, if equal number of shipments can only be shipped from each warehouse having non-zero shipment.
Example - [4,2,3,3,3] -> it would take 3 days
2 shipments from each warehouse on 1st day => [2,0,1,1,1]
1 shipment from each warehouse on 2nd day => [1,0,0,0,0]
1 shipment from the 1st warehouse on 3rd day
"""
def findShipmentTime(nums):
    if len(nums) == 1:
        return 1
    if len(nums) == 0:
        return 0
    dayCnt = 0
    while(sum(nums) > 0):
        if min(nums) == 0:
           nums = [value for value in nums if value != 0]
        minShip = min(nums)
        nums = [x - minShip for x in nums]
        dayCnt +=1
        print(nums)
    return dayCnt

nums = [4,2,3,3,3]
print(findShipmentTime(nums))
