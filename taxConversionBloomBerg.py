"""
What data structure would you use to store the federal tax slab?

Range - Tax Rate
0-10000 - 15%
10001-50000 - 20%
50001-250000 - 28%
250001-500000 - 37%
500001 and above - 42%
(Not the exact values)

Input - 85000
Output - 10000 * 0.15 + 40000 * 0.20 + 35000 * 0.28 = 19300
"""
def findTax(amount):
    #best way to represent these is using array [upperbound, tax percentage]
    brackets =[[10000,15],[50000,20],[250000,28],[500000,37],[float("inf"),42]]
    tax = prev = 0
    for upper, per in brackets:
        if amount >= upper:
            tax += (upper - prev)*per/100
            prev = upper
        else:
            tax += (amount - prev)*per/100
            return tax
    return tax

print(findTax(1005000))
