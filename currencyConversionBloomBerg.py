from collections import defaultdict
from collections import deque
"""
Question
Paramenters:

array of currency conversion rates. E.g. ['USD', 'GBP', 0.77] which means 1 USD is equal to 0.77 GBP
an array containing a 'from' currency and a 'to' currency
Given the above parameters, find the conversion rate that maps to the 'from' currency to the 'to' currency.
Your return value should be a number.

Example:
You are given the following parameters:

Rates: ['USD', 'JPY', 110] ['US', 'AUD', 1.45] ['JPY', 'GBP', 0.0070]
To/From currency ['GBP', 'AUD']
Find the rate for the 'To/From' curency. In this case, the correct result is 1.89.
"""
def getRatio(start, end, data):
    dict = defaultdict(list)
    for node in data:
        dict[node[0]].append([node[1], node[2]])
        dict[node[1]].append([node[0], 1.0 / node[2]])
    queue = deque()
    queue.append((start, 1.0))
    visited = set()
    while queue:
        curr, num = queue.popleft()
        if curr == end:
            return num
        for next_curr, next_num in dict[curr]:
            if next_curr not in visited:
                visited.add(next_curr)
                queue.append((next_curr, next_num * num))
    return -1
data = [("USD", "JPY", 110), ("USD", "AUD", 1.45), ("JPY", "GBP", 0.0070)]
print(getRatio("GBP", "AUD", data))
