class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        if len(keyTime) == 1:
            return []
        times_map = defaultdict(list)
        for i in range(len(keyName)):
            #convert string to minutes
            time = int(keyTime[i][0:2]) * 60 + int(keyTime[i][3:])
            times_map[keyName[i]].append(time)
        print(times_map)
        res = []
        for name, times in times_map.items():
            times.sort() #sort
            count = 0
            for i in range(len(times)-2):
                diff = times[i+2] - times[i]#for every 3 times, if diff between last and first is < 60, then append and break since we don't have to append it again
                if diff <= 60:
                    res.append(name)
                    break
        return sorted(res)