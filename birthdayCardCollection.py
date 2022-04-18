"""
HackerCards is a trendy new card game. Each type of HackerCard has a distinct ID number greater that or
 equals to 1, and the cost of each HackerCard equals its ID number. 
 For example, HackerCard 1 costs 1, HackerCard 5 costs 5, and so on.

Leanne already has a collection started. For her birthday, Mike wants to buy her as many cards as he can,
 but they must cost less than or equals to his budget. He wants to buy one each of some cards 
 she doesn't already have. 
 If he has to make one choice among several, he will always choose the lowest cost option. 
 Determine which cards he will buy.

For example, Leanne's collection = [2, 4, 5] and Mike has d = 7 to spend. He can purchase a maximum of 2 cards, the 1 and the 3 to add to her collection. Two other options he has are 1 and 6 (costs more) or 7(fewer cards, costs more)

Input: 
collections[] = [1,3,4]
d = 7

output: [2,5]

collections[] = [2,4,5]
d = 7

output: [1,3] //costs less than 2,5 (if he has a choice he will always choose lower cost)
"""

#imp point to note - He wants to buy one each of some cards she doesn't already have. 
#If he has to make one choice among several, he will always choose the lowest cost option. 
# we know we have to add up other numbers, and we can add as many as we can until it's less than target
#also he prefers the first low cost option - hence no need to be greedy, first best solution is the answer
#O(N) O(1)
def birthdayCard(nums, target):
    sum = 0
    res = []
    for i in range(1, target + 1):
        if i in nums:
            continue
        if sum + i > target:
            break
        sum += i
        res.append(i)
    return res

nums = [2,4,5]
target = 7
print(birthdayCard(nums,target))

