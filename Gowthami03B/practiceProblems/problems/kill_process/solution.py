class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        graph = defaultdict(list)
        for i in range(len(ppid)):
            graph[ppid[i]].append(pid[i])
            
        if kill not in graph:
            return [kill]
        # for i in range(len(pid)):
        #     if pid[i] not in graph:
        #         graph[pid[i]] = []
        queue = deque([kill])
        res = []
        while queue:
            curr = queue.popleft()
            res.append(curr)
            for child in graph[curr]:
                queue.append(child)
        return res
            