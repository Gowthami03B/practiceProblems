#Efficient Harvest: A farmer uses pivot irrigation to water a circular field of crops. Due to varying conditions, the field does not produce consistently. The farmer wants to achieve maximum profit using limited resources for harvest. The field is segmented into a number of equal segments, and a profit is calculated for each segment. This profit is the cost to harvest versus the sale price a the produce. The farmer will harvest a number of contiguous segments along with those opposite. Determine the maximum profit the farmer can achieve. For example, the field is divided into n = 6 sections and will select k = 2 contiguous sections and those opposite for harvest. The profit estimates are profit = [1, 5, 1, 3, 7.-3) respectively. The diagrams below show the possible choices with profits(0) at the 9 o'clock position and filling counterclockwise. -3 The profit levels, from left to right, are 1 + 5+7 + 3 - 16,5+1 +7 +-3-10, and 1 + 3+3+1 -2. The maximum profit is 16. Function Description Complete the function maxProfit in the editor below. The function must return the maximum profit achievable. maxProfit has the following parameters: k an integer denoting the half of the needed amount of pieces of the field. profit[profit[0],..profit[n-1].
def maxHarvest(arr, k):
    n = len(arr)
    maxprofit = float('-inf')
    for i in range(n//2):
        sum = 0
        for j in range(k):
            currIndex = i+j
            oppIndex = (currIndex + (n//2))%n
            sum += arr[currIndex] + arr[oppIndex]
        maxprofit = max(maxprofit,sum)
    return maxprofit

# print(maxHarvest([3, -5], 1)) #-2
print(maxHarvest([1, 5, 1, 3, 7, -3], 2)) #16
print(maxHarvest([-6, 3, 6, -3], 1)) #0

# Time Complexity O(nk) where N is the number of segments and k is the number of consecutive segments we consider per option.
# Space Complexity O(1)
#https://leetcode.com/discuss/interview-question/1321204/efficient-harvest-faang-oa-question-2021
