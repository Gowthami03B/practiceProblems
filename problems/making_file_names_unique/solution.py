class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        seen = {}
        res = []
        for i in names:
            if i not in seen:#it's not in seen we append to res
                seen[i] = 0#append 0 initially
                res.append(i)
            else:
                s = i#temp var s
                while s in seen:#we need to iteratively check if var(1),var(2) are already in res
                    seen[i] += 1#increment count
                    s = i + "(" + str(seen[i]) + ")"#check if the new string is in map
                seen[s] = 0
                res.append(s)
        return res
            