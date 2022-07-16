''' Suppose we have an unsorted log file of accesses to web resources. Each log entry consists of an 
access time, the ID of the user making the access, and the resource ID. 

The access time is represented as seconds since 00:00:00, and all times are assumed to be in the same day.

Example:
logs1 = [
    ["58523", "user_1", "resource_1"],
    ["62314", "user_2", "resource_2"],
    ["54001", "user_1", "resource_3"],
    ["200", "user_6", "resource_5"],    
    ["215", "user_6", "resource_4"],
    ["54060", "user_2", "resource_3"],
    ["53760", "user_3", "resource_3"],
    ["58522", "user_22", "resource_1"],
    ["53651", "user_5", "resource_3"],
    ["2", "user_6", "resource_1"],
    ["100", "user_6", "resource_6"],
    ["400", "user_7", "resource_2"],
    ["100", "user_8", "resource_6"],
    ["54359", "user_1", "resource_3"],
]
r3 : 54000 54060 54501 
r4: 200 400 600

Example 2:
logs2 = [
    ["300", "user_1", "resource_3"],
    ["599", "user_1", "resource_3"],
    ["900", "user_1", "resource_3"],
    ["1199", "user_1", "resource_3"],
    ["1200", "user_1", "resource_3"],
    ["1201", "user_1", "resource_3"],
    ["1202", "user_1", "resource_3"]
]

Example 3:
logs3 = [
    ["300", "user_10", "resource_5"]
]

Write a function that takes the logs and returns the resource with the highest number of accesses 
in any 5 minute window, together with how many accesses it saw.

Expected Output:
most_requested_resource(logs1) # => ('resource_3', 3) [resource_3 is accessed at 53760, 54001, and 54060]
most_requested_resource(logs2) # => ('resource_3', 4) [resource_3 is accessed at 1199, 1200, 1201, and 1202]
most_requested_resource(logs3) # => ('resource_5', 1) [resource_5 is accessed at 300]

Complexity analysis variables:

n: number of logs in the input

'''


logs1 = [
    ["58523", "user_1", "resource_1"],
    ["62314", "user_2", "resource_2"],
    ["54001", "user_1", "resource_3"],
    ["200", "user_6", "resource_5"],  
    ["215", "user_6", "resource_4"],
    ["54060", "user_2", "resource_3"],
    ["53760", "user_3", "resource_3"],
    ["58522", "user_22", "resource_1"],
    ["53651", "user_5", "resource_3"],
    ["2", "user_6", "resource_1"],
    ["100", "user_6", "resource_6"],
    ["400", "user_7", "resource_2"],
    ["100", "user_8", "resource_6"],
    [ "54359", "user_1", "resource_3"],
]

logs2 = [
    ["300", "user_1", "resource_3"],
    ["599", "user_1", "resource_3"],
    ["900", "user_1", "resource_3"],
    ["1199", "user_1", "resource_3"],
    ["1200", "user_1", "resource_3"],
    ["1201", "user_1", "resource_3"],
    ["1202", "user_1", "resource_3"]
]

logs3 = [
    ["300", "user_10", "resource_5"]
]

import collections
from collections import defaultdict,deque
def userAccesses(logs):
    user_map = defaultdict(list)
    for time,user,resource in logs:
        time = int(time)
        if user in user_map:
            print(user_map[user])
            start , end = user_map[user]
            if time < start:
                user_map[user][0] = time
            if time > end:
                user_map[user][1] = time

        else:
            user_map[user].extend([time,time])
    print(user_map)

logs1 = [
    ["58523", "user_1", "resource_1"],
    ["62314", "user_2", "resource_2"],
    ["54001", "user_1", "resource_3"],
    ["200", "user_6", "resource_5"],    
    ["215", "user_6", "resource_4"],
    ["54060", "user_2", "resource_3"],
    ["53760", "user_3", "resource_3"],
    ["58522", "user_22", "resource_1"],
    ["53651", "user_5", "resource_3"],
    ["2", "user_6", "resource_1"],
    ["100", "user_6", "resource_6"],
    ["400", "user_7", "resource_2"],
    ["100", "user_8", "resource_6"],
    ["54359", "user_1", "resource_3"],
]

logs11 = [
    [58523, "user_1", "resource_1"],
    [62314, "user_2", "resource_2"],
    [54001, "user_1", "resource_3"],
    [200, "user_6", "resource_5"],    
    [215, "user_6", "resource_4"],
    [54060, "user_2", "resource_3"],
    [53760, "user_3", "resource_3"],
    [58522, "user_22", "resource_1"],
    ["53651", "user_5", "resource_3"],
    ["2", "user_6", "resource_1"],
    ["100", "user_6", "resource_6"],
    ["400", "user_7", "resource_2"],
    ["100", "user_8", "resource_6"],
    ["54359", "user_1", "resource_3"],
]
# userAccesses(logs1)

def get_resource_logs(logs):
    resource_dict = defaultdict(list)
    result = {}
    for log in logs:
        resource_dict[log[2]].append(int(log[0]))
    # print(resource_dict)
    for resource, time in resource_dict.items():
        time.sort()
        res = 0
        s, e = 0, 0
        #sliding window, bcs we need to see in any 5 min window if the diff is <= 300
        while e < (len(time)-1):
            diff = time[e] - time[s]
            if diff <= 300:
                res = max(res, e -s +1)
                e += 1
            else:
                s += 1
        result[resource] = res
    resource = max(result, key=result.get)#get the max key based on value
    print((resource, result[resource]))

get_resource_logs(logs1)
