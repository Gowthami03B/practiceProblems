"""
Given there exists a network flow that makes up a majority of bandwidth 
(flow using more than 50% of bandwidth), could you identify it given a stream of packets? 
You only need to tell the flow ID at the end of the stream.

default solution is hashmap (O(N))
another is sorting, but here its immutable
hence using the below logic to find the majority flowid causing > 50% bandwidth
we sum count when our candidate is the same, else we subtract, when count goes below 0, we assign a new
candidate
"""
def majorityFlow(stream, flow):
    total_bandwidth = sum(stream)//2
    print(total_bandwidth)
    count = 0
    candidate = None
    for i in range(len(stream)):
        if count <= 0:
            candidate = flow[i]
        count += stream[i] if flow[i] == candidate else -stream[i]
        if count > total_bandwidth:
            return candidate
    return candidate

flow = ['A', 'A', 'A', 'B', 'B', 'C', 'B', 'A' ]
stream = [2, 6, 2, 1, 1, 10, 1, 2]
flow1 = ['A', 'B', 'A', 'B', 'C', 'A' ,'A']
stream1 = [1,1,1,1,1,1,1]
print(majorityFlow(stream,flow))
