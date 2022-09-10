"""
Q4 - Query In A Binary String
Given a binary string s that contains only "0" and "1". You are also given an array query with the following operations:

"Count" - The answer to this query is the number of 1s in the binary string.
"Flip" - Flip the substring [1, idx] so that "0" -> "1" and "1" -> "0" and idx is the first "1" in the binary string. You are guaranteed that flip operation will only be called when there is at least one "0". The answer to the query is idx.
Constraints:

1 <= s.length() <= 100000 (1e5)
1 <= query.length <= 100000 (1e5)
"""
from collections import deque
def queryInBinaryString2CodeSignal(s, query):
    ones_queue = deque()
    for indx,c in enumerate(s):
        if c == '1':
            ones_queue.append(indx)
    res = []
    print(ones_queue)
    for q in query:
        if q == "count":
            res.append(len(ones_queue))
        else:
            indx = ones_queue.popleft()
            temp_list = []
            for i in range(indx):
                temp_list.append(i)
            # print(temp_list[::-1])
            ones_queue.extendleft(temp_list[::-1])
            res.append(indx)
    return res

s = "0000101"
q = ["count", "flip", "flip", "flip", "count"]
print(queryInBinaryString2CodeSignal(s, q))
