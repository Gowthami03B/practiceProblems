"""
Re-order Array Based on Dictionary
I had an interview with Bloomberg recently and I received a question that I didn't know how to solve. If anyone has any idea of how to solve the question or if it's on Leetcode then I would really appreciate it. I want to know the optimal solution.

Consider a vector of employees with a name and their title:
[<John, Manager>, <Sally, CTO>, <Sam, CEO>, <Drax, Engineer>, <Bob, CFO>, <Daniel, Engineer>]

And a dictionary where the keys report to the values:
{[CTO, CEO], [Manager, CTO], [Engineer, Manager], [CFO, CEO]}

Re-order the vector of employees according to the dictionary mappings. The vector of employees can be extremely big, however the dictionary only contains the title orderings.

Sample output:
[<Drax, Engineer>, <Daniel, Engineer>, <John, Manager>, <Sally, CTO>, <Bob, CFO>, <Sam, CEO>]

Note that in this case, CTO and CFO both report to CEO so they are both before CEO and above the next biggest thing, which is manager. They can also be in either order in this case.
"""
from sortedcontainers import SortedDict
from collections import defaultdict,deque
def reorderArray(employees,order):
    indegree_dict = defaultdict(list)
    highest_pos, count = "",0
    emp_map=defaultdict(list)
    res = []
    for emp, mgr in order.items():
        indegree_dict[mgr].append(emp)
        if len(indegree_dict[mgr]) > count:
            count = len(indegree_dict[mgr])
            highest_pos = mgr
    
    for emp, title in employees:
            emp_map[title].append(emp)

    def dfs(highest_pos):
        queue = deque(([highest_pos]))
        while queue:
            for _ in range(len(queue)):
                pos = queue.popleft()
                for emp in emp_map[pos]:
                    res.append((emp,pos))

                for child in indegree_dict[pos]:
                    queue.append(child)

    dfs(highest_pos)
    return res[::-1]

employees=[('John', 'Manager'), ('Sally', 'CTO'), ('Sam', 'CEO'), ('Drax', 'Engineer'), ('Bob', 'CFO'), ('Daniel', 'Engineer')]
order={'CTO':'CEO', 'Manager':'CTO', 'Engineer': 'Manager', 'CFO': 'CEO'}
print(reorderArray(employees, order))
