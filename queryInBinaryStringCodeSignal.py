"""
Q4 - Query In A Binary String
Given a binary string s that contains only "0" and "1". You are also given an array query with the following operations:

"Count" - The answer to this query is the number of 1s in the binary string.
"Flip" - Flip the substring [0, idx] so that "0" -> "1" and "1" -> "0" and idx is the first "0" in the binary string. You are guaranteed that flip operation will only be called when there is at least one "0". The answer to the query is idx.
Constraints:

1 <= s.length() <= 100000 (1e5)
1 <= query.length <= 100000 (1e5)
Sample Testcases

s = "01110"
q = ["count", "count", "flip", "count", "count"]
Ans = [3, 3, 0, 4, 4]

s = "000"
q = ["flip", "count", "count"]
Ans = [0, 1, 1]

"""
from collections import deque
def queryInBinaryString(s, query):
    ones_queue = deque()
    zeros_queue = deque()
    for indx,c in enumerate(s):
        if c == '0':
            zeros_queue.append(indx)
        else:
            ones_queue.append(indx)
    # print(zeros_queue,ones_queue)
    res = []
    for q in query:
        if q == "count":
            res.append(len(ones_queue))
        else:
            indx = zeros_queue.popleft()
            temp_list = []
            while ones_queue[0] < indx:
                temp = ones_queue.popleft()#pop all the ones before the index
                temp_list.append(temp) #append to list, cannot directly append to queue as the order will not be correct

            # print(temp_list)
            zeros_queue.extendleft(reversed(temp_list))
            ones_queue.appendleft(indx) #the 0 being converted to 1, this one will always be the first
            # print(zeros_queue,ones_queue)
            res.append(indx)

    return res

# s = "01110"
# q = ["count", "count", "flip", "count", "count"]

s = "000001"
q = ["flip", "count", "count","flip","flip","count", "flip","flip","count"]
print(queryInBinaryString(s,q))
#[0,2,2,1,0,3,2,0,3]
#010001, 110001, 001001, 101001
