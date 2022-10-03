"""
Given a number, how many steps does it take to reach 1 given that:

If the number is even, divide it by two.
If the number is odd, triple it and add one.
I gave iterative and recusive solutions and also solution with caching results.
And they wanted me to save, not only the steps it takes to get 5 but also 
the steps to get 16, 8, 4,2 in the same function.
Example N=5
5, 16, 8, 4, 2, 1 -> 5 steps
"""
import collections
def stepsToReachOne(num):
    queue = collections.deque()
    queue.append((num,0))
    steps_map = collections.defaultdict(int)
    while queue:
        curr,steps = queue.popleft()
        if curr == 1:
            print(steps_map)
            return steps
        nextnode = curr//2 if not curr%2 else (curr*3)+1
        queue.append((nextnode, steps+1)) 
        steps_map[nextnode] = steps+1
    
print(calculate_steps(15))
