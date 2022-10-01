"""
 Min Steps to Generate Number
 Given an int n. You can use only 2 operations:

multiply by 2
integer division by 3 (e.g. 10 / 3 = 3)
Find the minimum number of steps required to generate n from 1.
"""
from collections import deque
def num_steps(n):
  # initialize queue with 1
  """
  Build a binary tree with the results from the two possible computations ( x / 3 and x * 2) as children. Then do a BFS.
An optimisation is implemented by using a "seen" set() to skip previously seen results.
This helps avoid rebuilding preiously traversed SubTrees. 
For example, in search of n = 16, you would begin to build three "2" subtrees and two "1" if you didnt ignore the parents to those subtrees.
  """
  queue = deque([1])#root of the binary tree
  no_of_steps = 0
  visited=set()
  while(queue):
    for i in range(len(queue)):
      cur_number = queue.popleft()#pop current node
      if cur_number == n:
          return no_of_steps
      if cur_number in visited:
          continue
      muliply_by_2 = int(cur_number * 2) #calculate the left and right subtrees
      divide_by_3 = int(cur_number / 3)
      visited.add(cur_number)
      # append multiplication and division results to queue
      queue.append(muliply_by_2)
      queue.append(divide_by_3)
    no_of_steps += 1
  return steps

print(num_steps(10))

def minNumber2(n):
    q=deque([(1,0)])
    seen=set()

    while q:
        res,ops=q.popleft()

        if res==n:
            return ops
        if res//3 not in seen:
            q.append((res//3,ops+1))
            seen.add(res//3)

        if res*2 not in seen:
            q.append((res*2,ops+1))
            seen.add(res*2)

print(minNumber2(10)) 
print(minNumber2(16)) 
