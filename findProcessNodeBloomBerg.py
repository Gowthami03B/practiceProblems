"""
First Problem: A process tree has crashed and you are given a sequence of it's nodes in random order, each representing a process and possible child(s). Each node has at most two child process. Find the root process node

Input:
{5 : [], 1: [2, 3], 4 : [], 3: [6], 6 : [], 2 : [4, 5]}

 			1
 		/      \
 	2            3
 /     \          / 
 4     5         6
 """
def findProcessNodeBloomBerg(nodes):
    indegree = [0] * len(nodes)
    for key, value in nodes.items():
        for val in value:
            indegree[val-1] += 1
    print(indegree)
    for idx, val in enumerate(indegree):
        if val == 0:
            return idx + 1

def findProcessNodeSets(ip): 
    root_node = set()
    for node in ip:
        root_node.add(node)

    for eachNode, children in ip.items():
        for eachChild in children:
            if eachChild in root_node:
                root_node.remove(eachChild)

    return root_node

nodes = {5 : [], 1: [2, 3], 4 : [], 3: [6], 6 : [], 2 : [4, 5]}
print(findProcessNodeSets(nodes))
