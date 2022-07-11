"""
Calculate the total wait time for a customer C to speak to an agent given N agents, M customers, and T[] time for an agent to serve a customer. T[i] represents the amount of time it takes for an agent i to serve one customer. One agent can serve one customer at a time. All N agents can serve concurrently. The customer chooses the agent with the lowest wait time.

Examples:

N = 2
M = 2
T = [4, 5]
First customer chooses agent 1. Second customer chooses agent 2.
Customer C will wait 4 minutes.
N = 2
M = 4
T = [4, 5]
First customer chooses agent 1. Second customer chooses agent 2.
Third customer chooses agent 1. Forth customer chooses agent 2.
Customer C will wait 8 minutes.
Initial questions:

Bounds on N and M - No bounds
Can N or M be zero - Both can be zero
Are the T values constant - Yes
Are the T values integers - Yes


"""
import heapq
def wait_time(N, M, T):
    """N agents with serving times T, M customers
    """
    if M < N:#if customers < agents, return 0
        return 0
    # put all agents busy
    agent_times = [(t, i) for i, t in enumerate(T)] #put agents with times, agent number in heap
    heapq.heapify(agent_times)

    # serve all other (M - N) customers with the agent finishes first
    for _ in range(M - N):#for the next customers
        t, i = heapq.heappop(agent_times)#pop bcs initial customers finished processing
        heapq.heappush(agent_times, (t + T[i], i))#push customers with wait time, t + T[i], wait time + processing time for agent

    # the next available agent working time is the wait time for C
    return agent_times[0][0] #the next customer who arrives will get the first slot, hence [0][0]

#n - agents, m - customer
print(wait_time(2, 4, [4,5]))
